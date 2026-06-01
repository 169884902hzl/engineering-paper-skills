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

ROOT = Path(__file__).resolve().parents[1]

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
    "json_expectations",
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


def _expect_json_expectations(path: Path, data: dict[str, Any]) -> dict[str, Any]:
    value = data.get("json_expectations")
    if not isinstance(value, dict):
        raise ValueError(f"{path}: json_expectations must be an object")
    for key in ("required_top_level_keys", "array_expectations"):
        if key in value and not isinstance(value[key], list):
            raise ValueError(f"{path}: json_expectations.{key} must be a list")
    for item in value.get("required_top_level_keys", []):
        if not isinstance(item, str) or not item:
            raise ValueError(f"{path}: json_expectations.required_top_level_keys entries must be strings")
    for item in value.get("array_expectations", []):
        if not isinstance(item, dict):
            raise ValueError(f"{path}: json_expectations.array_expectations entries must be objects")
        name = item.get("name")
        path_value = item.get("path")
        required_fields = item.get("required_fields", [])
        non_empty_fields = item.get("non_empty_fields", [])
        required_rows = item.get("required_rows", [])
        min_items = item.get("min_items", 0)
        if not isinstance(name, str) or not name:
            raise ValueError(f"{path}: json_expectations.array_expectations entry missing name")
        if not isinstance(path_value, str) or not path_value:
            raise ValueError(f"{path}: json_expectations.{name} missing path")
        if not isinstance(min_items, int) or min_items < 0:
            raise ValueError(f"{path}: json_expectations.{name}.min_items must be a non-negative integer")
        if not isinstance(required_fields, list) or not all(isinstance(field, str) for field in required_fields):
            raise ValueError(f"{path}: json_expectations.{name}.required_fields must be strings")
        if not isinstance(non_empty_fields, list) or not all(isinstance(field, str) for field in non_empty_fields):
            raise ValueError(f"{path}: json_expectations.{name}.non_empty_fields must be strings")
        if not isinstance(required_rows, list) or not all(isinstance(row, dict) for row in required_rows):
            raise ValueError(f"{path}: json_expectations.{name}.required_rows must be objects")
    for item in value.get("span_origin_checks", []):
        if not isinstance(item, dict):
            raise ValueError(f"{path}: json_expectations.span_origin_checks entries must be objects")
        name = item.get("name")
        path_value = item.get("path")
        fields = item.get("fields")
        source_file = item.get("source_file")
        if not isinstance(name, str) or not name:
            raise ValueError(f"{path}: json_expectations.span_origin_checks entry missing name")
        if not isinstance(path_value, str) or not path_value:
            raise ValueError(f"{path}: json_expectations.span_origin_checks.{name} missing path")
        if not isinstance(fields, list) or not all(isinstance(field, str) and field for field in fields):
            raise ValueError(f"{path}: json_expectations.span_origin_checks.{name}.fields must be strings")
        if not isinstance(source_file, str) or not source_file:
            raise ValueError(f"{path}: json_expectations.span_origin_checks.{name} missing source_file")
    for item in value.get("gold_row_expectations", []):
        if not isinstance(item, dict):
            raise ValueError(f"{path}: json_expectations.gold_row_expectations entries must be objects")
        for key in ("name", "output_path", "annotation_file", "annotation_path", "key"):
            if not isinstance(item.get(key), str) or not item[key]:
                raise ValueError(f"{path}: json_expectations.gold_row_expectations entry missing {key}")
        fields = item.get("fields")
        if not isinstance(fields, list) or not all(isinstance(field, str) and field for field in fields):
            raise ValueError(f"{path}: json_expectations.gold_row_expectations.{item['name']}.fields must be strings")
    return value


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
                    elif key == "json_expectations":
                        _expect_json_expectations(path, data)

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
    for suffix in (".out", ".txt", ".md", ".json"):
        candidate = outputs_dir / f"{case}{suffix}"
        if candidate.exists():
            return candidate
    return None


def _json_path(value: Any, path: str) -> Any:
    current = value
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            raise KeyError(path)
        current = current[part]
    return current


def _normalize_text(value: str) -> str:
    return " ".join(value.lower().split())


def _load_text_for_spec(path: str) -> str:
    source = ROOT / path
    if not source.exists():
        raise FileNotFoundError(path)
    return source.read_text(encoding="utf-8")


