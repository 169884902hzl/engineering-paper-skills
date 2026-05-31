---
name: engineering-paper-router
description: Route ambiguous or mixed English engineering paper tasks to the correct engineering paper skill. Use when the user asks broadly to improve, write, check, revise, respond to comments on, or prepare an engineering paper and it is unclear whether the task belongs to writing, polishing, figure/table work, response drafting, or validation.
---

# Engineering Paper Router

Use this skill only to choose the right workflow and required inputs. Do not
write final manuscript prose unless the user explicitly asks to continue after
routing.

## Core Stance

- Route first; do not draft first.
- Preserve evidence boundaries in the recommended next prompt.
- For mixed tasks, name a primary skill, secondary skills, and workflow order.
- If readiness or completion is requested, include `engineering-validation`.

## Boundaries

- Use this skill when the correct engineering paper skill is unclear.
- Do not use it when the user explicitly names one of the five task skills and
  the request matches that skill.

## When To Open Extra Files

| File | Open when |
|---|---|
| [references/examples.md](references/examples.md) | Needing routing examples |
| [references/failure-modes.md](references/failure-modes.md) | Avoiding router overreach or single-skill bias |
| [../_shared/evidence-boundary.md](../_shared/evidence-boundary.md) | Routing tasks that request strong claims, citations, validation, or missing-evidence work |
| [../_shared/output-mode.md](../_shared/output-mode.md) | User asks for a short route only |

## Routing Table

| User task | Route |
|---|---|
| draft/rebuild title, abstract, Introduction, Methods, Experiments, Discussion, or Conclusion | `engineering-writing` |
| polish existing prose, improve flow, downgrade claims, translate source notes into English prose | `engineering-polishing` |
| plan or revise figures, tables, captions, visual roles, page budget, or visual consistency | `engineering-figure-table` |
| classify reviewer/advisor/editor comments, build revision tracker, draft response letter | `engineering-response` |
| compile/check manuscript, inspect citations, claim-evidence anchors, figures/tables, readiness | `engineering-validation` |

## Mixed Workflow Order

For full-paper work, use:

1. `engineering-writing`
2. `engineering-figure-table`
3. `engineering-polishing`
4. `engineering-response` if comments exist
5. `engineering-validation`

## Default Output

```text
Recommended route
- Primary skill:
- Secondary skill:
- Reason:

Required inputs
- ...

Evidence boundary
- Do not invent:
- Must verify before claiming ready:

Next prompt to use
[copyable prompt]
```
