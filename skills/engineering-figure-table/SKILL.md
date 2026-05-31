---
name: engineering-figure-table
description: Plan, revise, audit, or polish figures, tables, captions, table notes, and visual evidence flow for English engineering conference or journal papers. Use when the user asks about figure responsibility, multi-panel layout, main-result tables, ablation tables, captions, table formatting, object/category naming consistency, page budget for visuals, or whether visuals support manuscript claims.
---

# Engineering Figure Table

Use this skill to make figures and tables serve the manuscript argument.

## Core Stance

- Define visual responsibility before visual styling.
- A figure or table should carry a specific claim, setup fact, evidence axis, or
  reader action.
- Do not let captions claim what the visual does not show.
- Do not use tables as unstructured parameter dumps unless the table's job is
  setup compression.
- Keep category names, metric names, captions, and prose consistent.

## When to Open Extra Files

| File | Open when |
|---|---|
| [references/visual-contract.md](references/visual-contract.md) | Planning figure/table responsibility or deciding which visuals are needed |
| [references/figure-roles.md](references/figure-roles.md) | Deciding what motivation, framework, workflow, gallery, or evidence figures should do |
| [references/captions.md](references/captions.md) | Writing or auditing captions and table notes |
| [references/tables.md](references/tables.md) | Designing setup, main results, ablation, or stress-test tables |
| [references/consistency.md](references/consistency.md) | Checking category names, metrics, labels, caption style, and prose alignment |
| [references/page-budget.md](references/page-budget.md) | Cutting visual space, caption length, or table detail without damaging evidence |

## Workflow

1. State the paper claim the visual supports.
2. Assign one responsibility to each figure/table.
3. Map each panel, row, or column to a piece of evidence.
4. Check whether the caption states only visible or tabulated information.
5. Check consistency across prose, caption, labels, and notes.
6. Check whether any category/metric rename needs coordinated changes.
7. If editing LaTeX, preserve labels and references unless there is a direct
   reason to change them.

## Default Output

```text
Visual audit
| Item | Responsibility | Evidence link | Risk | Action |

Caption/table revision
[English caption or table plan]
```
