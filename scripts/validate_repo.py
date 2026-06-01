#!/usr/bin/env python3
"""Repository QA for Engineering Paper Skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_expected_behavior import validate_specs  # noqa: E402

SKILLS = sorted((ROOT / "skills").glob("engineering-*"))

EXPECTED_SKILLS = {
    "engineering-paper-auditor",
    "engineering-paper-router",
    "engineering-writing",
    "engineering-polishing",
    "engineering-figure-table",
    "engineering-response",
    "engineering-validation",
}

REQUIRED_SHARED = {
    "evidence-boundary.md",
    "citation-boundary.md",
    "claim-strength.md",
    "list-to-argument.md",
    "non-english-source-notes.md",
    "output-mode.md",
    "sentence-role-and-story-flow.md",
    "terminology-ledger.md",
}


def s(*parts: str) -> str:
    return "".join(parts)


PRIVATE_PATTERNS = [
    r"/home/",
    r"/Users/",
    r"C:\\Users\\",
    s("ag", "ilex"),
    s("cobot", "_magic"),
    s("ieee", "_case", "2026"),
    s("final", "_paper"),
    "\u4f1a\u8bae\u8bba\u6587\u5199\u4f5c\u6307\u5357",
    "\u5bfc\u5e08",
    "\u5e08\u5144",
    "\u5fae\u4fe1",
    "\u624b\u673a\u53f7",
]

STALE_PATTERNS = [
    r"TODO",
    r"\[TODO\]",
    r"FIXME",
    r"TBD",
    s("Source", " Basis"),
    s("Source", " Mapping"),
    s("source", "-to-", "skill"),
    "\u6765\u6e90\u4f9d\u636e",
    "\u6765\u6e90\u6620\u5c04",
    s("dissert", "ation"),
    "\u535a\u58eb",
    s("paper", "-facing"),
    s("truth", " layer"),
    s("scope", " drift"),
    s("money", " figure"),
]

REQUIRED_PROMPTS = {
    "auditor_min.md",
    "auditor_adversarial.md",
    "auditor_realistic.md",
    "router_min.md",
    "router_adversarial.md",
    "router_realistic.md",
    "writing_min.md",
    "writing_adversarial.md",
    "writing_realistic.md",
    "polishing_min.md",
    "polishing_adversarial.md",
    "polishing_realistic.md",
    "figure_table_min.md",
    "figure_table_adversarial.md",
    "figure_table_realistic.md",
    "response_min.md",
    "response_adversarial.md",
    "response_realistic.md",
    "validation_min.md",
    "validation_adversarial.md",
    "validation_realistic.md",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_simple_agent_yaml(path: Path) -> dict[str, str]:
    """Parse the tiny agents/openai.yaml schema without third-party packages."""
    values: dict[str, str] = {}
    in_interface = False
    for raw_line in read(path).splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line == "interface:":
            in_interface = True
            continue
        if not in_interface:
            raise ValueError(f"{rel(path)} only supports an interface mapping")
        if not line.startswith("  ") or ":" not in line:
            raise ValueError(f"{rel(path)} invalid interface field: {line}")
        key, value = line.strip().split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] == '"':
            value = value[1:-1]
        if not value:
            raise ValueError(f"{rel(path)} field {key} is empty")
        values[key] = value
    return values


def md_files() -> list[Path]:
    return [
        p
        for p in ROOT.rglob("*.md")
        if ".git" not in p.parts and "tests/expected" not in str(p)
    ]


def check_structure(errors: list[str]) -> None:
    skill_names = {p.name for p in SKILLS}
    if skill_names != EXPECTED_SKILLS:
        missing = sorted(EXPECTED_SKILLS - skill_names)
        extra = sorted(skill_names - EXPECTED_SKILLS)
        if missing:
            errors.append(f"Missing engineering skills: {', '.join(missing)}")
        if extra:
            errors.append(f"Unexpected engineering skills: {', '.join(extra)}")

    shared = ROOT / "skills/_shared"
    if not shared.exists():
        errors.append("Missing shared reference directory: skills/_shared")
    else:
        shared_files = {p.name for p in shared.glob("*.md")}
        missing_shared = REQUIRED_SHARED - shared_files
        if missing_shared:
            errors.append(f"Missing shared references: {', '.join(sorted(missing_shared))}")

    for skill in SKILLS:
        for required in ("SKILL.md", "references", "agents/openai.yaml"):
            if not (skill / required).exists():
                errors.append(f"{rel(skill)} missing {required}")

        skill_md = skill / "SKILL.md"
        if not skill_md.exists():
            continue
        text = read(skill_md)
        if not text.startswith("---"):
            errors.append(f"{rel(skill_md)} missing YAML frontmatter")
        if "description:" not in text.split("---", 2)[1]:
            errors.append(f"{rel(skill_md)} missing description")
        if "## Boundaries" not in text:
            errors.append(f"{rel(skill_md)} missing Boundaries section")
        for ref in re.findall(r"\]\(((?:references|\.\./_shared)/[^)]+\.md)\)", text):
            if not (skill / ref).exists():
                errors.append(f"{rel(skill_md)} links missing reference {ref}")

        agent = skill / "agents/openai.yaml"
        if agent.exists():
            try:
                agent_values = parse_simple_agent_yaml(agent)
            except ValueError as exc:
                errors.append(str(exc))
                continue
            for key in ("display_name", "short_description", "default_prompt"):
                if key not in agent_values:
                    errors.append(f"{rel(agent)} missing {key}")
            for key, value in agent_values.items():
                if "\n" in value or len(value) > 240:
                    errors.append(f"{rel(agent)} field {key} is too long or multiline")


def check_links(errors: list[str]) -> None:
    link_re = re.compile(r"\]\(([^)]+)\)")
    for md in md_files():
        text = read(md)
        for match in link_re.finditer(text):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target_path = (md.parent / target).resolve()
            if not target_path.exists():
                errors.append(f"{rel(md)} broken relative link: {target}")


def check_patterns(errors: list[str]) -> None:
    scan_files = [
        p
        for p in ROOT.rglob("*")
        if p.is_file()
        and ".git" not in p.parts
        and p.suffix in {".md", ".yaml", ".yml", ".py", ".sh", ".txt"}
        and rel(p) != "scripts/validate_repo.py"
    ]

    for path in scan_files:
        text = read(path)
        for pattern in PRIVATE_PATTERNS:
            if re.search(pattern, text, flags=re.IGNORECASE):
                errors.append(f"{rel(path)} matches private pattern: {pattern}")
        for pattern in STALE_PATTERNS:
            if re.search(pattern, text, flags=re.IGNORECASE):
                errors.append(f"{rel(path)} matches stale pattern: {pattern}")


def check_prompts(errors: list[str]) -> None:
    prompt_dir = ROOT / "tests/prompts"
    expected_dir = ROOT / "tests/expected"
    prompts = {p.name for p in prompt_dir.glob("*.md")} if prompt_dir.exists() else set()

    missing = REQUIRED_PROMPTS - prompts
    if missing:
        errors.append(f"Missing prompt specs: {', '.join(sorted(missing))}")

    for prompt_name in REQUIRED_PROMPTS:
        expected = expected_dir / prompt_name.replace(".md", ".yaml")
        if not expected.exists():
            errors.append(f"Missing expected behavior for {prompt_name}")

    try:
        errors.extend(validate_specs(expected_dir))
    except Exception as exc:  # pragma: no cover - defensive release check
        errors.append(f"Expected-behavior validation crashed: {exc}")


def main() -> int:
    errors: list[str] = []
    check_structure(errors)
    check_links(errors)
    check_patterns(errors)
    check_prompts(errors)

    if errors:
        print("Repository QA failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository QA passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
