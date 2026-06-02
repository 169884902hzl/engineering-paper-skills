# RAL-Style Engineering Paper Drafting Guide

Use this reference when drafting engineering manuscript prose from author notes,
module lists, result tables, ablation rows, or partial section outlines. Learn
section skeletons, paragraph jobs, and evidence connection. Do not copy domain
terms, method names, or claims from any source paper.

## Core Principle

For writing requests, produce manuscript prose first. The prose must still be
evidence-bound, but the user should see a usable paper paragraph before the
structure notes.

Recommended order:

```text
Draft -> Why this works -> Evidence used -> Boundary / do-not-claim
```

## Abstract: Six-Sentence System Template

Use this when the paper is a robotics, control, perception, learning, or systems
paper with a named method and real experiments.

```text
1. [Task] remains challenging because [specific coupled difficulty].
2. Small errors in [operation/perception/planning] can cause [concrete failure].
3. We propose [Method], a [framework/system/representation] for [setting].
4. [Method] first [stage 1], then [stage 2], and finally [stage 3].
5. The resulting [representation/signal/plan] is converted into [executable action/control/policy] through [grounding mechanism].
6. Experiments on [platform/benchmark/dataset] show [headline result], with [comparison, boundary, or remaining limitation].
```

Use a five-sentence abstract when page or word budget is tight:

```text
problem + failure mode -> why existing routes are insufficient -> method core -> evaluation condition -> strongest stable evidence
```

Do not:

- begin with broad field importance
- turn the abstract into a Related Work mini-review
- list every module
- write `significantly improves` without numbers or a supplied statistical basis
- claim deployment, robustness, or generalization beyond the supplied evidence

## Introduction: Layered Problem-To-Formulation Path

Use this when rebuilding an Introduction or writing the opening paragraphs from
notes.

```text
P1. Task and difficulty:
[Task] is important in [domain], but remains difficult because it requires [requirement A] and [requirement B] under [condition].

P2. Core ambiguity or bottleneck:
A central difficulty lies in [ambiguity/occlusion/distribution shift/physical coupling], where [why naive perception, policy, or execution fails].

P3. Existing routes and missing condition:
Existing methods based on [route A] and [route B] address [partial problem], but still assume/require/fail to handle [missing condition].

P4. Why errors matter:
This gap is consequential because small errors in [stage] can [irreversible, costly, unsafe, or hard-to-recover failure].

P5. New formulation:
These observations motivate [new representation/control signal/framework], which [what it changes] before [execution/training/deployment].

P6. Contributions:
We present/formulate/introduce/validate [verifiable contributions].
```

Contribution verbs should be testable. Prefer `formulate`, `introduce`,
`present`, `evaluate`, and `validate under [condition]`. Avoid adjective-only
contributions such as `novel`, `robust`, or `general` without evidence.

## Related Work: Technical Axes, Not Paper Summaries

Group prior work by mechanism or assumption.

```text
[Axis A] methods address [problem] by [typical mechanism]. However, they usually assume/require/omit [limitation]. This leaves [specific gap] unresolved in [our setting].

[Axis B] methods provide [capability], especially for [related task]. Yet these methods do not directly provide [missing representation/control/evidence condition].

Taken together, existing work leaves uncovered the combination of [requirement 1], [requirement 2], and [requirement 3].
```

Do not write a chronological list of one-sentence paper summaries. If citations
are missing or unverified, use placeholders and do not claim that prior work
failed without a source.

## Methods: Reader Path Instead Of Module Directory

The first Methods paragraph should give the reader a data and execution path,
not a list of module names.

```text
Given [input], the system first produces [intermediate representation 1] through [stage 1].
This representation is passed to [stage 2], which [verifies/refines/transforms] it using [evidence source].
The refined representation is grounded into [control signal/executable action/training target] by [stage 3].
This path defines the main parts of the method: [A], [B], and [C].
```

Each Methods subsection should carry one bottleneck:

```text
Opening: [Component] is needed because [specific bottleneck].
Mechanism: It takes [input] and produces [output] by [operation/constraint].
Handoff: The resulting [output] is used by [next component] to [purpose].
Boundary: This component assumes [condition] and does not by itself guarantee [overclaim].
```

Do not start a Methods section with formulas before the object and reader path
are clear.

## Results: Ranking, Numbers, Interpretation, Boundary

Experiments must prove bounded contributions. They are not table narration.

### Main Result

```text
Table [X] summarizes [evaluation scope]. Overall, [method] achieves the best [primary metric], reaching [number] compared with [baseline number] for [baseline].
This improvement is most visible under [hard condition], where [mechanism-relevant factor] affects [signal/decision/action].
The trend is consistent with [bounded mechanism interpretation], but [boundary] remains outside the evaluation.
```

If the result is a difference between percentages, say `percentage points` when
that is what the table shows. For example, write `from 19% to 88%` or `69
percentage points higher`, not just `69% higher`, unless a relative-ratio claim
is intended and supported.

### Ablation

```text
Adding/removing [component] changes [metric] from [a] to [b], mainly affecting [failure mode or capability].
This supports the role of [component] in [contribution], rather than proving [stronger causal claim].
The remaining gap indicates [boundary or residual failure].
```

Do not let ablation become a component inventory. Each row must recover a
contribution or expose a failure mode.

### Robustness And Failure Boundary

```text
Performance changes across [condition axis], indicating that [condition] affects [perception/execution/reasoning] through [specific factor].
The hardest regime is [condition], where [failure mode] remains visible.
This defines the current operating boundary rather than invalidating the main result.
```

Report failure modes in Experiments, Results, or Discussion. Do not hide all
limitations in Conclusion.

## Conclusion: Two Paragraphs

Use two compact paragraphs when the venue allows.

```text
Paragraph 1:
We present [method], which [core mechanism]. On [evaluation scope], it achieves [headline result] compared with [baseline], and ablations show that [component] contributes to [mechanism]. These results support [bounded takeaway].

Paragraph 2:
The method currently assumes [condition]. Performance degrades when [failure regime 1] or [failure regime 2], indicating that [operating envelope]. Future work should address [specific extension derived from the failure].
```

Do not introduce new terms, new results, or broad promises in Conclusion.

## Reusable Sentence Skeletons

```text
[Task] remains challenging because [requirement A] and [requirement B] must be satisfied under [condition].
A central difficulty lies in [bottleneck], where [why existing signal/action is ambiguous].
This motivates [representation/formulation/control signal] that can be [verified/refined/grounded] before [execution].
Given [input], the system first [operation], yielding [intermediate output].
Table [X] summarizes [scope]. Overall, [method] achieves [number] compared with [baseline].
This pattern is consistent with [interpretation], but does not establish [untested stronger claim].
```

## Anti-Patterns

- Abstract starts with generic importance rather than a concrete task.
- Introduction compresses all gaps into one vague paragraph.
- Related Work lists papers one by one without a technical axis.
- Methods opening reads like a module directory.
- Results paragraph reads table cells without interpretation.
- Ablation reports drops but does not explain component responsibility.
- Robustness paragraph says `robust` without naming the stress condition.
- Conclusion revives a claim that Methods or Experiments did not support.
