# Engineering Paper Skills

Five Codex skills for writing, polishing, revising, and validating English
engineering conference and journal papers.

The suite is designed for evidence-bound technical writing. It is especially
useful for robotics, control, perception, learning, systems, algorithm, device,
benchmark, and experiment-heavy engineering papers.

## Skills

| Skill | Purpose |
|---|---|
| `engineering-writing` | Draft or restructure titles, abstracts, introductions, related work, methods, experiments, discussions, conclusions, and full paper arguments |
| `engineering-polishing` | Polish English manuscript prose while preserving facts, claim strength, terminology, and evidence boundaries |
| `engineering-figure-table` | Plan and audit figures, tables, captions, table notes, visual responsibilities, and evidence links |
| `engineering-response` | Convert advisor, senior-author, editor, or reviewer comments into revision tasks and English responses |
| `engineering-validation` | Validate manuscript readiness with live-draft checks, LaTeX builds, evidence anchors, citations, figures, tables, and submission checks |

## Installation

Copy the skill directories into your Codex skills directory:

```bash
cp -a skills/engineering-* ~/.codex/skills/
```

Then restart Codex so the new skills are loaded.

The legacy `engineering-paper-writing` router is not included in this package.
Use the specific skill that matches the task.

## Design Principles

- Final manuscript prose defaults to English.
- Non-English notes may be used as source material, but final paper text should
  be English unless explicitly requested otherwise.
- Evidence comes before wording.
- Do not invent experiments, mechanisms, references, metrics, numbers, novelty,
  limitations, or conclusions.
- Each claim must map to method support, figure/table support, experiment
  support, or an explicit boundary.
- Sentence polishing must not hide broken paper logic.
- No readiness claim should be made without fresh validation evidence.

## Source Basis

This suite is derived from two author-supplied sources:

1. A CASE 2026 engineering conference-paper writing guide, used for paper
   workflow, section responsibilities, figure/table logic, comment routing,
   page-budget strategy, and final validation.
2. `phd-writing` by Yuqi Cheng, used for fact-boundary rules, paragraph
   function classification, progressive argument construction, list handling,
   engineering topic modules, and anti-generic-prose checks.

See `SOURCE_MAPPING.md` for the detailed source-to-skill mapping.

## License and Attribution

The package is released under the MIT License. Portions of the writing rules are
adapted from `phd-writing`, which is also MIT licensed. See `NOTICE.md` for
third-party attribution.

## Quality Checks

The installed skill sources and this package were checked with:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-dir>
rg -n "TO[D]O|\\[TO[D]O\\]|dissertio[n]|Us[e] -" <skill-dirs>
rg -n "[\\p{Han}]" <skill-dirs>
```

Use `engineering-validation` before claiming any manuscript edit is ready.
