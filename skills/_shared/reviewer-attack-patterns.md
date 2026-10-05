# Reviewer Attack Patterns

Use this before submission, when planning experiments, and when auditing a
draft. It records what real reviewers and senior co-authors objected to in
engineering and robotics manuscripts, why the authors did not see it coming,
and what to change before a reviewer sees the paper.

Most entries are about evidence design, not prose. In the observed review sets,
reviewers almost never objected to sentence style; they objected to
comparisons, assumptions, cost, and under-specified mechanisms.

## How To Use

1. Read the manuscript as a skeptical reviewer from the closest neighboring
   field, not as the author. Ask what that reviewer would compare the work
   against: the simplest alternative configuration, the principled method
   from the adjacent field, and a baseline given the same capability or prior.
2. Use the patterns below as prompts, not as the list of allowed findings.
   Report any problem the manuscript gives evidence for, whether or not a
   pattern names it (data leakage, wrong statistical unit, misdescribed prior
   work, a contribution that does not hold). Skip patterns that are not
   triggered.
3. For each finding, name the exact trigger (a phrase, table, or design
   choice), how a reviewer would phrase the objection, and the cheapest
   pre-submission fix: an added control, a measurement, a paragraph, or a
   wording change.
4. Rank by consequence: would this change the conclusion, the fairness of the
   comparison, or reproducibility? Put the three objections most likely to
   appear in an actual report first. A numeric error that changes a headline
   number or comparison ranks with the major objections. List only
   non-substantive slips (a typo, a duplicate label that resolves correctly,
   formatting) separately as mechanical issues.

Evidence tags: `review N/2` = raised in N of the two real review sets studied;
`senior` = raised in a senior co-author's comments on a student draft;
`literature` = reported in the published sources listed at the end.

## P1. Handicapped Baseline

- Trigger: the baselines lack a capability, resource, or prior that the
  proposed method has, and the paper uses the comparison as evidence for its
  mechanism. Observed shapes: a passive configuration compared against an
  active one without giving it any simple form of adaptation; a method built
  on a large pretrained model compared against policies trained from scratch
  on far fewer demonstrations than such policies normally need.
- How it is raised: the comparison is called unfair and said to exaggerate the
  advantage; the reviewer asks whether the gain comes from the proposed design
  or from the stronger starting point.
- Why it is missed: the numbers are honest, so the author sees no problem; the
  baselines were chosen because they were available, not because they isolate
  the contribution.
