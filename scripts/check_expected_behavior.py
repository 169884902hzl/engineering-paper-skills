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
    "required_sections",
    "required_table_columns",
}

OPTIONAL_DICT_KEYS = {
    "status_constraints",
    "manual_rubric",
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
                    if key == "forbidden_regex":
                        for pattern in values:
                            try:
                                re.compile(pattern)
                            except re.error as exc:
                                raise ValueError(f"{path}: invalid forbidden_regex {pattern}: {exc}") from exc
            for key in OPTIONAL_DICT_KEYS:
                if key in data:
                    _expect_dict(path, data, key)

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


def check_outputs(spec_dir: Path, outputs_dir: Path) -> list[str]:
    errors = validate_specs(spec_dir)
    if errors:
        return errors

    for spec_path in sorted(spec_dir.glob("*.yaml")):
        data = _load_spec(spec_path)
        case = data["case"]
        output_path = _find_output(outputs_dir, case)
        if output_path is None:
            errors.append(f"{case}: missing output file in {outputs_dir}")
            continue

        output = output_path.read_text(encoding="utf-8")
        output_lower = output.lower()

        for item in data["must_include"]:
            if item.lower() not in output_lower:
                errors.append(f"{case}: missing required text: {item}")

        for item in data["must_not_include"]:
            if item.lower() in output_lower:
                errors.append(f"{case}: forbidden text found: {item}")

        for pattern in data.get("forbidden_regex", []):
            if re.search(pattern, output, flags=re.IGNORECASE | re.MULTILINE):
                errors.append(f"{case}: forbidden regex matched: {pattern}")

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

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec-dir", default="tests/expected", type=Path)
    parser.add_argument("--outputs-dir", type=Path)
    args = parser.parse_args()

    errors = (
        check_outputs(args.spec_dir, args.outputs_dir)
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
