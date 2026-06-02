#!/usr/bin/env python3
"""Check public writing demo surfaces for showcase blockers.

The public writing examples are local model-run artifacts, not only static
strings in README or Pages. This script therefore checks both the public
snippets and the linked output files against their prompt sources.
"""

from __future__ import annotations

import re
import sys
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PUBLIC_SURFACES = (
    "README.md",
    "docs/index.html",
    "docs/demo.html",
)

EVIDENCE_ARCHIVE_MARKERS = (
    "Evidence Archive",
    "Previous Behavior Evidence",
)

PUBLIC_REJECTED_OR_ARCHIVE_ONLY_OUTPUTS = {
    "tests/outputs/model_runs/writing/coach_write_draft_first_ce1478f.md",
    "tests/outputs/model_runs/writing/writing_ablation_interpretation_ce1478f.md",
    "tests/outputs/model_runs/writing/writing_results_interpretation_ce1478f.md",
    "tests/outputs/model_runs/writing/writing_methods_reader_path_ce1478f.md",
    "tests/outputs/model_runs/writing/writing_conclusion_two_paragraph_ce1478f.md",
    "tests/outputs/model_runs/writing/writing_min_ce1478f.md",
    "tests/outputs/model_runs/writing/writing_abstract_showcase_v2_ad6d5b4.md",
    "tests/outputs/model_runs/writing/writing_related_work_showcase_v2_ad6d5b4.md",
    "tests/outputs/model_runs/writing/writing_zh_to_en_showcase_v2_ad6d5b4.md",
    "tests/outputs/model_runs/writing/writing_conclusion_showcase_v2_ad6d5b4.md",
    "tests/outputs/model_runs/writing/writing_conclusion_showcase_v2_rerun_e99ca81.md",
    "tests/outputs/model_runs/writing/full_section_results_demo_e99ca81.md",
}

PHYSICAL_MECHANISM_TERMS = (
    "lateral jamming",
    "physical failure statistics",
    "jamming",
    "slip",
    "compliance",
    "deformation",
    "fatigue",
    "binding",
    "impact",
    "resonance",
    "collision",
    "vibration",
    "backlash",
    "wear",
    "fracture",
    "buckling",
    "instability",
    "drift",
)

PROMPT_META_LANGUAGE_TERMS = (
    "supplied notes",
    "supplied positioning",
    "supplied failure modes",
    "available evidence",
    "dominant failure source",
    "without claiming",
    "unsupported",
    "not verified",
    "pending verification",
    "pending verified citations",
    "Evidence Needed",
    "Unsupported / not verified",
)

PUBLIC_REGISTER_TERMS = (
    "These results support",
    "They do not establish",
    "without claiming",
    "not verified",
    "Evidence Needed",
    "Unsupported",
    "supplied notes",
    "available evidence",
    "pending verification",
    "This output",
    "The supplied prompt",
    "The current evidence",
)

PHYSICAL_MECHANISM_PATTERNS = {
    term: re.compile(rf"(?<![A-Za-z0-9]){re.escape(term).replace(r'\ ', r'\s+')}(?![A-Za-z0-9])", re.IGNORECASE)
    for term in PHYSICAL_MECHANISM_TERMS
}

PUBLIC_OUTPUT_BLOCKERS = {
    term: re.compile(rf"(?<![A-Za-z0-9]){re.escape(term).replace(r'\ ', r'\s+')}(?![A-Za-z0-9])", re.IGNORECASE)
    for term in PROMPT_META_LANGUAGE_TERMS
}

PUBLIC_REGISTER_BLOCKERS = {
    term: re.compile(rf"(?<![A-Za-z0-9]){re.escape(term).replace(r'\ ', r'\s+')}(?![A-Za-z0-9])", re.IGNORECASE)
    for term in PUBLIC_REGISTER_TERMS
}

RELATED_WORK_BLOCKERS = {
    "supplied notes",
    "supplied positioning",
    "available evidence",
    "without claiming",
    "Unsupported / not verified",
    "pending verified citations",
}

CONCLUSION_INVENTORY_STARTS = (
    "the operating scope",
    "the demonstrated operating envelope",
    "the study is limited to",
    "the current evaluation",
)

PROMPT_CONTROL_HEADINGS = (
    "forbidden",
    "do-not-claim",
    "do not claim",
    "requirements",
    "style requirements",
    "output requirements",
    "writing requirements",
)

