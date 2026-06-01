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
    "paragraph_transition",
    "section_dependency",
    "ai_smell",
    "venue_awareness",
    "response_truthfulness",
    "validation_honesty",
}

REQUIRED_FULL_PAPER_ASSETS = {
    "fixture": "tests/fixtures/full_paper/robot_active_observation_flawed_manuscript.md",
    "prompt": "tests/prompts/full_paper_audit.md",
    "expected": "tests/expected/full_paper_audit.yaml",
    "golden": "tests/outputs/golden/full_paper_audit.md",
    "eval_result": "evals/results/775ee48_full_paper_manual_eval.jsonl",
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

    for label, rel_path in REQUIRED_FULL_PAPER_ASSETS.items():
        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"Missing full-paper {label}: {rel_path}")

    full_fixture = ROOT / REQUIRED_FULL_PAPER_ASSETS["fixture"]
    if full_fixture.exists():
        words = word_count(full_fixture)
        if words < 1500:
            errors.append(f"{full_fixture.relative_to(ROOT)} is too short for a full-paper fixture")
        fixture_text = full_fixture.read_text(encoding="utf-8")
        for marker in (
            "Draft Abstract",
            "Draft Introduction",
            "Draft Methods",
            "Draft Experiments",
            "Draft Discussion",
            "Draft Conclusion",
            "Reviewer Comments",
            "Expected audit pressure",
            "Failure modes",
        ):
            if marker not in fixture_text:
                errors.append(f"{full_fixture.relative_to(ROOT)} missing marker: {marker}")

    full_golden = ROOT / REQUIRED_FULL_PAPER_ASSETS["golden"]
    if full_golden.exists():
        golden_text = full_golden.read_text(encoding="utf-8")
        for marker in (
            "Story spine",
            "Paragraph transition audit",
            "Section dependency audit",
            "Sentence role samples",
            "Response truthfulness",
            "Validation result",
        ):
            if marker not in golden_text:
                errors.append(f"{full_golden.relative_to(ROOT)} missing marker: {marker}")

    eval_result = ROOT / REQUIRED_FULL_PAPER_ASSETS["eval_result"]
    if eval_result.exists():
        for line_no, line in enumerate(eval_result.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"{eval_result.relative_to(ROOT)} line {line_no} invalid JSON: {exc}")
                continue
            for key in (
                "fixture",
                "gold_output",
                "runtime_model_executed",
                "review_type",
                "claim_evidence_alignment",
                "story_spine",
                "sentence_necessity",
                "paragraph_transition",
                "section_dependency",
                "response_truthfulness",
                "validation_honesty",
            ):
                if key not in record:
                    errors.append(f"{eval_result.relative_to(ROOT)} line {line_no} missing key: {key}")

    if errors:
        print("Quality asset check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Quality asset check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
