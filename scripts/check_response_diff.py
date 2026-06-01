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


def contains_phrase(text: str, phrase: str) -> bool:
    return " ".join(phrase.lower().split()) in " ".join(text.lower().split())


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

    old_excerpt = fixture.split("## Old Manuscript Excerpt", 1)[-1].split("## New Manuscript Excerpt", 1)[0]
    new_excerpt = fixture.split("## New Manuscript Excerpt", 1)[-1].split("## Draft Response", 1)[0]
    draft_response = fixture.split("## Draft Response", 1)[-1]
    for claim in annotation.get("unsupported_response_claims", []):
        if not isinstance(claim, str) or not claim:
            errors.append("unsupported_response_claims must contain non-empty strings")
            continue
        if not contains_phrase(draft_response, claim):
            errors.append(f"Draft response missing unsupported claim trigger: {claim}")
        if contains_phrase(new_excerpt, claim):
            errors.append(f"Unsupported response claim appears in new manuscript excerpt: {claim}")

    for check in annotation.get("semantic_change_checks", []):
        if not isinstance(check, dict):
            errors.append("semantic_change_checks entries must be objects")
            continue
        name = check.get("name")
        if not isinstance(name, str) or not name:
            errors.append("semantic_change_checks entries must have a name")
            continue
        for term in check.get("new_excerpt_terms", []):
            if not isinstance(term, str) or not term:
                errors.append(f"{name}: new_excerpt_terms must be non-empty strings")
                continue
            if not contains_phrase(new_excerpt, term):
                errors.append(f"{name}: new manuscript excerpt missing term: {term}")
        for term in check.get("draft_response_terms", []):
            if not isinstance(term, str) or not term:
                errors.append(f"{name}: draft_response_terms must be non-empty strings")
                continue
            if not contains_phrase(draft_response, term):
                errors.append(f"{name}: draft response missing term: {term}")
        for term in check.get("draft_response_forbidden_terms", []):
            if not isinstance(term, str) or not term:
                errors.append(f"{name}: draft_response_forbidden_terms must be non-empty strings")
                continue
            if not contains_phrase(draft_response, term):
                errors.append(f"{name}: draft response should contain unsafe term for fixture pressure: {term}")
            if contains_phrase(new_excerpt, term):
                errors.append(f"{name}: unsafe response term appears in new manuscript excerpt: {term}")

    for check in annotation.get("response_claim_checks", []):
        if not isinstance(check, dict):
            errors.append("response_claim_checks entries must be objects")
            continue
        comment_id = check.get("comment_id")
        reviewer_concern = check.get("reviewer_concern")
        response_claim = check.get("response_claim")
        expected_status = check.get("expected_status")
        if not all(isinstance(value, str) and value for value in (
            comment_id,
            reviewer_concern,
            response_claim,
            expected_status,
        )):
            errors.append("response_claim_checks entries require comment_id, reviewer_concern, response_claim, and expected_status")
            continue
        for term in check.get("required_new_excerpt_terms", []):
            if not isinstance(term, str) or not term:
                errors.append(f"{comment_id}: required_new_excerpt_terms must be non-empty strings")
                continue
            if not contains_phrase(new_excerpt, term):
                errors.append(f"{comment_id}: new manuscript excerpt missing term required for semantic match: {term}")
        for term in check.get("required_response_terms", []):
            if not isinstance(term, str) or not term:
                errors.append(f"{comment_id}: required_response_terms must be non-empty strings")
                continue
            if not contains_phrase(draft_response, term):
                errors.append(f"{comment_id}: draft response missing claimed-change term: {term}")
        for term in check.get("forbidden_new_excerpt_terms", []):
            if not isinstance(term, str) or not term:
                errors.append(f"{comment_id}: forbidden_new_excerpt_terms must be non-empty strings")
                continue
            if contains_phrase(new_excerpt, term):
                errors.append(f"{comment_id}: unsupported response claim appears in new manuscript excerpt: {term}")
        for term in check.get("unsupported_reason_terms", []):
            if not isinstance(term, str) or not term:
                errors.append(f"{comment_id}: unsupported_reason_terms must be non-empty strings")
                continue
            if not contains_phrase(draft_response, term):
                errors.append(f"{comment_id}: fixture no longer exposes unsupported reason term: {term}")

    if "complete pipeline for robust insertion" not in old_excerpt:
        errors.append("Old manuscript excerpt no longer contains the original overclaim pressure")

    if errors:
        print("Response diff check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Response diff check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