PROMPT_HEADING_RE = re.compile(r"^[A-Za-z][A-Za-z0-9 /(),'-]+:\s*$")

EXACT_RECORDED_LABELS = (
    "Exact recorded excerpt",
    "Recorded excerpt",
    "recorded output excerpt",
    "Recorded output excerpt",
    "recorded local output excerpt",
    "Recorded local output excerpt",
)

EXCERPT_LABEL_RE = re.compile(
    r"(?:Exact recorded excerpt|Recorded excerpt|Recorded output excerpt|recorded output excerpt|"
    r"Recorded local output excerpt|recorded local output excerpt|"
    r"Short excerpt from recorded output|Excerpted for readability)\s*:",
    re.IGNORECASE,
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def public_region(text: str) -> str:
    cutoff = len(text)
    for marker in EVIDENCE_ARCHIVE_MARKERS:
        index = text.find(marker)
        if index != -1:
            cutoff = min(cutoff, index)
    return text[:cutoff]


def writing_output_links(text: str) -> set[str]:
    links: set[str] = set()
    pattern = re.compile(r"tests/outputs/model_runs/writing/[^\"')<>\s]+\.md")
    for match in pattern.finditer(text):
        links.add(match.group(0))
    github_pattern = re.compile(
        r"github\.com/169884902hzl/engineering-paper-skills/blob/main/"
        r"(tests/outputs/model_runs/writing/[^\"')<>\s]+\.md)"
    )
    for match in github_pattern.finditer(text):
        links.add(match.group(1))
    return links


def prompt_for_output(output_rel: str) -> Path | None:
    name = Path(output_rel).name
    pairs = (
        ("writing_conclusion_showcase_v2_rerun2", "writing_conclusion_showcase_v2_rerun2.md"),
        ("writing_abstract_showcase_v2_rerun", "writing_abstract_showcase_v2_rerun.md"),
        ("writing_abstract_showcase_v2_", "writing_abstract_showcase_v2.md"),
        ("writing_related_work_showcase_v2_rerun", "writing_related_work_showcase_v2_rerun.md"),
        ("writing_related_work_showcase_v2_", "writing_related_work_showcase_v2.md"),
        ("writing_zh_to_en_showcase_v2_rerun", "writing_zh_to_en_showcase_v2_rerun.md"),
        ("writing_zh_to_en_showcase_v2_", "writing_zh_to_en_showcase_v2.md"),
        ("writing_conclusion_showcase_v2_rerun", "writing_conclusion_showcase_v2_rerun.md"),
        ("writing_conclusion_showcase_v2_", "writing_conclusion_showcase_v2.md"),
        ("writing_methods_showcase_v2_", "writing_methods_showcase_v2.md"),
        ("writing_results_showcase_v2_", "writing_results_showcase_v2.md"),
        ("writing_ablation_showcase_v2_", "writing_ablation_showcase_v2.md"),
        ("full_section_results_demo_v2_", "full_section_results_demo_v2.md"),
        ("full_section_results_demo_", "full_section_results_demo.md"),
        ("full_section_methods_demo_", "full_section_methods_demo.md"),
        ("rough_user_intro_minimal_", "rough_user_intro_minimal.md"),
        ("rough_user_results_minimal_", "rough_user_results_minimal.md"),
        ("rough_user_methods_minimal_", "rough_user_methods_minimal.md"),
        ("rough_user_zh_notes_minimal_", "rough_user_zh_notes_minimal.md"),
        ("rough_user_related_work_minimal_", "rough_user_related_work_minimal.md"),
        ("stability_rough_results_run", "rough_user_results_minimal.md"),
        ("stability_rough_zh_run", "rough_user_zh_notes_minimal.md"),
        ("stability_benchmark_robotics_run", "benchmark_robotics_system_results.md"),
        ("stability_benchmark_ml_systems_run", "benchmark_ml_systems_methods.md"),
        ("benchmark_robotics_system_results_", "benchmark_robotics_system_results.md"),
        ("benchmark_ml_systems_methods_", "benchmark_ml_systems_methods.md"),
        ("benchmark_control_experiment_discussion_", "benchmark_control_experiment_discussion.md"),
        ("related_work_verified_citation_mode_", "related_work_verified_citation_mode.md"),
        (
            "realistic_robotics_manuscript_notes_results_",
            "realistic_robotics_manuscript_notes_results.md",
        ),
        (
            "realistic_ml_systems_manuscript_notes_methods_",
            "realistic_ml_systems_manuscript_notes_methods.md",
        ),
        ("zh_notes_to_methods_showcase_", "zh_notes_to_methods_showcase.md"),
        ("zh_notes_to_discussion_showcase_", "zh_notes_to_discussion_showcase.md"),
        ("messy_notes_intro_", "messy_notes_intro.md"),
        ("messy_table_to_results_", "messy_table_to_results.md"),
        ("incomplete_related_work_notes_", "incomplete_related_work_notes.md"),
        ("mixed_zh_en_notes_to_methods_", "mixed_zh_en_notes_to_methods.md"),
        ("contradictory_boundary_notes_", "contradictory_boundary_notes.md"),
    )
    for prefix, prompt_name in pairs:
        if name.startswith(prefix):
            return ROOT / "tests/prompts" / prompt_name
    return None


def prompt_source_and_control(prompt: Path) -> tuple[str, str]:
    source_lines: list[str] = []
    control_lines: list[str] = []
    in_control = False

    for line in read(prompt).splitlines():
        stripped = line.strip()
        lower = stripped.lower().rstrip(":")
        if PROMPT_HEADING_RE.match(stripped):
            in_control = lower.startswith(PROMPT_CONTROL_HEADINGS)
        if in_control:
            control_lines.append(line)
        else:
            source_lines.append(line)

    return "\n".join(source_lines), "\n".join(control_lines)


def manuscript_region(text: str) -> str:
    cutoff = len(text)
    for marker in (
        "## Evidence boundary",
        "## Why this works",
        "## Do-not-claim",
        "Evidence boundary:",
        "Do-not-claim:",
    ):
        index = text.find(marker)
        if index != -1:
            cutoff = min(cutoff, index)
    return text[:cutoff]


def html_to_text(text: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    return unescape(text)


def manuscript_paragraphs(text: str) -> list[str]:
    body = manuscript_region(text)
    paragraphs = []
    for raw in re.split(r"\n\s*\n", body):
        paragraph = raw.strip()
        if not paragraph or paragraph.startswith("#"):
            continue
        paragraphs.append(paragraph)
    return paragraphs


def is_evidence_only_near(text: str, start: int) -> bool:
    window = text[max(0, start - 250) : min(len(text), start + 250)]
    return "evidence-only" in window.lower()


def validate_surface_register(rel_path: str, region: str, errors: list[str]) -> None:
    for label, pattern in PUBLIC_OUTPUT_BLOCKERS.items():
        for match in pattern.finditer(region):
            if not is_evidence_only_near(region, match.start()):
                errors.append(f"{rel_path} public display contains blocker wording: {label}")

    for label, pattern in PUBLIC_REGISTER_BLOCKERS.items():
        for match in pattern.finditer(region):
            if not is_evidence_only_near(region, match.start()):
                errors.append(f"{rel_path} public draft excerpt contains non-manuscript register: {label}")


def code_blocks(region: str) -> list[str]:
    blocks: list[str] = []
    for match in re.finditer(r"```(?:[A-Za-z0-9_-]+)?\n(.*?)```", region, flags=re.DOTALL):
        blocks.append(match.group(1))
    for match in re.finditer(r"<pre><code>(.*?)</code></pre>", region, flags=re.DOTALL | re.IGNORECASE):
        blocks.append(html_to_text(match.group(1)))
    return blocks


def public_excerpt_text(region: str) -> str:
    excerpts: list[str] = []
    for block in code_blocks(region):
        for match in EXCERPT_LABEL_RE.finditer(block):
            excerpt = block[match.end() :].strip()
            if excerpt:
                excerpts.append(excerpt)
    return "\n\n".join(excerpts)


def validate_mechanism_sources(output_rel: str, text: str, prompt: Path | None, errors: list[str]) -> None:
    manuscript = manuscript_region(text)
    found_terms = [
        term for term, pattern in PHYSICAL_MECHANISM_PATTERNS.items() if pattern.search(manuscript)
    ]
    if not found_terms:
        return

    if prompt is None:
        for term in found_terms:
            errors.append(
                f"{output_rel} term={term} prompt=<missing> failure=missing prompt mapping for mechanism check"
            )
        return

    if not prompt.exists():
        for term in found_terms:
            errors.append(
                f"{output_rel} term={term} prompt={rel(prompt)} failure=prompt file missing"
            )
        return

    source_body, control_body = prompt_source_and_control(prompt)
    for term in found_terms:
        in_source = bool(PHYSICAL_MECHANISM_PATTERNS[term].search(source_body))
        in_control = bool(PHYSICAL_MECHANISM_PATTERNS[term].search(control_body))
        if in_source:
            continue
        if in_control:
            reason = "term appears only in prompt forbidden/requirements body"
        else:
            reason = "term not supplied in prompt source body"
        errors.append(f"{output_rel} term={term} prompt={rel(prompt)} failure={reason}")


def validate_exact_recorded_excerpts(rel_path: str, region: str, errors: list[str]) -> None:
    label_pattern = re.compile("|".join(re.escape(label) for label in EXACT_RECORDED_LABELS))
    for match in label_pattern.finditer(region):
        following = region[match.end() : match.end() + 2000]
        output_links = sorted(writing_output_links(following))
        if not output_links:
            errors.append(f"{rel_path} exact recorded excerpt label has no following writing artifact link")
            continue

        end_match = re.search(r"(```|</code>|</pre>)", following)
        snippet_region = following[: end_match.start()] if end_match else following
        snippet = html_to_text(snippet_region)
        snippet = snippet.lstrip(":\n ").strip()
        if not snippet:
            errors.append(f"{rel_path} exact recorded excerpt label has an empty excerpt")
            continue

        output_rel = output_links[0]
        output_path = ROOT / output_rel
        if not output_path.exists():
            errors.append(f"{rel_path} exact recorded excerpt points to missing artifact: {output_rel}")
            continue
        artifact = read(output_path)
        if snippet not in artifact:
            errors.append(
                f"{rel_path} exact recorded excerpt not found in artifact: label={match.group(0)} "
                f"artifact={output_rel}"
            )


def validate_three_paragraph_public_output(output_rel: str, text: str, errors: list[str]) -> None:
    if not (
        "full_section_results_demo_v2_" in output_rel
        or "full_section_methods_demo_" in output_rel
    ):
        return
    paragraphs = manuscript_paragraphs(text)
    if len(paragraphs) != 3:
        errors.append(f"{output_rel} must have exactly three manuscript paragraphs; found {len(paragraphs)}")


def validate_public_writing_demos(errors: list[str]) -> None:
    public_links: set[str] = set()

    for rel_path in PUBLIC_SURFACES:
        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"Missing public surface: {rel_path}")
            continue
        region = public_region(read(path))
        validate_surface_register(rel_path, public_excerpt_text(region), errors)
        validate_exact_recorded_excerpts(rel_path, region, errors)
        links = writing_output_links(region)
        public_links.update(links)
        for output in sorted(PUBLIC_REJECTED_OR_ARCHIVE_ONLY_OUTPUTS & links):
            errors.append(f"{rel_path} public display links archive-only output: {output}")

    for output_rel in sorted(public_links):
        output_path = ROOT / output_rel
        if not output_path.exists():
            errors.append(f"Public writing demo link points to missing output: {output_rel}")
            continue
        text = read(output_path)
        prompt = prompt_for_output(output_rel)

        for label, pattern in PUBLIC_OUTPUT_BLOCKERS.items():
            if pattern.search(manuscript_region(text)):
                errors.append(f"{output_rel} contains public-demo blocker: {label}")

        validate_mechanism_sources(output_rel, text, prompt, errors)
        validate_three_paragraph_public_output(output_rel, text, errors)

        if "related_work" in output_rel:
            for label in RELATED_WORK_BLOCKERS:
                pattern = PUBLIC_OUTPUT_BLOCKERS[label]
                if pattern.search(manuscript_region(text)):
                    errors.append(f"{output_rel} contains Related Work meta-language: {label}")

        if "conclusion" in output_rel:
            paragraphs = manuscript_paragraphs(text)
            if len(paragraphs) >= 2:
                second = paragraphs[1].lower()
                for start in CONCLUSION_INVENTORY_STARTS:
                    if second.startswith(start):
                        errors.append(f"{output_rel} Conclusion paragraph 2 starts as inventory")


def main() -> int:
    errors: list[str] = []
    validate_public_writing_demos(errors)
    if errors:
        print("Public writing demo check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Public writing demo check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
