---
name: engineering-response
description: Draft, audit, or revise English response letters and revision plans for engineering papers from advisor, senior-author, reviewer, or editor comments. Use when the user provides comments, decision letters, rebuttal notes, revision drafts, or asks how to respond, what to revise, how to classify comments, how to avoid over-editing, or how to map each comment to manuscript changes.
---

# Engineering Response

Use this skill to turn comments into traceable revision tasks and professional
English responses.

## Core Stance

- Preserve each comment before responding.
- Answer every concern or mark it as unresolved.
- Map responses to manuscript evidence, a revision location, or explicit author
  input needed.
- Do not invent experiments, line numbers, figures, citations, analyses, or
  manuscript changes.
- Prefer concise, evidence-linked responses over defensive explanations.
- When a comment reveals misunderstanding, first check whether the manuscript
  caused it.

## Boundaries

- Use this skill for comment triage, revision planning, rebuttal drafts, and
  response letters.
- Use `engineering-writing` for manuscript section drafting after a comment has
  been turned into a concrete edit.
- Use `engineering-polishing` for prose-only improvements.
- Use `engineering-figure-table` for caption, figure, or table revisions.
- Use `engineering-validation` before claiming a response package is complete or
  before using final line numbers.

## When to Open Extra Files

| File | Open when |
|---|---|
| [references/comment-routing.md](references/comment-routing.md) | Classifying advisor/reviewer comments and deciding which section to edit first |
| [references/revision-tracker.md](references/revision-tracker.md) | Turning comments into concrete edit tasks with acceptance evidence |
| [references/comment-resolution-worksheet.md](references/comment-resolution-worksheet.md) | Building a full comment-to-action worksheet before editing |
| [references/response-letter.md](references/response-letter.md) | Drafting point-by-point English responses |
| [references/comment-examples.md](references/comment-examples.md) | Handling common comments about experiments, methods, claims, captions, related work, conclusions, or abstract |
| [references/tone-and-risk.md](references/tone-and-risk.md) | Handling disagreement, impossible requests, missing experiments, or high-risk claims |
| [references/examples.md](references/examples.md) | Needing concrete response tracker and reply examples |
| [references/failure-modes.md](references/failure-modes.md) | Handling false completed-change claims or impossible reviewer requests |

## Workflow

1. Split editor/advisor/reviewer comments into stable IDs.
2. Classify each comment by type, severity, section, and missing input.
3. Identify the real complaint, not just the surface wording.
4. Choose `revise`, `defer with reason`, or `no change with reason`.
5. Define prohibited over-edit.
6. Define acceptance evidence and minimum verification.
7. Draft the response only after the change or placeholder is clear.
8. Run completeness and factuality checks before calling the package ready.

## Default Output

```text
Response strategy summary
- Decision type:
- Main risks:
- Revision priority:

Comment-response tracker
| ID | Comment | Type | Severity | Target | Action | Evidence/change needed | Status |

Draft response
[English point-by-point response]

Revision checklist
- ...
```
