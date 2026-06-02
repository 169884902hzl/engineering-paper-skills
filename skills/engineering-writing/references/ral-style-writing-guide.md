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

## Showcase-Grade Paragraph Standard

Use this stricter standard for README, demo, recorded-output, or user-facing
examples. A paragraph that is merely safe is not enough.

- It must have a section job that a reader can name after one pass.
- It must contain at least one interpretation sentence that is specific to the
  section: bottleneck for Introduction, handoff rationale for Methods,
  mechanism-level reading for Results, component role for Ablation, or operating
  boundary for robustness.
- It must not be a list of facts joined by connectors.
- It must not spend more space on disclaimers than on the paper claim.
- It must integrate boundaries as scientific scope, not as an apology.
- It must avoid generic sentence frames when a concrete task, failure mode,
  metric, or component role is available.

Weak but safe:

```text
X remains difficult. To address this limitation, we propose Y. The method
achieves Z. These results indicate improvement in the tested setup.
```

Stronger engineering prose:

```text
The experiment isolates where the system gains reliability: execution
constraints alone produce only a small improvement, while target-focused
perception and verification account for the main jumps in success. This pattern
suggests that the bottleneck is not only executing the action, but selecting and
grounding the action before contact.
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

### Introduction Opening: Showcase Pattern

Use this when the user asks for a strong opening, a README demo, or a recorded
writing example.

Paragraph 1 should name the task and the operational bottleneck. It should
explain why the difficulty breaks a perception, planning, control, or execution
loop.

Paragraph 2 should contrast the main existing routes, isolate the missing
condition, and motivate the proposed formulation without listing modules.

Reusable high-density opening:

```text
The difficulty is not simply that [task] requires [capability]; it is that
[failure mode] changes the information available to [downstream stage] exactly
when [execution/recovery] becomes least forgiving.
```

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

### Nearest-Neighbor Distinction

Use this paragraph pattern when the user supplies rough related-work notes but
not verified citations.

```text
The closest prior line shares [surface similarity], but differs in
[assumption/signal/execution loop/evidence condition]. This distinction matters
because [our setting] requires [combination] rather than [prior capability
alone]. With the supplied notes, this should be framed as a bounded positioning
claim until the exact citations and protocols are verified.
```

The paragraph must identify:

- technical axis
- what that axis solves
- what it assumes or omits
- nearest-neighbor similarity
- exact distinction
- gap bridge

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

For a stronger Methods overview, include the reason for the order:

```text
The system estimates [state] before [execution] because [failure mode] would
otherwise propagate into [downstream error]. This handoff makes [component B]
responsible for [role], while [component C] enforces [safety or execution
boundary].
```

Avoid:

```text
The method has three modules: perception, planning, and control.
```

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

A stronger Results paragraph explains the numbers:

```text
Overall, [method] ranks first on [metric], reaching [number] compared with
[baseline number] for [closest baseline]. The gap is largest under [condition],
where [failure mode] makes [baseline assumption] unreliable. This pattern is
consistent with [mechanism], but the evidence remains limited to [scope].
```

If no diagnostic notes are supplied, do not invent them. Instead write:

```text
The supplied results support the ranking but do not explain which failure mode
accounts for the difference; a mechanism-level interpretation would require
[failure breakdown / category results / ablation].
```

### Ablation

```text
Adding/removing [component] changes [metric] from [a] to [b], mainly affecting [failure mode or capability].
This supports the role of [component] in [contribution], rather than proving [stronger causal claim].
The remaining gap indicates [boundary or residual failure].
```

Do not let ablation become a component inventory. Each row must recover a
contribution or expose a failure mode.

Use contribution-level recovery when interpretation notes are supplied:

```text
The ablation separates three responsibilities. [Component A] mainly affects
[failure mode/capability], as shown by [delta]. [Component B] accounts for the
larger jump from [a] to [b], suggesting that [role] is the main bottleneck. The
remaining improvement from [component C] supports [spatial/temporal/semantic]
grounding, but the additive design does not prove an isolated causal mechanism.
```

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

The first paragraph should end with a bounded takeaway sentence when possible:

```text
Taken together, these results support [specific claim], not [stronger untested
claim].
```

## Chinese Notes To English Manuscript Prose

Use this when source notes are Chinese but the final manuscript should be
English.

Do not translate sentence by sentence. First extract:

- task
- bottleneck
- method object
- evidence
- boundary
- target section

Then write native English manuscript prose using the target section skeleton.
Chinese phrasing is source material, not the final sentence order. Preserve
numbers, method facts, and limitations exactly; do not add citations, baselines,
statistics, novelty, or deployment claims.

## Rich Prompt Inputs

Showcase-grade outputs need richer source notes than smoke checks. For public
demos or recorded writing examples, prefer prompts that include:

- section target and desired paragraph count
- task, bottleneck, and why it matters
- method object and information flow
- table numbers or ablation rows
- diagnostic axes or failure modes for Results
- component roles for Ablation
- nearest-neighbor notes for Related Work
- explicit boundaries and forbidden claims

If these inputs are absent, write a bounded draft, but mark that stronger
section-specific interpretation would require diagnostic notes, failure
breakdowns, ablation details, or verified citations.

## Reusable Sentence Skeletons

```text
[Task] remains challenging because [requirement A] and [requirement B] must be satisfied under [condition].
A central difficulty lies in [bottleneck], where [why existing signal/action is ambiguous].
This motivates [representation/formulation/control signal] that can be [verified/refined/grounded] before [execution].
Given [input], the system first [operation], yielding [intermediate output].
Table [X] summarizes [scope]. Overall, [method] achieves [number] compared with [baseline].
This pattern is consistent with [interpretation], but does not establish [untested stronger claim].
```

## Avoid Generic Drafting Patterns

Do not repeat these as default openers when the supplied evidence permits a
more concrete section-specific sentence:

- `X remains challenging/difficult...`
- `To address this limitation...`
- `These results indicate/suggest/support...`
- `The current results remain bounded...`
- `The proposed system achieved...`

Prefer:

- Introduction: `The difficulty is not only [task], but [specific bottleneck that breaks existing route].`
- Methods: `The reader path starts from [input] because [downstream stage] depends on [intermediate state].`
- Results: `The full system ranks first under [evaluation scope], with the clearest gap against [closest baseline].`
- Ablation: `The ablation isolates where the improvement enters the pipeline: [component/role].`
- Related Work: `The nearest prior line shares [feature], but assumes [condition] that this setting violates.`
- Conclusion: `Taken together, the results support [bounded takeaway], not [stronger untested claim].`

## Anti-Patterns

- Abstract starts with generic importance rather than a concrete task.
- Introduction compresses all gaps into one vague paragraph.
- Related Work lists papers one by one without a technical axis.
- Methods opening reads like a module directory.
- Results paragraph reads table cells without interpretation.
- Ablation reports drops but does not explain component responsibility.
- Robustness paragraph says `robust` without naming the stress condition.
- Conclusion revives a claim that Methods or Experiments did not support.
