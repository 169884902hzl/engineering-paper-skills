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

REQUIRED_FULL_PAPER_CASES = {
    "full_paper_audit": {
        "fixture": "tests/fixtures/full_paper/robot_active_observation_flawed_manuscript.md",
        "annotation": "tests/fixtures/full_paper/gold_annotations/robot_active_observation_flawed_manuscript.json",
        "prompt": "tests/prompts/full_paper_audit.md",
        "expected": "tests/expected/full_paper_audit.yaml",
        "golden": "tests/outputs/golden/full_paper_audit.md",
        "min_words": 1500,
    },
    "full_paper_realistic_audit": {
        "fixture": "tests/fixtures/full_paper/robot_active_observation_realistic_8page.md",
        "annotation": "tests/fixtures/full_paper/gold_annotations/robot_active_observation_realistic_8page.json",
        "prompt": "tests/prompts/full_paper_realistic_audit.md",
        "expected": "tests/expected/full_paper_realistic_audit.yaml",
        "golden": "tests/outputs/golden/full_paper_realistic_audit.md",
        "min_words": 5000,
    },
}

REQUIRED_EVAL_RESULTS = {
    "evals/results/f3cbb28_full_paper_manual_eval.jsonl",
    "evals/results/f3cbb28_full_paper_model_eval.jsonl",
}

REQUIRED_MODEL_RUNS = {
    "tests/outputs/model_runs/full_paper_realistic_audit_f3cbb28.md",
}

REQUIRED_SENTENCE_AUDITS = {
    "tests/outputs/golden/full_paper_realistic_sentence_audit.md",
}

REQUIRED_RESPONSE_DIFF_ASSETS = {
    "fixture": "tests/fixtures/full_paper/response_old_new_diff.md",
    "annotation": "tests/fixtures/full_paper/gold_annotations/response_old_new_diff.json",
    "script": "scripts/check_response_diff.py",
}

REQUIRED_VENUE_PROFILES = {
    "skills/engineering-validation/venue_profiles/robotics_venues.json",
    "skills/engineering-validation/venue_profiles/ml_venues.json",
}