- Separate two claims. A system-level claim ("our system outperforms the
  common configuration") may compare against a baseline without the
  capability, provided every difference is disclosed. A mechanism-level claim
  ("the proposed loop is what helps") needs a matched control. Reviewers
  still asked for the matched control when the capability itself was the
  contribution, so plan for it.
- Before submission: add a matched control that has the same capability or
  prior but lacks the proposed mechanism (for a foundation-model pipeline: the
  same model prompted directly, without the proposed loop; for an active
  system: the baseline with the simplest available form of the capability).
  If such a control already exists in the ablation, move it next to the
  headline result and say what it isolates. Give learned baselines a
  defensible data budget, or state why it was limited.
- In the manuscript: write what each baseline isolates ("differs only in X,
  which tests Y"). Do not call a comparison "fair" unless the resources that
  matter for the claim are matched.
- Evidence: `review 2/2`; `literature` [1, 2].

## P2. Unstated Operating Assumption

- Trigger: the method only works while some condition holds (two objects in
  one view, a detectable target, a reachable pose, a valid intermediate
  estimate), and the paper does not say how often it holds or what happens
  when it fails.
- How it is raised: the reviewer describes concrete situations in which the
  condition breaks and asks how the method can still be robust, sometimes
  asking for a theoretical guarantee.
- Why it is missed: the experiments were designed inside the condition, so
  failures outside it never appear in the data.
- Before submission: list the assumptions. For each, report how often it held,
  how the system detects violation, and what it does then (pause, recover,
  stop). Do not promise guarantees the method does not have.
- In the manuscript: one explicit operating-envelope paragraph or table and a
  failure-handling path in Methods, written as scope rather than apology.
- Evidence: `review 1/2`.

## P3. Unmeasured Internal Component

- Trigger: the method relies on an internal component (a verifier, a mask, an
  estimator, a confidence score) whose accuracy is never measured on its own,
  especially when the same model produces a result and also checks it.
- How it is raised: the reviewer asks whether the check itself is accurate,
  since a check produced by the same model may simply confirm its own output.
- Before submission: measure the component against ground truth (accuracy,
  false accept and false reject rates), and report how often it changes the
  outcome for better and for worse.
- Evidence: `review 1/2`.

## P4. Added Cost Versus A Simpler Alternative

- Trigger: the system adds hardware, sensors, actuators, model calls,
  iterations, or setup complexity, and the paper neither reports the cost nor
  compares against the simplest configuration that might already reduce the
  problem.
- How it is raised: the added hardware is said to increase complexity and
  cost, with a cheaper configuration (a better-placed sensor, an extra degree
  of freedom on the existing platform) proposed as an alternative; or the
  reviewer counts the model calls per action and asks for time and cost per
  action, because they decide whether the system is practical.
- Why it is missed: the author built the system around the added component and
  never treats "do less" as a baseline.
- Before submission: report time per action, calls or iterations per action,
  and hardware or compute cost next to success. Name the simplest alternative
  and either test it or argue with a number why it is insufficient.
- In the manuscript: watch single words that imply cost. Calling a reused
  component "dedicated" or "additional" invites a cost objection even when no
  hardware was added.
- Evidence: `review 2/2`.

## P5. Under-Specified Or Heuristic Decision Rule

- Trigger: a step selects or adjusts something (a view, a corrected point, a
  direction, a score) without saying how, or uses fixed weights and hand-tuned
  thresholds without separating that step from the main mechanism.
- How it is raised: the reviewer asks how the adjustment is computed, or argues
  that the heuristic cannot be relied on in harder scenes and points to more
  principled methods in the neighboring field (information-theoretic or
  optimization-based).
- Why it is missed: the author knows which part is core and which is fallback;
  the reader does not, and judges the method by its weakest visible part.
- Before submission: write every decision rule as inputs, rule, output. Mark
  heuristics as heuristics, say why they suffice in the evaluated setting, and
  cite the principled alternative.
- In the manuscript: give the main mechanism and any fallback separate
  headings or an explicit "primary strategy versus recovery mechanism"
  sentence.
- Evidence: `review 2/2`.

## P6. Unquantified Practical Factors

- Trigger: deployment-relevant quantities are mentioned but not measured or
  bounded: calibration error, or timing mismatch between cooperating
  subsystems.
- How it is raised: the reviewer asks to quantify the named error and to
  discuss what happens when the subsystems do not keep pace with each other.
- Before submission: measure or bound each named error source and describe
  the behavior under timing mismatch.
- Evidence: `review 1/2`.

## P7. Mechanical Errors Reviewers Notice

- Trigger: text cites the wrong table or figure, floats are numbered out of
  order, labels are duplicated, or person and voice are inconsistent.
- How it is raised: a minor comment pointing at the wrong table number, or a
  request to number tables in the order they appear.
- Before submission: after the final layout, check that each float is first
  referenced in numeric order and that every reference resolves to the
  intended float.
- Evidence: `review 2/2`.

## P8. Results Reported Without Discussion

- Trigger: the experiments section reads like a report: setup text is longer
  than the discussion, numbers appear without interpretation, or only pooled
  averages are given.
- Before submission: move parameters into a setup table and report every
  category, not only the mean. Interpret each result with the mechanism the
  author's evidence supports (diagnostic measurements, per-category results,
  qualitative examples). Where the mechanism is not measured, present it as
  an interpretation ("is consistent with") rather than a cause, and remember
  that cumulative ablations depend on the order of addition.
- Evidence: `senior`.

## P9. Figures And Tables That Do Not Earn Their Space

- Trigger: a figure and a table serve the same function for the reader; colors
  carry no meaning; one table mixes comparisons that are easier to read apart.
- Before submission: give each float one job. Showing the same data as a trend
  and as exact values is fine; showing it twice for the same purpose is not.
  Make colors semantic (for example success versus failure). Split the main
  comparison and the ablation when combining them makes either harder to
  read.
- Evidence: `senior`.

## Calibration Notes

- Reviewers in both sets called the work novel or interesting and still raised
  P1-P5. Novelty and clear figures do not protect against evidence-design
  objections.
- Reviewers did not object to conventional result wording when the evidence
  behind it was visible; they objected when the comparison behind the claim
  was unfair. Fix the comparison, and match the wording to the evidence that
  exists now.
- Test of an earlier version of this file: two papers with real reviews; for
  each paper, a pattern file built only from the other paper's reviews; Claude
  and Codex; one run per condition; blind scoring against the real reviews.
  Recall changed by at most one point. The first objection of the first
  reviewer moved to rank 1 in three of four runs (from ranks 2-7 without a
  pattern file); in one run another major objection dropped from rank 4 to 8.
  P2 and P6 were not part of the held-out files, and no run found the timing
  question (P6). This is a small, single-run test; read it as a hint that the
  file mainly helps ranking, not as proof.
- Comparisons must be feasible: reviewer guidance for robotics journals warns
  against demanding baselines that need unreasonable re-implementation [3].
  Prefer one matched control over many weak baselines. Reviewer guidelines
  also reward being explicit about limitations [4]; an operating-envelope
  paragraph (P2) costs little.

## Output Shape

```text
Reviewer simulation
| Rank | Pattern or issue | Trigger in manuscript | Objection as a reviewer would write it | Cheapest fix before submission |

Mechanical issues: [non-substantive slips: typos, labels that resolve correctly, formatting]
Not triggered: [pattern ids]
Needs author input: [facts the manuscript does not state]
```

## Sources

1. Analysis of weaknesses in ICLR 2024-2025 reviews, arXiv:2511.15462
   (insufficient or weak baselines and missing ablations among the most
   common experiment criticisms; weaknesses labeled with an LLM).
2. A. Billard et al., "Surviving the Paper Deluge," IEEE RAS:
   https://www.ieee-ras.org/wp-content/uploads/2026/05/Surviving-the-Paper-Deluge.pdf
   (many robotics papers revisit solved problems without comparison to
   previous solutions).
3. P. Robuffo Giordano, "How to review a scientific paper," IEEE T-RO:
   https://www.ieee-ras.org/images/publications/t-ro/HowToReviewAScientificPaper.pdf
4. NeurIPS 2025 Reviewer Guidelines:
   https://neurips.cc/Conferences/2025/ReviewerGuidelines
