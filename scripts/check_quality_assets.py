#!/usr/bin/env python3
"""Validate top-tier paper quality assets.

This check is intentionally static. It does not claim that the skills produce
top-tier output; it makes sure the repository contains the evaluation assets
needed to test story, sentence, AI-smell, and validation behavior.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FIXTURES = {
    "abstract_overclaim.md",
    "introduction_gap_fake.md",
    "related_work_paper_list.md",
    "methods_module_directory.md",
    "results_table_narration.md",
    "discussion_wishlist.md",
    "conclusion_claim_resurrection.md",
    "caption_mechanism_overclaim.md",
    "response_false_revision.md",
    "validation_not_run_ready.md",
    "chinese_notes_source_expansion.md",
}

REQUIRED_RUBRIC_KEYS = {
    "claim_evidence_alignment",
    "story_spine",
    "sentence_necessity",
    "ai_smell",
    "venue_awareness",
    "response_truthfulness",
    "validation_honesty",
}


def word_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").split())


def main() -> int:
    errors: list[str] = []

    fixture_dir = ROOT / "tests/fixtures/long"
    if not fixture_dir.exists():
        errors.append("Missing tests/fixtures/long")
    else:
        found = {p.name for p in fixture_dir.glob("*.md")}
        missing = REQUIRED_FIXTURES - found
        if missing:
            errors.append(f"Missing long fixtures: {', '.join(sorted(missing))}")
        for name in sorted(REQUIRED_FIXTURES & found):
            path = fixture_dir / name
            if word_count(path) < 120:
                errors.append(f"{path.relative_to(ROOT)} is too short for a long-form fixture")
            text = path.read_text(encoding="utf-8")
            for marker in ("Expected audit pressure", "Failure modes"):
                if marker not in text:
                    errors.append(f"{path.relative_to(ROOT)} missing marker: {marker}")

    rubric_json = ROOT / "evals/top_tier_rubric.json"
    rubric_md = ROOT / "evals/manual-rubric.md"
    if not rubric_json.exists():
        errors.append("Missing evals/top_tier_rubric.json")
    else:
        try:
            data = json.loads(rubric_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid evals/top_tier_rubric.json: {exc}")
        else:
            criteria = data.get("criteria")
            if not isinstance(criteria, dict):
                errors.append("evals/top_tier_rubric.json missing criteria object")
            else:
                missing = REQUIRED_RUBRIC_KEYS - set(criteria)
                if missing:
                    errors.append(f"Rubric missing criteria: {', '.join(sorted(missing))}")

    if not rubric_md.exists():
        errors.append("Missing evals/manual-rubric.md")
    elif "Sentence necessity" not in rubric_md.read_text(encoding="utf-8"):
        errors.append("evals/manual-rubric.md missing Sentence necessity")

    if errors:
        print("Quality asset check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Quality asset check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
