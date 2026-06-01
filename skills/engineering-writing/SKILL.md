---
name: engineering-writing
description: Draft, restructure, or plan English engineering research paper sections from author-provided claims, methods, results, figures, notes, outlines, LaTeX files, or manuscript drafts. Use for section logic, contribution-evidence mapping, abstract/introduction/related-work/methods/experiments/discussion/conclusion drafting, and evidence-bounded manuscript prose. Do not use for pure language polishing, figure/table-only work, reviewer responses, or final build/readiness validation unless the user explicitly asks for those workflows.
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
- Do not finalize Abstract or Conclusion claims before Methods/Experiments
  evidence and boundaries are available; produce a scaffold instead.
- For an existing paper, read the current live draft and relevant files before
  rewriting.

## Boundaries

- Use `engineering-polishing` for pure language polish after the section logic is
  already stable.
- Use `engineering-figure-table` for captions, table design, visual roles, and
  figure/table consistency.
- Use `engineering-response` for reviewer, editor, advisor, or senior-author
  comments.
- Use `engineering-validation` for build checks, readiness claims, citation
  checks, and final submission QA.

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
| [references/methods-worksheet.md](references/methods-worksheet.md) | A Methods draft risks becoming a module directory or formula dump |
| [references/experiments.md](references/experiments.md) | Planning or writing Experiments/Results, baselines, metrics, main results, ablations, failure analysis |
| [references/experiments-worksheet.md](references/experiments-worksheet.md) | Results need setup, baseline, metric, ablation, category, stress, or failure-envelope structure |
| [references/discussion.md](references/discussion.md) | Writing Discussion, limitations, interpretation, or implications |
| [references/conclusion.md](references/conclusion.md) | Writing a bounded conclusion and future work |
| [references/section-boundaries.md](references/section-boundaries.md) | Auditing whether content belongs in the right section or when a section is drifting |
| [references/section-budget.md](references/section-budget.md) | Checking whether a section is too thin, too dense, or taking space from evidence |
| [references/page-budget-war-plan.md](references/page-budget-war-plan.md) | Cutting manuscript length without damaging evidence anchors |
| [references/source-learning.md](references/source-learning.md) | Learning structure from 3-5 neighboring papers without copying wording or surface format |
| [references/bad-sentence-repairs.md](references/bad-sentence-repairs.md) | Repairing common bad manuscript sentences and section-level failure symptoms |
| [manifest.yaml](manifest.yaml) | Planning which references to load for section, input-state, or failure-repair tasks |
| [references/examples.md](references/examples.md) | Needing concrete prompt and output behavior examples |
| [references/failure-modes.md](references/failure-modes.md) | Handling thin evidence, invented-citation requests, or overclaim pressure |
| [references/venue-aware-writing.md](references/venue-aware-writing.md) | Target venue family may change abstract, limitation, reproducibility, or contribution framing |
| [references/paper-level-narrative-map.md](references/paper-level-narrative-map.md) | Full-paper or multi-section writing needs story dependency checks |
| [../_shared/story-spine.md](../_shared/story-spine.md) | Building problem-to-evidence-to-boundary logic before drafting |
| [../_shared/evidence-boundary.md](../_shared/evidence-boundary.md) | Any task asks for stronger claims, missing evidence, or manuscript facts |
| [../_shared/citation-boundary.md](../_shared/citation-boundary.md) | Related Work or citations are requested without provided sources |
| [../_shared/claim-strength.md](../_shared/claim-strength.md) | Calibrating verbs, novelty, robustness, generalization, or causal language |
| [../_shared/ai-assisted-writing-policy.md](../_shared/ai-assisted-writing-policy.md) | AI-assisted prose or venue disclosure risk is relevant |
| [../_shared/list-to-argument.md](../_shared/list-to-argument.md) | Source material is a bullet list, module list, result-row list, or contribution list |
| [../_shared/non-english-source-notes.md](../_shared/non-english-source-notes.md) | Non-English notes must become English manuscript prose |
| [../_shared/output-mode.md](../_shared/output-mode.md) | The user asks for output only |
| [../_shared/sentence-role-and-story-flow.md](../_shared/sentence-role-and-story-flow.md) | Drafting, shortening, or reordering paragraphs where every sentence must justify its role |
| [../_shared/terminology-ledger.md](../_shared/terminology-ledger.md) | A writing task may rename methods, metrics, categories, or baselines |

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
2. Build the story spine: problem, gap, insight, method, evidence, boundary,
   and implication.
3. Create a contribution-evidence map before writing strong claims. Use columns:
   `Claim`, `First stated in`, `Mechanism support`, `Evidence`, and
   `Boundary/overclaim risk`.
4. Choose the section reference and assign one job to each paragraph.
5. Draft from evidence outward.
6. Calibrate claim verbs: `show`, `indicate`, `suggest`, `support`, `enable`,
   `demonstrate` only when directly supported.
7. Remove unsupported novelty, universal claims, and vague adjectives.
8. Check sentence roles: every sentence must have a function, necessity,
   placement, connection, and evidence boundary.
9. Return prose plus assumptions, missing evidence, and a short claim-evidence
   map unless prose-only output was requested and no unsupported-risk note would
   be hidden.

## Default Output

```text
One-sentence thesis
[In task/setting, we address gap by method/formulation, supported by evidence, within boundary.]

Story spine
| Node | Section location | Claim | Evidence anchor | Boundary | If removed, what breaks? |

Section job map
| Section/paragraph | Job | Evidence anchor | Boundary |

Source-note triage
| Source item | Fact / Assumption / Unsupported | Can enter prose? | Handling |

Draft
[English manuscript prose]

Claim-evidence map
| Claim | First stated in | Mechanism support | Evidence support | Boundary/overclaim risk | Repair |

Unsupported or downgraded claims
| Requested claim | Status | Reason | Safe wording |

Sentence role audit
| Sentence/span | Job | Needed because | Connection to previous/next | Evidence boundary | Action |

Missing evidence or assumptions
- ...
```
