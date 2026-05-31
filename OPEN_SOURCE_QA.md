# Open Source QA

Run these checks before publishing, tagging, or accepting a pull request.

## Repository QA

```bash
python scripts/validate_repo.py
```

This checks:

- required skill files
- `SKILL.md` frontmatter and reference tables
- relative Markdown links
- agent metadata fields
- private-path and stale-wording patterns
- expected minimal and adversarial prompt specs

## Codex Skill Validation

```bash
for s in skills/engineering-*; do
  python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$s"
done
```

## Manual Scans

```bash
rg -n "TO[D]O|\\[TO[D]O\\]|dissertio[n]|Us[e] -" skills
rg -n "[\\p{Han}]" skills
```

For this package, validation was run on both installed skill sources and copied
package skill directories:

- `engineering-writing`
- `engineering-polishing`
- `engineering-figure-table`
- `engineering-response`
- `engineering-validation`

All returned `Skill is valid!` during the hardening pass.

## Manual Review Checklist

- Each skill has a focused trigger description.
- Each skill states handoff boundaries to the other skills.
- Each skill keeps the entry `SKILL.md` concise and routes details to
  `references/`.
- Each skill has examples and failure modes.
- English manuscript output is the default.
- Fact-boundary rules are explicit.
- Claim-evidence mapping is explicit.
- Figure/table responsibility is explicit.
- Comment-response workflow requires acceptance evidence.
- Validation workflow requires fresh command evidence.
- Validation outputs distinguish `PASS`, `FAIL`, `PARTIAL`, `NOT_RUN`, and
  `UNKNOWN`.
- Minimal and adversarial prompt specs still match the intended behavior.
- Third-party license notices are preserved.
