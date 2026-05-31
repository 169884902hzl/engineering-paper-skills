# Validation Dry Read Not Ready

## Before

```text
I read the PDF and it looks ready. The build and citations should be fine.
```

## Problem

A dry read is not a build, citation, or claim-evidence validation.

## After

```text
Validation result
- Goal interpreted as: full submission readiness
- Build: NOT_RUN
- References: NOT_RUN
- Figures/tables: NOT_RUN
- Claim-evidence audit: PARTIAL
- Private/stale wording scan: NOT_RUN
- Overall readiness: CANNOT_DETERMINE

Evidence
- Commands run: none
- Files inspected: PDF text only
- Not verified: source build, bibliography, labels, figure/table consistency,
  final source synchronization
```

## Skill Behavior

- Use `engineering-validation`.
- Report `NOT_RUN` when checks were not run.
- Do not call the paper ready from a dry read.
