#!/usr/bin/env python3
"""Optional prompt regression runner for the skill test prompts."""

from __future__ import annotations

import argparse
import shlex
import subprocess
import sys
from pathlib import Path

from check_expected_behavior import check_outputs, validate_specs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt-dir", default="tests/prompts", type=Path)
    parser.add_argument("--expected-dir", default="tests/expected", type=Path)
    parser.add_argument("--output-dir", default="tests/outputs", type=Path)
    parser.add_argument("--case", action="append", help="Run only the named case; may be repeated")
    parser.add_argument(
        "--require-command",
        action="store_true",
        help="Fail if --command-template is not provided. Use in behavior-regression CI.",
    )
    parser.add_argument(
        "--command-template",
        help=(
            "Command template with {prompt}, {output}, and {name} placeholders. "
            "Example: 'codex exec --prompt-file {prompt} --output {output}'"
        ),
    )
    args = parser.parse_args()

    spec_errors = validate_specs(args.expected_dir)
    if spec_errors:
        print("Expected-behavior specs are invalid:")
        for error in spec_errors:
            print(f"- {error}")
        return 1

    if not args.command_template:
        if args.require_command:
            print("Prompt command template is required but was not provided.")
            return 2
        print("Spec validation passed; prompt regression NOT_RUN because no command template was provided.")
        return 0

    args.output_dir.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    selected_cases = set(args.case) if args.case else None

    for prompt in sorted(args.prompt_dir.glob("*.md")):
        name = prompt.stem
        if selected_cases is not None and name not in selected_cases:
            continue
        output = args.output_dir / f"{name}.out"
        command = args.command_template.format(
            prompt=shlex.quote(str(prompt)),
            output=shlex.quote(str(output)),
            name=shlex.quote(name),
        )
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if not output.exists() or output.stat().st_size == 0:
            output.write_text(result.stdout, encoding="utf-8")
        if result.returncode != 0:
            stderr = result.stderr.strip()
            failures.append(f"{name}: command failed with {result.returncode}: {stderr}")

    failures.extend(check_outputs(args.expected_dir, args.output_dir, selected_cases))

    if failures:
        print("Prompt regression failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Prompt regression passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
