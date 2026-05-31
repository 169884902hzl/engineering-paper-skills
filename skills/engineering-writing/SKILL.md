---
name: engineering-writing
description: Draft, restructure, or plan English engineering research paper sections from author-provided claims, results, figures, notes, outlines, or manuscript drafts. Use when the user asks to write or rebuild a title, abstract, introduction, related work, methods, experiments/results, discussion, conclusion, full paper outline, section logic, contribution-evidence map, or IEEE/robotics conference manuscript argument.
---

# Engineering Writing

Use this skill for English manuscript creation and structural revision. It is
for writing the paper's argument, not merely polishing sentences.

## Core Stance

- Final manuscript prose defaults to English.
- Non-English notes are source material only; do not preserve them as the final
  manuscript language unless the user explicitly asks.
- Evidence comes first. Do not invent methods, datasets, experiments, metrics,
  numbers, references, mechanisms, novelty, limitations, or conclusions.
- Write the argument before writing sentences.
- Every claim must have a visible route to method detail, figure/table evidence,
  experiment evidence, or an explicit boundary.
- If evidence is missing, expose the gap or write a scaffold with placeholders.
- For an existing paper, read the current live draft and relevant files before
  rewriting.

## When to Open Extra Files

| File | Open when |
|---|---|
| [references/paper-workflow.md](references/paper-workflow.md) | Starting from scratch, rebuilding a draft, or deciding paper-writing order |
| [references/contribution-evidence.md](references/contribution-evidence.md) | Defining the paper thesis, contributions, claim boundaries, or evidence map |
| [references/title.md](references/title.md) | Drafting or auditing the title |
| [references/abstract.md](references/abstract.md) | Drafting or revising the abstract |
| [references/introduction.md](references/introduction.md) | Drafting Introduction, positioning, gap, formulation, or contribution list |
| [references/related-work.md](references/related-work.md) | Drafting Related Work, taxonomy, nearest-neighbor distinction, or folded literature positioning |
| [references/methods.md](references/methods.md) | Writing Methods, overview, formulas, system roles, algorithms, execution, or safety/deployment logic |
| [references/experiments.md](references/experiments.md) | Planning or writing Experiments/Results, baselines, metrics, main results, ablations, failure analysis |
| [references/discussion.md](references/discussion.md) | Writing Discussion, limitations, interpretation, or implications |
| [references/conclusion.md](references/conclusion.md) | Writing a bounded conclusion and future work |
| [references/section-boundaries.md](references/section-boundaries.md) | Auditing whether content belongs in the right section or when a section is drifting |
| [references/section-budget.md](references/section-budget.md) | Checking whether a section is too thin, too dense, or taking space from evidence |
| [references/source-learning.md](references/source-learning.md) | Learning structure from 3-5 neighboring papers without copying wording or surface format |

## Intake

Before drafting, identify:

- target section and venue
- paper type: robotics system, algorithm, method, benchmark, dataset, device,
  control, perception, learning, or experiment-heavy systems paper
- core object: system, task, method, dataset, mechanism, device, or phenomenon
- problem and gap
- proposed method or formulation
- evidence: figures, tables, metrics, comparisons, ablations, stress tests,
  qualitative evidence, or deployment evidence
- boundary: what is not shown
- current manuscript paths and page/word constraints

If `core claim`, `evidence`, or `boundary` is absent, state the gap before
drafting. You may still provide a scaffold.

## Workflow

1. Build a one-sentence thesis:
   `In [task/setting], we address [gap] by [method/formulation], supported by [evidence], within [boundary].`
2. Create a contribution-evidence map before writing strong claims.
3. Choose the section reference and assign one job to each paragraph.
4. Draft from evidence outward.
5. Calibrate claim verbs: `show`, `indicate`, `suggest`, `support`, `enable`,
   `demonstrate` only when directly supported.
6. Remove unsupported novelty, universal claims, and vague adjectives.
7. Return prose plus assumptions, missing evidence, and a short claim-evidence
   map unless the user asks for prose only.

## Default Output

```text
Draft
[English manuscript prose]

Claim-evidence map
| Claim | Evidence | Boundary |

Missing evidence or assumptions
- ...
```

## Source Basis

This skill is based primarily on the CASE conference-paper writing guide supplied
by the project author, with conservative fact-boundary rules adapted from
`https://github.com/hustCYQ/phd-writing`.
