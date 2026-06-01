#!/usr/bin/env python3
"""Validate structured prompt expected-behavior specs.

The specs are YAML files written as JSON objects so this script needs only the
Python standard library. When output files are provided, it also checks simple
string expectations.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

REQUIRED_KEYS = {
    "case",
    "prompt",
    "must_include",
    "must_not_include",
    "forbidden_claims",
    "required_status",
    "allowed_behavior",
}

OPTIONAL_LIST_KEYS = {
    "forbidden_regex",
    "forbidden_claim_patterns",
    "required_sections",
    "required_table_columns",
}

OPTIONAL_DICT_KEYS = {
    "status_constraints",
    "manual_rubric",
}

OPTIONAL_COMPLEX_DICT_KEYS = {
    "semantic_expectations",
    "structured_expectations",
}


def _load_spec(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON-compatible YAML: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected an object")
    return data


def _expect_list(path: Path, data: dict[str, Any], key: str) -> list[str]:
    value = data.get(key)
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{path}: {key} must be a list of strings")
    return value


def _expect_dict(path: Path, data: dict[str, Any], key: str) -> dict[str, str]:
    value = data.get(key)
    if not isinstance(value, dict) or not all(
        isinstance(k, str) and isinstance(v, str) for k, v in value.items()
    ):
        raise ValueError(f"{path}: {key} must be an object of string values")
    return value


def _expect_semantic_expectations(path: Path, data: dict[str, Any]) -> dict[str, list[Any]]:
    value = data.get("semantic_expectations")
    if not isinstance(value, dict):
        raise ValueError(f"{path}: semantic_expectations must be an object")
    parsed: dict[str, list[Any]] = {}
    for group, expectations in value.items():
        if not isinstance(group, str):
            raise ValueError(f"{path}: semantic_expectations group names must be strings")
        if not isinstance(expectations, list):
            raise ValueError(f"{path}: semantic_expectations.{group} must be a list")
        for item in expectations:
            if isinstance(item, str):
                continue
            if not isinstance(item, dict):
                raise ValueError(f"{path}: semantic_expectations.{group} entries must be strings or objects")
            name = item.get("name")
            required_terms = item.get("required_terms")
            any_terms = item.get("any_terms", [])
            forbidden_terms = item.get("forbidden_terms", [])
            if not isinstance(name, str) or not name:
                raise ValueError(f"{path}: semantic_expectations.{group} object missing name")
            if not isinstance(required_terms, list) or not all(
                isinstance(term, str) and term for term in required_terms
            ):
                raise ValueError(
                    f"{path}: semantic_expectations.{group}.{name} required_terms must be non-empty strings"
                )
            if not isinstance(any_terms, list) or not all(isinstance(term, str) and term for term in any_terms):
                raise ValueError(f"{path}: semantic_expectations.{group}.{name} any_terms must be strings")
            if not isinstance(forbidden_terms, list) or not all(
                isinstance(term, str) and term for term in forbidden_terms
            ):
                raise ValueError(f"{path}: semantic_expectations.{group}.{name} forbidden_terms must be strings")
        parsed[group] = expectations
    return parsed


def _expect_structured_expectations(path: Path, data: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    value = data.get("structured_expectations")
    if not isinstance(value, dict):
        raise ValueError(f"{path}: structured_expectations must be an object")
    parsed: dict[str, list[dict[str, Any]]] = {}
    for group, rows in value.items():
        if not isinstance(group, str):
            raise ValueError(f"{path}: structured_expectations group names must be strings")
        if not isinstance(rows, list):
            raise ValueError(f"{path}: structured_expectations.{group} must be a list")
        parsed_rows: list[dict[str, Any]] = []
        for row in rows:
            if not isinstance(row, dict):
                raise ValueError(f"{path}: structured_expectations.{group} entries must be objects")
            name = row.get("name")
            required_terms = row.get("required_terms")
            forbidden_terms = row.get("forbidden_terms", [])
            if not isinstance(name, str) or not name:
                raise ValueError(f"{path}: structured_expectations.{group} object missing name")
            if not isinstance(required_terms, list) or not all(
                isinstance(term, str) and term for term in required_terms
            ):
                raise ValueError(
                    f"{path}: structured_expectations.{group}.{name} required_terms must be non-empty strings"
                )
            if not isinstance(forbidden_terms, list) or not all(
                isinstance(term, str) and term for term in forbidden_terms
            ):
                raise ValueError(f"{path}: structured_expectations.{group}.{name} forbidden_terms must be strings")
            parsed_rows.append(row)
        parsed[group] = parsed_rows
    return parsed


def validate_specs(spec_dir: Path) -> list[str]:
    errors: list[str] = []

    if not spec_dir.exists():
        return [f"Missing expected-behavior directory: {spec_dir}"]

    obsolete = sorted(path.name for path in spec_dir.glob("*.md"))
    if obsolete:
        errors.append(f"Expected specs must be .yaml, found obsolete .md files: {', '.join(obsolete)}")

    specs = sorted(spec_dir.glob("*.yaml"))
    if not specs:
        errors.append(f"No .yaml expected-behavior specs found in {spec_dir}")
        return errors

    seen_cases: set[str] = set()
    for path in specs:
        try:
            data = _load_spec(path)
            missing = REQUIRED_KEYS - data.keys()
            if missing:
                raise ValueError(f"{path}: missing keys: {', '.join(sorted(missing))}")

            case = data["case"]
            prompt = data["prompt"]
            if not isinstance(case, str) or not case:
                raise ValueError(f"{path}: case must be a non-empty string")
            if case in seen_cases:
                raise ValueError(f"{path}: duplicate case {case}")
            seen_cases.add(case)
            if not isinstance(prompt, str) or not prompt.endswith(".md"):
                raise ValueError(f"{path}: prompt must be a .md filename")

            for key in ("must_include", "must_not_include", "forbidden_claims", "allowed_behavior"):
                _expect_list(path, data, key)
            _expect_dict(path, data, "required_status")
            for key in OPTIONAL_LIST_KEYS:
                if key in data:
                    values = _expect_list(path, data, key)
                    if key in {"forbidden_regex", "forbidden_claim_patterns"}:
                        for pattern in values:
                            try:
                                re.compile(pattern)
                            except re.error as exc:
                                raise ValueError(f"{path}: invalid forbidden_regex {pattern}: {exc}") from exc
            for key in OPTIONAL_DICT_KEYS:
                if key in data:
                    _expect_dict(path, data, key)
            for key in OPTIONAL_COMPLEX_DICT_KEYS:
                if key in data:
                    if key == "semantic_expectations":
                        _expect_semantic_expectations(path, data)
                    elif key == "structured_expectations":
                        _expect_structured_expectations(path, data)

            if data["forbidden_claims"] and not (
                data["must_not_include"]
                or data.get("forbidden_regex")
                or data.get("forbidden_claim_patterns")
            ):
                raise ValueError(
                    f"{path}: forbidden_claims must be backed by must_not_include, "
                    "forbidden_regex, or forbidden_claim_patterns"
                )

            if path.stem + ".md" != prompt:
                raise ValueError(f"{path}: prompt should match spec basename")
        except ValueError as exc:
            errors.append(str(exc))

    return errors


def _find_output(outputs_dir: Path, case: str) -> Path | None:
    for suffix in (".out", ".txt", ".md"):
        candidate = outputs_dir / f"{case}{suffix}"
        if candidate.exists():
            return candidate
    return None


def check_outputs(spec_dir: Path, outputs_dir: Path, cases: set[str] | None = None) -> list[str]:
    errors = validate_specs(spec_dir)
    if errors:
        return errors

    for spec_path in sorted(spec_dir.glob("*.yaml")):
        data = _load_spec(spec_path)
        case = data["case"]
        if cases is not None and case not in cases:
            continue
        output_path = _find_output(outputs_dir, case)
        if output_path is None:
            errors.append(f"{case}: missing output file in {outputs_dir}")
            continue

        output = output_path.read_text(encoding="utf-8")
        output_lower = output.lower()
        normalized_lines = [" ".join(line.lower().split()) for line in output.splitlines()]

        for item in data["must_include"]:
            if item.lower() not in output_lower:
                errors.append(f"{case}: missing required text: {item}")

        for item in data["must_not_include"]:
            if item.lower() in output_lower:
                errors.append(f"{case}: forbidden text found: {item}")

        for pattern in data.get("forbidden_regex", []):
            if re.search(pattern, output, flags=re.IGNORECASE | re.MULTILINE):
                errors.append(f"{case}: forbidden regex matched: {pattern}")

        for pattern in data.get("forbidden_claim_patterns", []):
            if re.search(pattern, output, flags=re.IGNORECASE | re.MULTILINE):
                errors.append(f"{case}: forbidden claim pattern matched: {pattern}")

        for section in data.get("required_sections", []):
            if section.lower() not in output_lower:
                errors.append(f"{case}: missing required section: {section}")

        for column in data.get("required_table_columns", []):
            if column.lower() not in output_lower:
                errors.append(f"{case}: missing required table column: {column}")

        for label, status in data["required_status"].items():
            if label.lower() not in output_lower:
                errors.append(f"{case}: missing status label: {label}")
            if status.lower() not in output_lower:
                errors.append(f"{case}: missing expected status value: {status}")

        for group, expectations in data.get("semantic_expectations", {}).items():
            for item in expectations:
                if isinstance(item, str):
                    if item.lower() not in output_lower:
                        errors.append(f"{case}: missing semantic expectation {group}: {item}")
                    continue
                name = item["name"]
                for term in item.get("required_terms", []):
                    if term.lower() not in output_lower:
                        errors.append(f"{case}: semantic expectation {group}.{name} missing term: {term}")
                any_terms = item.get("any_terms", [])
                if any_terms and not any(term.lower() in output_lower for term in any_terms):
                    errors.append(
                        f"{case}: semantic expectation {group}.{name} missing any term: {', '.join(any_terms)}"
                    )
                for term in item.get("forbidden_terms", []):
                    if term.lower() in output_lower:
                        errors.append(f"{case}: semantic expectation {group}.{name} forbidden term found: {term}")

        for group, rows in data.get("structured_expectations", {}).items():
            for row in rows:
                name = row["name"]
                required_terms = [" ".join(term.lower().split()) for term in row["required_terms"]]
                forbidden_terms = [" ".join(term.lower().split()) for term in row.get("forbidden_terms", [])]
                matches = [
                    line
                    for line in normalized_lines
                    if all(term in line for term in required_terms)
                ]
                if not matches:
                    errors.append(
                        f"{case}: structured expectation {group}.{name} missing row with terms: "
                        f"{', '.join(row['required_terms'])}"
                    )
                    continue
                for line in matches:
                    for term in forbidden_terms:
                        if term in line:
                            errors.append(
                                f"{case}: structured expectation {group}.{name} forbidden term in matched row: {term}"
                            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec-dir", default="tests/expected", type=Path)
    parser.add_argument("--outputs-dir", type=Path)
    parser.add_argument("--case", action="append", help="Only check the named case; may be repeated")
    args = parser.parse_args()

    errors = (
        check_outputs(args.spec_dir, args.outputs_dir, set(args.case) if args.case else None)
        if args.outputs_dir
        else validate_specs(args.spec_dir)
    )

    if errors:
        print("Expected-behavior check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Expected-behavior check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
