---
name: engineering-writing
description: Draft, restructure, or plan English engineering research paper sections from author-provided claims, methods, results, figures, notes, outlines, LaTeX files, or manuscript drafts. Use for section logic, contribution-evidence mapping, abstract/introduction/related-work/methods/experiments/discussion/conclusion drafting, and evidence-bounded manuscript prose. Do not use for pure language polishing, figure/table-only work, reviewer responses, or final build/readiness validation unless the user explicitly asks for those workflows.
---

# Engineering Writing

Use this skill to write the paper's argument from the author's evidence. Most
of what makes a strong engineering paper is decided before prose: which claim,
which comparison, which table, which figure. This skill puts that experience
first and leaves sentence craft to the model.

## Hard Floor

- Never invent experiments, results, numbers, baselines, citations, datasets,
  or completed work. Planned work stays planned.
- If a fact that would change the scientific claim is missing, mark a concise
  placeholder (`[RESULT NEEDED]`, `[CITATION NEEDED]`, `[VALUE?]`) or ask, and
  keep writing the parts that are supported.
- Use mechanisms the author supplies. Do not add a physical or causal
  mechanism the author did not give.
- For an existing paper, read the live source and local project instructions
  before rewriting. Preserve LaTeX labels, citations, macros, and terminology.
- Final manuscript prose defaults to English. Non-English notes are source
  material; rebuild the argument in English rather than translating sentence
  by sentence.

## Boundaries

- Use `engineering-polishing` for wording once the section logic is stable.
- Use `engineering-figure-table` for captions, table design, and visual roles.
- Use `engineering-response` for reviewer, editor, or co-author comments.
- Use `engineering-paper-auditor` for a pre-submission reviewer simulation.
- Use `engineering-validation` for builds, references, and readiness claims.

## Experience First

- What to write first, and how to write while results are incomplete:
  [writing-process.md](../_shared/writing-process.md). In short: lock one
  sentence, allocate the page budget, design result tables before the
  remaining experiments, design figures from the tables, then write Methods,
  Experiments, Introduction, and the Abstract last.
- What reviewers will attack, so the draft can pre-empt it:
  [reviewer-attack-patterns.md](../_shared/reviewer-attack-patterns.md).
  Check P1 (handicapped baseline), P2 (unstated operating assumption), P3
  (unmeasured internal component), and P4 (added cost versus a simpler
  alternative) whenever drafting Introduction, Methods, or Experiments.
- How senior authors restructure a draft:
  [revision-moves.md](../_shared/revision-moves.md).

## Section Notes

- Abstract: the concrete failure mode, the method core, the evaluation scope,
  and the strongest numbers. Write it last.
- Introduction: task difficulty, the core bottleneck, why existing routes fall
  short, the design requirement that follows, and the proposed formulation.
  Let the problem drive the story, not the tool. State the key idea at
  principle level; keep mechanism detail for Methods. Each contribution is a
  testable sentence; their number follows the independent, supported
  advances.
- Related Work: organize by technical axis; give the nearest neighbors the
  detail the positioning needs; state only differences and limitations the
  sources support.
- Methods: a reader path (input, intermediate object, transformation, handoff,
  execution and failure handling), not a module directory. Say how every
  decision rule is computed; label heuristics as heuristics.
- Results: ranking, key number, the interpretation the evidence supports,
  per-category results, and the operating boundary. Turn numbers into
  findings (bottleneck, stage attribution, method-family verdict, closing
  lesson; see "From Numbers To Findings" in
  [revision-moves.md](../_shared/revision-moves.md)). Present an unmeasured
  mechanism as an interpretation, not a cause. Keep setup short and
  parameters in a table.
- Ablation: relate each major delta to a component role or failure mode, and
  remember that cumulative ablations depend on the order of addition.
- Robustness and failure: the stress axis, the trend, the route by which the
  factor affects the method, what still works, and the hardest regime.
- Conclusion: the method, the strongest evidence, a bounded takeaway, and
  future work derived from the observed failure regime.