def _field_matches(actual: Any, expected: Any) -> bool:
    if isinstance(expected, list):
        return actual in expected
    if isinstance(expected, str) and isinstance(actual, str):
        return _normalize_text(expected) in _normalize_text(actual)
    return actual == expected


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

        if "json_expectations" in data:
            try:
                parsed_output = json.loads(output)
            except json.JSONDecodeError as exc:
                errors.append(f"{case}: output is not valid JSON for json_expectations: {exc}")
                continue

            json_spec = data["json_expectations"]
            for key in json_spec.get("required_top_level_keys", []):
                if not isinstance(parsed_output, dict) or key not in parsed_output:
                    errors.append(f"{case}: JSON output missing top-level key: {key}")

            for expectation in json_spec.get("array_expectations", []):
                name = expectation["name"]
                try:
                    rows = _json_path(parsed_output, expectation["path"])
                except KeyError:
                    errors.append(f"{case}: JSON expectation {name} missing path: {expectation['path']}")
                    continue
                if not isinstance(rows, list):
                    errors.append(f"{case}: JSON expectation {name} path is not an array")
                    continue
                min_items = expectation.get("min_items", 0)
                if len(rows) < min_items:
                    errors.append(f"{case}: JSON expectation {name} has {len(rows)} rows, expected {min_items}")
                required_fields = expectation.get("required_fields", [])
                non_empty_fields = expectation.get("non_empty_fields", [])
                for index, row in enumerate(rows):
                    if not isinstance(row, dict):
                        errors.append(f"{case}: JSON expectation {name} row {index} is not an object")
                        continue
                    for field in required_fields:
                        if field not in row:
                            errors.append(f"{case}: JSON expectation {name} row {index} missing field: {field}")
                    for field in non_empty_fields:
                        value = row.get(field)
                        if isinstance(value, str):
                            if not value.strip():
                                errors.append(
                                    f"{case}: JSON expectation {name} row {index} has empty field: {field}"
                                )
                        elif isinstance(value, list):
                            if not value or not all(isinstance(item, str) and item.strip() for item in value):
                                errors.append(
                                    f"{case}: JSON expectation {name} row {index} has empty list field: {field}"
                                )
                        elif value is None:
                            errors.append(f"{case}: JSON expectation {name} row {index} missing field: {field}")
                for required_row in expectation.get("required_rows", []):
                    matches = []
                    for row in rows:
                        if not isinstance(row, dict):
                            continue
                        if all(
                            field in row and _field_matches(row[field], expected)
                            for field, expected in required_row.items()
                        ):
                            matches.append(row)
                    if not matches:
                        errors.append(
                            f"{case}: JSON expectation {name} missing row matching: "
                            f"{json.dumps(required_row, sort_keys=True)}"
                        )

            for expectation in json_spec.get("span_origin_checks", []):
                name = expectation["name"]
                try:
                    rows = _json_path(parsed_output, expectation["path"])
                    source_text = _load_text_for_spec(expectation["source_file"])
                except (KeyError, FileNotFoundError) as exc:
                    errors.append(f"{case}: JSON span-origin expectation {name} cannot load source: {exc}")
                    continue
                if not isinstance(rows, list):
                    errors.append(f"{case}: JSON span-origin expectation {name} path is not an array")
                    continue
                normalized_source = _normalize_text(source_text)
                for index, row in enumerate(rows):
                    if not isinstance(row, dict):
                        errors.append(f"{case}: JSON span-origin expectation {name} row {index} is not an object")
                        continue
                    for field in expectation["fields"]:
                        value = row.get(field)
                        if not isinstance(value, str) or not value.strip():
                            errors.append(
                                f"{case}: JSON span-origin expectation {name} row {index} missing {field}"
                            )
                            continue
                        if _normalize_text(value) not in normalized_source:
                            errors.append(
                                f"{case}: JSON span-origin expectation {name} row {index} {field} "
                                f"not found in {expectation['source_file']}: {value}"
                            )

            for expectation in json_spec.get("gold_row_expectations", []):
                name = expectation["name"]
                try:
                    output_rows = _json_path(parsed_output, expectation["output_path"])
                    annotation = json.loads(_load_text_for_spec(expectation["annotation_file"]))
                    gold_rows = _json_path(annotation, expectation["annotation_path"])
                except (KeyError, FileNotFoundError, json.JSONDecodeError) as exc:
                    errors.append(f"{case}: JSON gold-row expectation {name} cannot load data: {exc}")
                    continue
                if not isinstance(output_rows, list) or not all(isinstance(row, dict) for row in output_rows):
                    errors.append(f"{case}: JSON gold-row expectation {name} output path is not object rows")
                    continue
                if not isinstance(gold_rows, list) or not all(isinstance(row, dict) for row in gold_rows):
                    errors.append(f"{case}: JSON gold-row expectation {name} annotation path is not object rows")
                    continue
                key = expectation["key"]
                output_by_key = {row.get(key): row for row in output_rows if isinstance(row.get(key), str)}
                for gold_row in gold_rows:
                    row_id = gold_row.get(key)
                    if not isinstance(row_id, str) or not row_id:
                        errors.append(f"{case}: JSON gold-row expectation {name} annotation row missing key {key}")
                        continue
                    output_row = output_by_key.get(row_id)
                    if output_row is None:
                        errors.append(f"{case}: JSON gold-row expectation {name} missing output row {key}={row_id}")
                        continue
                    for field in expectation["fields"]:
                        expected_value = gold_row.get(field)
                        actual_value = output_row.get(field)
                        if isinstance(expected_value, str) and isinstance(actual_value, str):
                            if _normalize_text(expected_value) != _normalize_text(actual_value):
                                errors.append(
                                    f"{case}: JSON gold-row expectation {name} {key}={row_id} "
                                    f"field {field} mismatch"
                                )
                        elif expected_value != actual_value:
                            errors.append(
                                f"{case}: JSON gold-row expectation {name} {key}={row_id} "
                                f"field {field} mismatch"
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
