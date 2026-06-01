#!/usr/bin/env python3
"""Static sanity check for the response diff fixture.

This script does not verify real manuscript edits. It ensures the repository's
response-diff fixture contains both verified and unsupported response claims so
the engineering-response skill can be tested against them.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests/fixtures/full_paper/response_old_new_diff.md"
ANNOTATION = ROOT / "tests/fixtures/full_paper/gold_annotations/response_old_new_diff.json"


def main() -> int:
    errors: list[str] = []
    if not FIXTURE.exists():
        errors.append(f"Missing {FIXTURE.relative_to(ROOT)}")
    if not ANNOTATION.exists():
        errors.append(f"Missing {ANNOTATION.relative_to(ROOT)}")

    if errors:
        print("Response diff check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    fixture = FIXTURE.read_text(encoding="utf-8")
    try:
        annotation = json.loads(ANNOTATION.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"Response diff check failed:\n- Invalid annotation JSON: {exc}")
        return 1

    for heading in ("Old Manuscript Excerpt", "New Manuscript Excerpt", "Draft Response"):
        if heading not in fixture:
            errors.append(f"{FIXTURE.relative_to(ROOT)} missing heading: {heading}")

    for claim in annotation.get("verified_changes", []):
        if not isinstance(claim, str) or not claim:
            errors.append("verified_changes must contain non-empty strings")

    draft_response = fixture.split("## Draft Response", 1)[-1]
    for claim in annotation.get("unsupported_response_claims", []):
        if not isinstance(claim, str) or not claim:
            errors.append("unsupported_response_claims must contain non-empty strings")
            continue
        if claim.lower() not in draft_response.lower():
            errors.append(f"Draft response missing unsupported claim trigger: {claim}")

    if errors:
        print("Response diff check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Response diff check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