Scope belongs in the prose as a concrete operating condition, not as a
disclaimer. Keep it wherever a passage is read on its own (Abstract, headline
result, Conclusion) and avoid repeating it in adjacent sentences. Process
language ("the supplied notes show", "pending
verification") and audit language ("without claiming") do not belong in
manuscript prose.

## Request Modes

- WRITE (draft, compose, turn notes or results into prose): return usable
  manuscript prose first. Add a short note after it only for placeholders,
  missing evidence, or claims the author should check.
- PLAN (outline, paper plan, contribution design, writing order): start from
  the one-sentence thesis, the section job map, the table slots, and the
  contribution-evidence map.
- AUDIT: hand off to `engineering-paper-auditor`.
- POLISH: hand off to `engineering-polishing`.

Follow the user's requested length and format. If the user asks for prose
only, return prose only.

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
| [references/ral-style-writing-guide.md](references/ral-style-writing-guide.md) | The user explicitly wants RA-L-style section skeletons or sentence patterns |
| [references/positive-patterns.md](references/positive-patterns.md) | Choosing a paper-level or section-level pattern before drafting, or a draft reads structurally generic |
| [references/bad-sentence-repairs.md](references/bad-sentence-repairs.md) | Repairing common bad manuscript sentences and section-level failure symptoms |
| [manifest.yaml](manifest.yaml) | Looking up which references belong to a section or request type |
| [references/examples.md](references/examples.md) | Needing concrete prompt and output behavior examples |
| [references/failure-modes.md](references/failure-modes.md) | Handling thin evidence, invented-citation requests, or overclaim pressure |
| [references/venue-aware-writing.md](references/venue-aware-writing.md) | Target venue family may change abstract, limitation, reproducibility, or contribution framing |
| [references/paper-level-narrative-map.md](references/paper-level-narrative-map.md) | Full-paper or multi-section writing needs story dependency checks |
| [../_shared/writing-process.md](../_shared/writing-process.md) | Deciding what to write first, or writing while results are incomplete |
| [../_shared/reviewer-attack-patterns.md](../_shared/reviewer-attack-patterns.md) | Drafting Introduction, Methods, or Experiments that a reviewer will probe |
| [../_shared/revision-moves.md](../_shared/revision-moves.md) | Restructuring an existing draft |
| [../_shared/story-spine.md](../_shared/story-spine.md) | Building problem-to-evidence-to-boundary logic before drafting |
| [../_shared/evidence-boundary.md](../_shared/evidence-boundary.md) | Any task asks for stronger claims, missing evidence, or manuscript facts |
| [../_shared/citation-boundary.md](../_shared/citation-boundary.md) | Related Work or citations are requested without provided sources |
| [../_shared/citation-verification-workflow.md](../_shared/citation-verification-workflow.md) | The user supplies externally discovered citations (deep research, scholarly APIs) that need a verification gate before Related Work positioning |
| [../_shared/claim-strength.md](../_shared/claim-strength.md) | Calibrating verbs, novelty, robustness, generalization, or causal language |
| [../_shared/ai-assisted-writing-policy.md](../_shared/ai-assisted-writing-policy.md) | AI-assisted prose or venue disclosure risk is relevant |
| [../_shared/list-to-argument.md](../_shared/list-to-argument.md) | Source material is a bullet list, module list, result-row list, or contribution list |
| [../_shared/non-english-source-notes.md](../_shared/non-english-source-notes.md) | Non-English notes must become English manuscript prose |
| [../_shared/output-mode.md](../_shared/output-mode.md) | The user asks for output only |
| [../_shared/sentence-role-and-story-flow.md](../_shared/sentence-role-and-story-flow.md) | Drafting, shortening, or reordering paragraphs where every sentence must justify its role |
| [../_shared/terminology-ledger.md](../_shared/terminology-ledger.md) | A writing task may rename methods, metrics, categories, or baselines |

Open only what the task needs; none of these files is mandatory.
