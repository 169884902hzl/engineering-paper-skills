# Open Source QA

## Source Currency

`phd-writing` was checked against origin HEAD:

```text
cb4d845c6521d70017c0a08edbb8597d72be3642
```

## Validation Commands

Run from a machine with Codex skills installed:

```bash
for s in skills/engineering-*; do
  python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$s"
done
```

Run stale-wording scans:

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
- Each skill keeps the entry `SKILL.md` concise and routes details to
  `references/`.
- English manuscript output is the default.
- Fact-boundary rules are explicit.
- Claim-evidence mapping is explicit.
- Figure/table responsibility is explicit.
- Comment-response workflow requires acceptance evidence.
- Validation workflow requires fresh command evidence.
- MIT notice for `phd-writing` is preserved.
