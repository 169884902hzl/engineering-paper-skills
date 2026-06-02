#!/usr/bin/env python3
"""Validate top-tier paper quality assets.

This check is intentionally static. It does not claim that the skills produce
top-tier output; it makes sure the repository contains the evaluation assets
needed to test story, sentence, AI-smell, and validation behavior.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_public_writing_demos import validate_public_writing_demos  # noqa: E402

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
    "full_paper_realistic_structured_audit": {
        "fixture": "tests/fixtures/full_paper/robot_active_observation_realistic_8page.md",
        "annotation": "tests/fixtures/full_paper/gold_annotations/robot_active_observation_realistic_8page.json",
        "prompt": "tests/prompts/full_paper_realistic_structured_audit.md",
        "expected": "tests/expected/full_paper_realistic_structured_audit.yaml",
        "golden": "tests/outputs/golden/full_paper_realistic_structured_audit.json",
        "min_words": 5000,
    },
    "ml_benchmark_flawed_manuscript": {
        "fixture": "tests/fixtures/full_paper/ml_benchmark_flawed_manuscript.md",
        "annotation": "tests/fixtures/full_paper/gold_annotations/ml_benchmark_flawed_manuscript.json",
        "prompt": "tests/prompts/full_paper_realistic_audit.md",
        "expected": "tests/expected/full_paper_realistic_audit.yaml",
        "golden": "tests/outputs/golden/full_paper_realistic_audit.md",
        "min_words": 500,
    },
    "systems_artifact_flawed_manuscript": {
        "fixture": "tests/fixtures/full_paper/systems_artifact_flawed_manuscript.md",
        "annotation": "tests/fixtures/full_paper/gold_annotations/systems_artifact_flawed_manuscript.json",
        "prompt": "tests/prompts/full_paper_realistic_audit.md",
        "expected": "tests/expected/full_paper_realistic_audit.yaml",
        "golden": "tests/outputs/golden/full_paper_realistic_audit.md",
        "min_words": 500,
    },
}

REQUIRED_EVAL_RESULTS = {
    "evals/results/2dc9571_hero_demo_model_eval.jsonl",
    "evals/results/681d305_demo_outputs_model_eval.jsonl",
    "evals/results/38b3d4d_full_paper_model_eval.jsonl",
    "evals/results/80d9c23_full_paper_model_eval.jsonl",
    "evals/results/6bec865_full_paper_model_eval.jsonl",
    "evals/results/8da3ceb_full_paper_model_eval.jsonl",
    "evals/results/f3cbb28_full_paper_manual_eval.jsonl",
    "evals/results/f3cbb28_full_paper_model_eval.jsonl",
    "evals/results/f383bb9_full_paper_model_eval.jsonl",
}

REQUIRED_MODEL_RUNS = {
    "tests/outputs/model_runs/full_paper_realistic_audit_8da3ceb.md": [
        "Target commit under review: 8da3ceb",
        "Runtime model executed: true",
        "CI-controlled behavior regression: no",
        "Full-paper audit verdict",
        "Response diff verification",
        "CANNOT_VALIDATE_AS_READY",
    ],
    "tests/outputs/model_runs/full_paper_realistic_audit_f3cbb28.md": [
        "local model-run artifact, not a CI regression result",
        "Full-paper audit verdict",
        "Paragraph transition matrix",
        "Response diff verification",
        "CANNOT_MARK_READY",
    ],
    "tests/outputs/model_runs/full_paper_realistic_audit_f383bb9.md": [
        "Runtime model executed: true",
        "CI-controlled behavior regression: no",
        "Full-paper audit verdict",
        "Paragraph transition matrix",
        "Response diff verification",
        "CANNOT_VALIDATE_AS_READY",
    ],
    "tests/outputs/model_runs/full_paper_realistic_structured_audit_6bec865_failed.json": [
        "BLOCKED_NOT_READY",
        "claim_evidence",
        "source_span",
        "response_truthfulness",
        "validation_status",
    ],
    "tests/outputs/model_runs/full_paper_realistic_structured_audit_80d9c23_failed.json": [
        "PASS_WITH_BLOCKERS",
        "claim_evidence",
        "source_span",
        "response_truthfulness",
        "validation_status",
    ],
    "tests/outputs/model_runs/full_paper_realistic_structured_audit_38b3d4d_pass.json": [
        "CANNOT_MARK_READY",
        "claim_evidence",
        "SUPPORTED_BOUNDED",
        "response_truthfulness",
        "validation_status",
        "official_venue_policy",
        "NOT_RUN",
    ],
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

REQUIRED_DISCOVERY_ASSETS = {
    ".github/workflows/behavior-regression.yml": [
        "--require-command",
        "actions/upload-artifact@v4",
        "behavior-regression-output",
    ],
    ".github/workflows/qa.yml": [
        "check_venue_profiles.py",
        "optional-behavior-regression-output",
        "if-no-files-found: ignore",
    ],
    "scripts/check_venue_profiles.py": [
        "Validate venue profile JSON files",
        "--refresh",
        "official source URLs",
        "STATIC_SUMMARY_NOT_LIVE_CHECK",
    ],
    "scripts/write_behavior_eval_stub.py": [
        "behavior-regression eval stub",
        "ci_single_run",
        "output_sha256",
    ],
    "docs/index.html": [
        "Engineering Paper Skills",
        "manuscript audit",
        "Start With Rough Notes",
        "Recorded local output excerpt",
        "Normal users only need",
        "Example Outputs",
        "SoftwareSourceCode",
    ],
    "docs/demo.html": [
        "Demo Gallery",
        "Example Provenance",
        "Illustrative examples",
        "Recorded local Codex outputs",
        "Recorded Demo Outputs",
        "Manuscript Writing Examples",
        "Safety And Audit Examples",
        "Notes To Manuscript Paragraph",
        "Related Work Positioning",
        "Methods Execution Path",
        "Conservative Claim Audit",
        "Reviewer Response Truthfulness",
        "Deep Audit Artifacts",
        "Structured JSON Audit",
        "Response Diff Verification",
        "Inline Audit Snippets",
        "Mini Walkthrough",
        "source_span",
        "remaining_gap",
    ],
    "docs/quality-gates.html": [
        "Quality Gates",
        "Behavior Evidence",
        "Evidence Boundary",
    ],
    "docs/robots.txt": [
        "Sitemap: https://169884902hzl.github.io/engineering-paper-skills/sitemap.xml",
    ],
    "docs/sitemap.xml": [
        "https://169884902hzl.github.io/engineering-paper-skills/",
    ],
    "docs/quality-gates.md": [
        "does not require GitHub releases",
        "Behavior Evidence",
        "Evidence Boundary",
    ],
    "docs/contract-failure-analysis.md": [
        "What The Model Got Right",
        "What The Strict Contract Rejected",
        "Evaluation Design Diagnosis",
        "Current Contract Direction",
    ],
    "docs/discovery.md": [
        "Discovery Checklist",
        "Google Search Console",
        "Do not claim",
    ],
    "docs/discovery.html": [
        "Discovery Checklist",
        "Search Console",
        "Safe Launch Wording",
    ],
    "CITATION.cff": [
        "Engineering Paper Skills",
        "commit-based-beta",
    ],
    "codemeta.json": [
        "Engineering Paper Skills",
        "research paper validation",
    ],
    "CHANGELOG.md": [
        "No-release beta changelog",
        "Replace first-screen safety examples with writing demo",
        "38b3d4d",
        "80d9c23",
        "6bec865",
        "d03d683",
        "8da3ceb",
    ],
    "KNOWN_GOOD.md": [
        "Commit anchors",
        "Behavior evidence",
        "Demo output provenance",
        "hero notes-to-manuscript paragraph demo",
        "Known limitations",
    ],
    "scripts/check_metadata_files.py": [
        "Validate repository metadata",
        "commit-based-beta",
        "urlset",
    ],
    "skills/engineering-paper-coach/SKILL.md": [
        "Engineering Paper Coach",
        "Evidence Boundary",
        "Claim Strength",
        "Output Requirements",
        "CANNOT_DETERMINE",
    ],
    "skills/engineering-paper-coach/agents/openai.yaml": [
        "Engineering Paper Coach",
        "conservative engineering paper",
    ],
    "tests/prompts/simple_engineering_paper.md": [
        "engineering-paper-coach",
        "deployment-ready",
        "proven robust",
    ],
    "tests/expected/simple_engineering_paper.yaml": [
        "simple_engineering_paper",
        "Evidence Boundary",
        "Safe Rewrite",
        "NOT_READY",
    ],
    "tests/outputs/golden/simple_engineering_paper.md": [
        "NOT_READY",
        "Evidence Boundary",
        "Safe Rewrite",
        "one tabletop fixture",
    ],
    "tests/prompts/full_paper_realistic_schema_contract.md": [
        "claim_evidence",
        "response_truthfulness",
        "validation_status",
    ],
    "tests/expected/full_paper_realistic_schema_contract.yaml": [
        "full_paper_realistic_schema_contract",
        "json_expectations",
        "span_origin_checks",
    ],
    "tests/outputs/golden/full_paper_realistic_schema_contract.json": [
        "claim_evidence",
        "response_truthfulness",
        "validation_status",
    ],
}

REQUIRED_DEMO_CASES = {
    "demo_claim_audit": {
        "prompt": "tests/prompts/demo_claim_audit.md",
        "output": "tests/outputs/model_runs/demo/demo_claim_audit_681d305.md",
        "skill": "engineering-paper-coach",
        "markers": ["Claim-strength audit", "Safe rewrite", "What stronger claims would require"],
    },
    "demo_notes_to_manuscript_paragraph": {
        "prompt": "tests/prompts/demo_notes_to_manuscript_paragraph.md",
        "output": "tests/outputs/model_runs/demo/demo_notes_to_manuscript_paragraph_2dc9571.md",
        "skill": "engineering-writing",
        "markers": [
            "Manuscript paragraph",
            "Why this is evidence-bound",
            "Claims not supported by the supplied notes",
        ],
    },
    "demo_results_paragraph": {
        "prompt": "tests/prompts/demo_results_paragraph.md",
        "output": "tests/outputs/model_runs/demo/demo_results_paragraph_681d305.md",
        "skill": "engineering-writing",
        "markers": ["Experiment question", "Manuscript paragraph", "Claim-evidence note"],
    },
    "demo_polishing_claim_inflation": {
        "prompt": "tests/prompts/demo_polishing_claim_inflation.md",
        "output": "tests/outputs/model_runs/demo/demo_polishing_claim_inflation_681d305.md",
        "skill": "engineering-polishing",
        "markers": ["Claim-strength diff", "Polished paragraph", "Remaining evidence needed"],
    },
    "demo_figure_source_data_consistency": {
        "prompt": "tests/prompts/demo_figure_source_data_consistency.md",
        "output": "tests/outputs/model_runs/demo/demo_figure_source_data_consistency_681d305.md",
        "skill": "engineering-figure-table",
        "markers": ["Panel/table responsibility map", "Safe caption", "Source-data checks required"],
    },
    "demo_response_truthfulness": {
        "prompt": "tests/prompts/demo_response_truthfulness.md",
        "output": "tests/outputs/model_runs/demo/demo_response_truthfulness_681d305.md",
        "skill": "engineering-response",
        "markers": ["Comment-response tracker", "Prohibited final-response claims", "Verification needed"],
    },
    "demo_validation_readiness": {
        "prompt": "tests/prompts/demo_validation_readiness.md",
        "output": "tests/outputs/model_runs/demo/demo_validation_readiness_681d305.md",
        "skill": "engineering-validation",
        "markers": ["Overall readiness: NOT_READY", "Check table", "Required next actions"],
    },
    "demo_related_work_nearest_neighbor": {
        "prompt": "tests/prompts/demo_related_work_nearest_neighbor.md",
        "output": "tests/outputs/model_runs/demo/demo_related_work_nearest_neighbor_681d305.md",
        "skill": "engineering-writing",
        "markers": ["Technical axes table", "Nearest-neighbor distinction", "Citation/evidence still needed"],
    },
    "demo_methods_execution_path": {
        "prompt": "tests/prompts/demo_methods_execution_path.md",
        "output": "tests/outputs/model_runs/demo/demo_methods_execution_path_681d305.md",
        "skill": "engineering-writing",
        "markers": ["Execution-Path Paragraph Scaffold", "Placeholders That Must Not Be Invented", "Safe Methods Paragraph"],
    },
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
    validate_public_writing_demos(errors)

    for rel_path in ("README.md", "docs/index.html", "docs/demo.html"):
        path = ROOT / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for forbidden in ("**Output**", "<pre><code>Output:"):
            if forbidden in text:
                errors.append(
                    f"{rel_path} uses unqualified output label; use illustrative or recorded provenance"
                )

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
            if full_golden.suffix == ".json":
                try:
                    golden_data = json.loads(golden_text)
                except json.JSONDecodeError as exc:
                    errors.append(f"{full_golden.relative_to(ROOT)} invalid JSON: {exc}")
                else:
                    for marker in (
                        "claim_evidence",
                        "paragraph_transitions",
                        "section_dependencies",
                        "response_truthfulness",
                        "validation_status",
                    ):
                        if marker not in golden_data:
                            errors.append(f"{full_golden.relative_to(ROOT)} missing key: {marker}")
            else:
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
                "evidence_level",
                "score_interpretation",
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
            if rel_path.endswith("_model_eval.jsonl") and record.get("evidence_level") not in {
                "local_single_run",
                "local_single_run_failed",
            }:
                errors.append(
                    f"{eval_result.relative_to(ROOT)} line {line_no} must record local single-run evidence_level"
                )
            if not rel_path.endswith("_model_eval.jsonl") and record.get("evidence_level") != "repository_gold_review":
                errors.append(f"{eval_result.relative_to(ROOT)} line {line_no} must record evidence_level=repository_gold_review")
            if rel_path.endswith("_model_eval.jsonl") and "model_output" not in record:
                errors.append(f"{eval_result.relative_to(ROOT)} line {line_no} missing key: model_output")
            if rel_path.endswith("_model_eval.jsonl") and "model_output" in record:
                model_output = ROOT / str(record["model_output"])
                if not model_output.exists():
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} points to missing model_output"
                    )
            if rel_path.endswith("_model_eval.jsonl") and not isinstance(
                record.get("blocking_failures"), list
            ):
                errors.append(f"{eval_result.relative_to(ROOT)} line {line_no} missing list: blocking_failures")
            if "f383bb9" in rel_path:
                if record.get("commit") != "f383bb9":
                    errors.append(f"{eval_result.relative_to(ROOT)} line {line_no} must record commit=f383bb9")
                if record.get("ci_controlled") is not False:
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must explicitly record ci_controlled=false"
                    )
                if not isinstance(record.get("residual_limitations"), list) or not record["residual_limitations"]:
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must record residual_limitations"
                    )
            if "8da3ceb" in rel_path:
                if record.get("commit") != "8da3ceb":
                    errors.append(f"{eval_result.relative_to(ROOT)} line {line_no} must record commit=8da3ceb")
                if record.get("ci_controlled") is not False:
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must explicitly record ci_controlled=false"
                    )
                if not isinstance(record.get("residual_limitations"), list) or not record["residual_limitations"]:
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must record residual_limitations"
                    )
            if "6bec865" in rel_path:
                if record.get("commit") != "6bec865":
                    errors.append(f"{eval_result.relative_to(ROOT)} line {line_no} must record commit=6bec865")
                if record.get("ci_controlled") is not False:
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must explicitly record ci_controlled=false"
                    )
                if record.get("evidence_level") != "local_single_run_failed":
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must record failed local evidence"
                    )
                if not isinstance(record.get("blocking_failures"), list) or not record["blocking_failures"]:
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must record blocking_failures"
                    )
            if "80d9c23" in rel_path:
                if record.get("commit") != "80d9c23":
                    errors.append(f"{eval_result.relative_to(ROOT)} line {line_no} must record commit=80d9c23")
                if record.get("ci_controlled") is not False:
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must explicitly record ci_controlled=false"
                    )
                if record.get("evidence_level") != "local_single_run_failed":
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must record failed local evidence"
                    )
                if "output_sha256" not in record:
                    errors.append(f"{eval_result.relative_to(ROOT)} line {line_no} missing key: output_sha256")
                if not isinstance(record.get("blocking_failures"), list) or not record["blocking_failures"]:
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must record blocking_failures"
                    )
            if "38b3d4d" in rel_path:
                if record.get("commit") != "38b3d4d72660fbfe5705103e6bc27addac14668e":
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must record full commit=38b3d4d..."
                    )
                if record.get("ci_controlled") is not False:
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must explicitly record ci_controlled=false"
                    )
                if record.get("evidence_level") != "local_single_run":
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must record local_single_run evidence"
                    )
                if "output_sha256" not in record:
                    errors.append(f"{eval_result.relative_to(ROOT)} line {line_no} missing key: output_sha256")
                if record.get("output_sha256") != "41ca34d9c363ba2cd3cc308c4c5dba83430cbca33789616b7210de4db9d46f0f":
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} records unexpected output_sha256"
                    )
                if record.get("blocking_failures") != []:
                    errors.append(
                        f"{eval_result.relative_to(ROOT)} line {line_no} must record no blocking failures"
                    )

    for rel_path, markers in REQUIRED_MODEL_RUNS.items():
        model_run = ROOT / rel_path
        if not model_run.exists():
            errors.append(f"Missing model run output: {rel_path}")
            continue
        text = model_run.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(f"{model_run.relative_to(ROOT)} missing marker: {marker}")

    demo_manifest = ROOT / "tests/outputs/model_runs/demo/manifest.json"
    if not demo_manifest.exists():
        errors.append("Missing recorded demo manifest: tests/outputs/model_runs/demo/manifest.json")
    else:
        try:
            manifest = json.loads(demo_manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{demo_manifest.relative_to(ROOT)} invalid JSON: {exc}")
            manifest = {}
        if manifest:
            if manifest.get("manifest_type") != "recorded_local_demo_outputs":
                errors.append(f"{demo_manifest.relative_to(ROOT)} must record manifest_type=recorded_local_demo_outputs")
            if manifest.get("runtime_model_executed") is not True:
                errors.append(f"{demo_manifest.relative_to(ROOT)} must record runtime_model_executed=true")
            if manifest.get("ci_controlled") is not False:
                errors.append(f"{demo_manifest.relative_to(ROOT)} must record ci_controlled=false")
            if manifest.get("evidence_level") != "local_single_run":
                errors.append(f"{demo_manifest.relative_to(ROOT)} must record evidence_level=local_single_run")
            outputs = manifest.get("outputs")
            if not isinstance(outputs, list):
                errors.append(f"{demo_manifest.relative_to(ROOT)} missing outputs list")
                outputs = []
            manifest_by_case = {
                item.get("case"): item
                for item in outputs
                if isinstance(item, dict) and isinstance(item.get("case"), str)
            }
            for case, assets in REQUIRED_DEMO_CASES.items():
                entry = manifest_by_case.get(case)
                if not entry:
                    errors.append(f"{demo_manifest.relative_to(ROOT)} missing demo case: {case}")
                    continue
                for key in ("prompt", "output", "sha256", "skill"):
                    if not isinstance(entry.get(key), str) or not entry[key]:
                        errors.append(f"{demo_manifest.relative_to(ROOT)} case {case} missing {key}")
                if entry.get("skill") != assets["skill"]:
                    errors.append(f"{demo_manifest.relative_to(ROOT)} case {case} records unexpected skill")
                if entry.get("prompt") != assets["prompt"]:
                    errors.append(f"{demo_manifest.relative_to(ROOT)} case {case} records unexpected prompt path")
                if entry.get("output") != assets["output"]:
                    errors.append(f"{demo_manifest.relative_to(ROOT)} case {case} records unexpected output path")
                output_path = ROOT / str(entry.get("output", ""))
                if output_path.exists() and isinstance(entry.get("sha256"), str):
                    actual = hashlib.sha256(output_path.read_bytes()).hexdigest()
                    if actual != entry["sha256"]:
                        errors.append(f"{output_path.relative_to(ROOT)} sha256 does not match manifest")

    for case, assets in REQUIRED_DEMO_CASES.items():
        for label in ("prompt", "output"):
            path = ROOT / assets[label]
            if not path.exists():
                errors.append(f"Missing recorded demo {label} for {case}: {assets[label]}")
                continue
            text = path.read_text(encoding="utf-8")
            if label == "prompt" and assets["skill"] not in text:
                errors.append(f"{path.relative_to(ROOT)} missing skill marker: {assets['skill']}")
            if label == "output":
                for marker in assets["markers"]:
                    if marker not in text:
                        errors.append(f"{path.relative_to(ROOT)} missing marker: {marker}")

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
            if profile.get("profile_status") != "STATIC_SUMMARY_NOT_LIVE_CHECK":
                errors.append(
                    f"Venue profile {rel_path}:{name} must mark profile_status=STATIC_SUMMARY_NOT_LIVE_CHECK"
                )
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
            snapshot = profile.get("policy_snapshot")
            if not isinstance(snapshot, dict):
                errors.append(f"Venue profile {rel_path}:{name} must include policy_snapshot")
                continue
            for key in ("last_checked", "verification_method", "policy_excerpt_hash", "hash_basis"):
                if not isinstance(snapshot.get(key), str) or not snapshot[key]:
                    errors.append(f"Venue profile {rel_path}:{name} policy_snapshot missing {key}")
            if "not live policy extraction" not in str(snapshot.get("verification_method", "")):
                errors.append(f"Venue profile {rel_path}:{name} policy_snapshot must disclose non-live extraction")

    for rel_path, markers in REQUIRED_REFERENCE_MARKERS.items():
        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"Missing reference file: {rel_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(f"{rel_path} missing marker: {marker}")

    for rel_path, markers in REQUIRED_DISCOVERY_ASSETS.items():
        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"Missing discovery or quality asset: {rel_path}")
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