REQUIRED_REFERENCE_MARKERS = {
    "skills/_shared/story-spine.md": [
        "Complete Claim Inventory",
        "Contribution dependency map",
    ],
    "skills/engineering-paper-auditor/references/paragraph-to-paragraph-transition-audit.md": [
        "Terminology drift",
        "Claim-strength drift",
        "False evidence escalation",
    ],
    "skills/engineering-response/references/diff-verification.md": [
        "Semantic Match Check",
        "Semantic diff verification",
    ],
    "skills/engineering-polishing/references/anti-ai-prose.md": [
        "Unsafe stronger wording rejected",
        "claim-strength inflation",
    ],
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
            thresholds = data.get("thresholds")
            if not isinstance(thresholds, dict):
                errors.append("evals/top_tier_rubric.json missing thresholds object")
            else:
                for threshold in ("top_tier_candidate", "top_tier_ready"):
                    if threshold not in thresholds:
                        errors.append(f"evals/top_tier_rubric.json missing threshold: {threshold}")
            blocking_failure_types = data.get("blocking_failure_types")
            if not isinstance(blocking_failure_types, list) or len(blocking_failure_types) < 5:
                errors.append("evals/top_tier_rubric.json must define blocking_failure_types")

    if not rubric_md.exists():
        errors.append("Missing evals/manual-rubric.md")
    elif "Sentence necessity" not in rubric_md.read_text(encoding="utf-8"):
        errors.append("evals/manual-rubric.md missing Sentence necessity")

    for case, assets in REQUIRED_FULL_PAPER_CASES.items():
        for label, rel_path in assets.items():
            if label == "min_words":
                continue
            path = ROOT / str(rel_path)
            if not path.exists():
                errors.append(f"Missing {case} {label}: {rel_path}")

        full_fixture = ROOT / str(assets["fixture"])
        if full_fixture.exists():
            words = word_count(full_fixture)
            min_words = int(assets["min_words"])
            if words < min_words:
                errors.append(
                    f"{full_fixture.relative_to(ROOT)} has {words} words, expected at least {min_words}"
                )
            fixture_text = full_fixture.read_text(encoding="utf-8")
            for marker in (
                "Draft Abstract",
                "Draft Introduction",
                "Draft Methods",
                "Draft Experiments",
                "Draft Discussion",
                "Draft Conclusion",
                "Reviewer Comments",
            ):
                if marker not in fixture_text:
                    errors.append(f"{full_fixture.relative_to(ROOT)} missing marker: {marker}")
            for prompt_visible_answer in ("Expected audit pressure", "Failure modes"):
                if prompt_visible_answer in fixture_text:
                    errors.append(
                        f"{full_fixture.relative_to(ROOT)} exposes gold label: {prompt_visible_answer}"
                    )

        annotation = ROOT / str(assets["annotation"])
        if annotation.exists():
            try:
                annotation_data = json.loads(annotation.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"{annotation.relative_to(ROOT)} invalid JSON: {exc}")
            else:
                for key in ("fixture", "failure_modes"):
                    if key not in annotation_data:
                        errors.append(f"{annotation.relative_to(ROOT)} missing key: {key}")

        full_golden = ROOT / str(assets["golden"])
        if full_golden.exists():
            golden_text = full_golden.read_text(encoding="utf-8")
            for marker in (
                "Story spine",
                "Paragraph transition",
                "Section",
                "Sentence role",
                "Response",
                "Validation result",
            ):
                if marker not in golden_text:
                    errors.append(f"{full_golden.relative_to(ROOT)} missing marker: {marker}")

    for rel_path in REQUIRED_EVAL_RESULTS:
        eval_result = ROOT / rel_path
        if not eval_result.exists():
            errors.append(f"Missing eval result: {rel_path}")
            continue
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
            if rel_path.endswith("_model_eval.jsonl") and record.get("runtime_model_executed") is not True:
                errors.append(f"{eval_result.relative_to(ROOT)} line {line_no} must record runtime_model_executed=true")
            if rel_path.endswith("_model_eval.jsonl") and "model_output" not in record:
                errors.append(f"{eval_result.relative_to(ROOT)} line {line_no} missing key: model_output")
            if rel_path.endswith("_model_eval.jsonl") and "model_output" in record:
                model_output = ROOT / str(record["model_output"])
                if not model_output.exists():
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} points to missing model_output"
                    )

    for rel_path in REQUIRED_MODEL_RUNS:
        model_run = ROOT / rel_path
        if not model_run.exists():
            errors.append(f"Missing model run output: {rel_path}")
            continue
        text = model_run.read_text(encoding="utf-8")
        for marker in (
            "local model-run artifact, not a CI regression result",
            "Full-paper audit verdict",
            "Paragraph transition matrix",
            "Response diff verification",
            "CANNOT_MARK_READY",
        ):
            if marker not in text:
                errors.append(f"{model_run.relative_to(ROOT)} missing marker: {marker}")

    for rel_path in REQUIRED_SENTENCE_AUDITS:
        audit = ROOT / rel_path
        if not audit.exists():
            errors.append(f"Missing sentence audit artifact: {rel_path}")
            continue
        text = audit.read_text(encoding="utf-8")
        for marker in (
            "Abstract Sentence Audit",
            "Results Sentence Audit",
            "Conclusion Sentence Audit",
            "Response Sentence Audit",
            "Required Model Behavior",
        ):
            if marker not in text:
                errors.append(f"{audit.relative_to(ROOT)} missing marker: {marker}")

    for label, rel_path in REQUIRED_RESPONSE_DIFF_ASSETS.items():
        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"Missing response diff {label}: {rel_path}")

    for rel_path in REQUIRED_VENUE_PROFILES:
        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"Missing venue profile: {rel_path}")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid venue profile {rel_path}: {exc}")
            continue
        profiles = data.get("profiles")
        if not isinstance(profiles, dict) or not profiles:
            errors.append(f"Venue profile {rel_path} missing profiles object")
            continue
        for name, profile in profiles.items():
            if not isinstance(profile, dict):
                errors.append(f"Venue profile {rel_path}:{name} must be an object")
                continue
            if profile.get("official_policy_checked_required") is not True:
                errors.append(f"Venue profile {rel_path}:{name} must require official policy check")
            if not isinstance(profile.get("source_url"), str) or not profile["source_url"].startswith("https://"):
                errors.append(f"Venue profile {rel_path}:{name} must include https source_url")
            if not isinstance(profile.get("source_date"), str) or not profile["source_date"]:
                errors.append(f"Venue profile {rel_path}:{name} must include source_date")
            fields = profile.get("required_fields")
            if not isinstance(fields, list) or "source_url" not in fields or "source_date" not in fields:
                errors.append(f"Venue profile {rel_path}:{name} must require source_url and source_date")
            policy_checks = profile.get("policy_checks")
            if not isinstance(policy_checks, list) or len(policy_checks) < 3:
                errors.append(f"Venue profile {rel_path}:{name} must include at least three policy_checks")

    for rel_path, markers in REQUIRED_REFERENCE_MARKERS.items():
        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"Missing reference file: {rel_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(f"{rel_path} missing marker: {marker}")

    if errors:
        print("Quality asset check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Quality asset check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
