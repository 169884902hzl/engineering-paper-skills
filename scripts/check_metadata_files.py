#!/usr/bin/env python3
"""Validate repository metadata, Pages discovery files, and workflow shape.

This check is intentionally lightweight and dependency-free. It is not a full
YAML/CFF linter; it catches the metadata failures most likely to confuse users,
search engines, or GitHub Actions in this no-release beta repository.
"""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES_ROOT = "https://169884902hzl.github.io/engineering-paper-skills/"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require_file(path: Path, errors: list[str]) -> bool:
    if not path.exists():
        errors.append(f"Missing {path.relative_to(ROOT)}")
        return False
    return True


def check_citation(errors: list[str]) -> None:
    path = ROOT / "CITATION.cff"
    if not require_file(path, errors):
        return
    text = read(path)
    required_lines = [
        "cff-version: 1.2.0",
        'title: "Engineering Paper Skills"',
        'version: "commit-based-beta"',
        "repository-code: ",
        "url: ",
        "abstract: ",
    ]
    for marker in required_lines:
        if marker not in text:
            errors.append(f"{path.relative_to(ROOT)} missing marker: {marker}")
    for forbidden in ('version: "0.1.0-beta"', "date-released:"):
        if forbidden in text:
            errors.append(f"{path.relative_to(ROOT)} contains release-like metadata: {forbidden}")
    if text.count("\n") < 12:
        errors.append(f"{path.relative_to(ROOT)} appears collapsed into too few lines")


def check_workflows(errors: list[str]) -> None:
    workflow_dir = ROOT / ".github/workflows"
    if not require_file(workflow_dir, errors):
        return
    for path in sorted(workflow_dir.glob("*.yml")):
        text = read(path)
        lines = text.splitlines()
        if len(lines) < 8:
            errors.append(f"{path.relative_to(ROOT)} appears collapsed into too few lines")
        for marker in ("name:", "on:", "jobs:"):
            if not any(line.startswith(marker) for line in lines):
                errors.append(f"{path.relative_to(ROOT)} missing top-level {marker}")


def check_sitemap(errors: list[str]) -> None:
    path = ROOT / "docs/sitemap.xml"
    if not require_file(path, errors):
        return
    try:
        root = ET.fromstring(read(path))
    except ET.ParseError as exc:
        errors.append(f"{path.relative_to(ROOT)} invalid XML: {exc}")
        return
    if not root.tag.endswith("urlset"):
        errors.append(f"{path.relative_to(ROOT)} root element must be urlset")
    locs = [element.text or "" for element in root.iter() if element.tag.endswith("loc")]
    if not locs:
        errors.append(f"{path.relative_to(ROOT)} has no loc entries")
    for loc in locs:
        if not loc.startswith(PAGES_ROOT):
            errors.append(f"{path.relative_to(ROOT)} loc outside Pages root: {loc}")


def check_robots(errors: list[str]) -> None:
    path = ROOT / "docs/robots.txt"
    if not require_file(path, errors):
        return
    lines = [line.strip() for line in read(path).splitlines() if line.strip()]
    required = [
        "User-agent: *",
        "Allow: /",
        f"Sitemap: {PAGES_ROOT}sitemap.xml",
    ]
    for marker in required:
        if marker not in lines:
            errors.append(f"{path.relative_to(ROOT)} missing line: {marker}")


def check_html_pages(errors: list[str]) -> None:
    for name in ("index.html", "demo.html", "quality-gates.html", "discovery.html"):
        path = ROOT / "docs" / name
        if not require_file(path, errors):
            continue
        text = read(path)
        for marker in ("<title>", '<meta name="description"', '<link rel="canonical"'):
            if marker not in text:
                errors.append(f"{path.relative_to(ROOT)} missing marker: {marker}")


def check_no_release_docs(errors: list[str]) -> None:
    for rel_path, markers in {
        "KNOWN_GOOD.md": ["Commit anchors", "Behavior evidence", "Known limitations"],
        "CHANGELOG.md": ["No-release beta changelog", "6bec865", "d03d683", "8da3ceb"],
    }.items():
        path = ROOT / rel_path
        if not require_file(path, errors):
            continue
        text = read(path)
        for marker in markers:
            if marker not in text:
                errors.append(f"{rel_path} missing marker: {marker}")


def main() -> int:
    errors: list[str] = []
    check_citation(errors)
    check_workflows(errors)
    check_sitemap(errors)
    check_robots(errors)
    check_html_pages(errors)
    check_no_release_docs(errors)

    if errors:
        print("Metadata file check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Metadata file check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
