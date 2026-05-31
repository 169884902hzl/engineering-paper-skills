---
name: engineering-validation
description: Validate English engineering manuscript readiness before claiming edits are complete. Use when the user asks to check a paper, compile LaTeX, verify references, page count, citations, figure/table consistency, claim-evidence anchors, final-paper synchronization, submission checklist, or whether a conference/journal manuscript is safe to submit.
---

# Engineering Validation

Use this skill before saying a paper edit is complete, fixed, or ready.

## Core Stance

- No verification, no completion claim.
- A dry read is not a build check.
- Report exactly what was run and what was not run.
- Treat evidence anchors, citations, figures, tables, and PDF output as part of
  manuscript correctness.
- For existing paper repos, read the current live draft and project-specific
  instructions before validating.

## When to Open Extra Files

| File | Open when |
|---|---|
| [references/live-draft-check.md](references/live-draft-check.md) | Confirming source draft, input order, title, author/blind state, or final sync |
| [references/latex-build.md](references/latex-build.md) | Compiling LaTeX, checking bibitem count, page count, warnings, or diff checks |
| [references/evidence-audit.md](references/evidence-audit.md) | Checking contributions, claims, section anchors, citations, and overclaims |
| [references/final-readonly-check.md](references/final-readonly-check.md) | Running the final 30-minute style read-only inspection |
| [references/error-archive.md](references/error-archive.md) | Diagnosing common manuscript failure symptoms and the first section to inspect |
| [references/submission-checklist.md](references/submission-checklist.md) | Final read-only inspection before submission |

## Workflow

1. Identify manuscript root and live draft.
2. Read local instructions and relevant build files.
3. Check structure anchors: thesis, contribution list, main results, ablation,
   limitations.
4. Check figures, tables, captions, labels, and category/metric names.
5. Run the smallest relevant build and consistency commands.
6. Report evidence, failures, and unverified items.

## Default Output

```text
Validation result
- Status:
- Commands run:
- Evidence:
- Failures:
- Not verified:

Next actions
- ...
```
