# Stage Playbook

Use this in guide mode. `SKILL.md` says when guide mode applies and names the
deliverable for each stage; this file holds the detail.

## Read Before Asking

Read a repo or folder in this order:

1. README, notes, plans, and lab logs (`.md`, `.txt`, notes in any language).
2. Result files: CSV, JSON, training or evaluation logs, figure folders.
   Summarize large logs; do not paste them.
3. Manuscript sources: `.tex`, `.bib`, a compiled PDF, or a document the user
   names.
4. Reviewer or editor comments and decision letters.

Rules:

- Read only. In guide mode, do not run experiments, training, or builds, and
  do not edit the user's files unless asked.
- A config file, script, or plan is not a result. A result is a logged number
  or a figure made from logged data. Planned runs stay planned.
- Name the paths you actually read in one line, so the user can correct the
  stage if something was missed.
- Notes in Chinese or any other language are source material. Use them
  directly; do not ask the user to translate them.

## Detect The Stage

| Stage | Signals in the materials |
|---|---|
| S4 | Reviewer or editor comments, a decision letter, a rebuttal draft |
| S3 | A manuscript with every main section drafted, even if rough |
| S2 | Logged numbers for the main comparison, but no full draft |
| S1 | An idea plus planned, running, or partial experiments; result tables with empty cells |
| S0 | An idea, a problem, or a method sketch, and no experiment yet |

- When materials span stages, work at the most advanced stage, but first
  repair an earlier deliverable whose absence would change the plan. A full
  draft with no clear one-sentence contribution gets that sentence first, in a
  few lines.
- A draft whose main table still has empty cells is S1 for the experiments and
  S3 for the prose. Say which part is which.
- If the user names the stage ("I have a draft"), trust it unless the files
  contradict it, and say so if they do.

## Questions

Ask at most three, in plain words, after the deliverable. Ask only for facts
that change the plan:

- Target venue and deadline: they set the page budget and how many
  experiments fit before submission.
- Which runs are finished and which are planned: this decides S1 versus S2.
- What the method is compared against now: this decides the result table.

Do not ask for what the files already show, for style preferences, or for
facts that only a later stage needs.

## S0. Idea Only

Deliverable: one sentence with five slots.

```text
For [task], existing approaches fail when [gap]; we [mechanism], and we
will show [evidence still needed] under [scope].
```

- Fill the slots from what the user said. Mark empty slots `[?]`.
- "Evidence still needed" names the measurement that would convince a
  skeptical reader, for example "higher success than the same system without
  the proposed step, on held-out objects". It is a plan, not a claim.
- Scope is a concrete operating condition: one robot, one object family,
  simulation only.
- Add one sentence on the simplest alternative a reviewer would compare the
  idea against (P1 and P4 in
  [reviewer-attack-patterns.md](../../_shared/reviewer-attack-patterns.md)).
- Move to S1 when every slot is filled or knowingly left open.

## S1. Experiments Planned Or Running

Deliverables: a result-table skeleton, the list of missing experiments, and
an experiment pre-mortem.

```text
| Row (what it isolates)                     | Condition A     | Condition B | Category 1 |
|--------------------------------------------|-----------------|-------------|------------|
| Proposed method                            | [RESULT NEEDED] |             |            |
| Baseline: [named by the user]              |                 |             |            |
| Matched control: proposed minus [key idea] |                 |             |            |
| Ablation: proposed minus [component]       |                 |             |            |
```

- Rows: the proposed method, the baselines the user names, a matched control
  (same capability or prior, proposed mechanism removed; P1), and ablations.
  Columns: test conditions or object and task categories, so per-category
  behavior is visible instead of only an average.
- Rows the user did not name are proposals. Describe each by what it
  isolates, and ask the user for the concrete method and citation. Never name
  a published method the user did not supply, and never fill a cell without a
  logged number.
- Trials per cell follow the evaluation unit, the expected variability, and
  the uncertainty the claim needs, not the table layout
  ([writing-process.md](../../_shared/writing-process.md)).
- Missing experiments are the empty cells plus anything the pre-mortem adds,
  such as a check of the operating assumption (P2), a measurement of an
  internal component (P3), or the cost against a simpler alternative (P4).
- Pre-mortem: follow
  [experiment-premortem.md](../../_shared/experiment-premortem.md). Its
  purpose is to find the objections an experiment can still fix, before the
  experiment runs. In guide mode, show its ranked cheapest additions and the
  claims to narrow; give the full pre-mortem table when the user asks.
- Move to S2 when the main comparison has logged numbers.

## S2. Results In Hand

Deliverables, in this order:

1. Outline with page budget. Ask for the venue page limit or a link to the
   official call for papers; do not state venue rules from memory. Fill each
   section with placeholder blocks of the intended length. Methods and
   Experiments get most of the space.
2. Figure and table plan: the main results table, the ablation table, a
   framework figure that doubles as a reading guide for Methods, a light
   teaser figure that contrasts the naive and the proposed approach, and
   qualitative examples chosen by a stated criterion, including observed
   failures. Give each one sentence on the claim it supports. Route detail to
   `engineering-figure-table`.
3. Sections in the order Methods, Experiments, Introduction, Abstract. Write
   Related Work once Methods and Experiments are stable, and the Conclusion
   with the Abstract. Route drafting to `engineering-writing`, one section per
   turn unless the user asks for more.

- The Abstract and Conclusion claim only what filled cells support. Empty
  cells stay `[RESULT NEEDED]`.
- Move to S3 when every main section exists in draft.

## S3. Full Draft

Deliverables:

1. Reviewer simulation with `engineering-paper-auditor`: the three objections
   most likely to appear in a real report, each with the cheapest fix before
   submission.
2. Mechanical checks:
   [skills/engineering-validation/scripts/paper_check.py](../../engineering-validation/scripts/paper_check.py)
   runs LaTeX consistency checks. Read its own usage text before running it,
   and report exactly what it printed. For builds, citations, page counts, and
   readiness, use `engineering-validation`.
3. Revision plan in the order of
   [revision-moves.md](../../_shared/revision-moves.md): argument, evidence
   design, section moves, sentences, then mechanical fixes.

- Readiness stays `NOT_READY` or `CANNOT_DETERMINE` until build logs and
  sources have been inspected. Submission is the author's decision; the coach
  does not declare a paper ready.

## S4. Reviews Received

Deliverable: a comment-by-comment revision plan and response letter through
`engineering-response`.

- Separate misreadings, fixed in the manuscript framing, from real gaps, which
  need a control, a measurement, or an explicit limitation.
- The response letter claims only edits and experiments that exist in the
  revised manuscript.

## Plain Words For Common Terms

Explain a term the first time it appears in a reply, in the user's language.

| Term | Plain words |
|---|---|
| baseline | the method you compare against |
| matched control | your system with only the key idea removed, so the comparison isolates that idea |
| ablation | removing one part of the method to see what it contributes |
| contribution | the one thing the paper adds that others can use or test |
| operating assumption | a condition the method needs in order to work, such as the target being visible |
| pre-mortem | listing how the experiment or paper could fail, while there is still time to fix it |
| page budget | how many pages each section gets, decided before writing |
| reviewer simulation | reading the draft as a skeptical reviewer would, to find objections first |
| overclaim | a sentence that says more than the results show |

## Reply Ending

```text
Produced: a one-sentence contribution with two open slots ([gap], [scope]).
Next: a result table that would test it.
Bring: the methods you can run and the test conditions you have.
```

In Chinese, the labels are 本轮产出, 下一步, and 请准备.
