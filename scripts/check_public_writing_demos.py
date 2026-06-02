#!/usr/bin/env python3
"""Check public writing demo surfaces for showcase blockers."""

from __future__ import annotations

import re
import sys
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
    "tests/outputs/model_runs/writing/writing_abstract_showcase_v2_ad6d5b4.md",
    "tests/outputs/model_runs/writing/writing_related_work_showcase_v2_ad6d5b4.md",
    "tests/outputs/model_runs/writing/writing_zh_to_en_showcase_v2_ad6d5b4.md",
    "tests/outputs/model_runs/writing/writing_conclusion_showcase_v2_ad6d5b4.md",
}

PUBLIC_OUTPUT_BLOCKERS = {
    "lateral jamming": re.compile(r"\blateral\s+jamming\b", re.IGNORECASE),
    "supplied notes": re.compile(r"\bsupplied\s+notes\b", re.IGNORECASE),
    "supplied positioning": re.compile(r"\bsupplied\s+positioning\b", re.IGNORECASE),
    "available evidence": re.compile(r"\bavailable\s+evidence\b", re.IGNORECASE),
    "without claiming": re.compile(r"\bwithout\s+claiming\b", re.IGNORECASE),
    "Unsupported / not verified": re.compile(r"Unsupported\s*/\s*not\s+verified", re.IGNORECASE),
    "pending verified citations": re.compile(r"\bpending\s+verified\s+citations\b", re.IGNORECASE),
    "dominant failure source": re.compile(r"\bdominant\s+failure\s+source\b", re.IGNORECASE),
    "supplied failure modes": re.compile(r"\bsupplied\s+failure\s+modes\b", re.IGNORECASE),
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
    "the study is limited to",
    "the current evaluation",
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
        ("full_section_results_demo_", "full_section_results_demo.md"),
    )
    for prefix, prompt_name in pairs:
        if name.startswith(prefix):
            return ROOT / "tests/prompts" / prompt_name
    return None


def prompt_supplies_jamming(prompt: Path | None) -> bool:
    if prompt is None or not prompt.exists():
        return False
    text = read(prompt)
    supplied = text
    for marker in ("Forbidden", "Style requirements", "Output requirements"):
        index = supplied.find(marker)
        if index != -1:
            supplied = supplied[:index]
            break
    return bool(re.search(r"\bjamming\b", supplied, flags=re.IGNORECASE))


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


def manuscript_paragraphs(text: str) -> list[str]:
    body = manuscript_region(text)
    paragraphs = []
    for raw in re.split(r"\n\s*\n", body):
        paragraph = raw.strip()
        if not paragraph or paragraph.startswith("#"):
            continue
        paragraphs.append(paragraph)
    return paragraphs


def validate_public_writing_demos(errors: list[str]) -> None:
    public_links: set[str] = set()

    for rel_path in PUBLIC_SURFACES:
        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"Missing public surface: {rel_path}")
            continue
        region = public_region(read(path))
        for label, pattern in PUBLIC_OUTPUT_BLOCKERS.items():
            if pattern.search(region):
                errors.append(f"{rel_path} public display contains blocker wording: {label}")
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
            if pattern.search(text):
                errors.append(f"{output_rel} contains public-demo blocker: {label}")

        if "abstract" in output_rel:
            if re.search(r"\bjamming\b", text, flags=re.IGNORECASE) and not prompt_supplies_jamming(prompt):
                errors.append(f"{output_rel} contains jamming without supplied prompt mechanism")

        if "related_work" in output_rel:
            for label in RELATED_WORK_BLOCKERS:
                pattern = PUBLIC_OUTPUT_BLOCKERS[label]
                if pattern.search(text):
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
