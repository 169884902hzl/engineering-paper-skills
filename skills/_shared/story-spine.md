# Story Spine

Use this before writing, auditing, shortening, or validating a full paper,
section cluster, abstract, introduction, experiments section, or conclusion.
Top-tier papers are not a collection of correct sentences; they are a dependency
chain from problem to bounded implication.

## Core Spine

```text
problem -> gap -> insight -> method -> evidence -> boundary -> implication
```

Each node must be explicit, supported, and connected to the next node. If a node
is absent, do not write around the gap with smoother prose.

## Story Node Map

```text
Story spine
| Node | Section location | Claim | Upstream basis | Downstream proof | Figure/table | Boundary | If removed, what breaks? |
```

Use this map to prevent these failures:

- Abstract promises a result that Experiments never proves.
- Introduction claims a gap that Related Work does not justify.
- Methods describes modules but never embodies the stated insight.
- Experiments reports numbers but does not prove the contribution.
- Discussion or Conclusion revives a claim that Results did not support.
- Figures decorate the story instead of serving as evidence nodes.

## Complete Claim Inventory

For a full-paper audit, story spine is not complete until every major claim has
been inventoried across sections.

```text
Section claim inventory
| Claim ID | Claim text | First section | Reappears in | Method anchor | Experiment anchor | Figure/table anchor | Citation/source anchor | Boundary anchor | Verdict |
```

Rules:

- If a claim appears in Abstract or Conclusion, it must have at least one method
  or evidence anchor and one boundary anchor.
- If a claim appears only in Discussion or Conclusion, treat it as claim
  resurrection and downgrade, move, or delete it.
- If one contribution depends on another, show the dependency rather than
  listing contributions independently.
- If a paper has multiple contributions, make one row per contribution and one
  row per required evidence path.

## Section Dependency Checks

| Section | Must depend on | Must support |
|---|---|---|
| Abstract | all finished evidence and boundary nodes | reader's first model of the paper |
| Introduction | problem, gap, nearest-neighbor limits | contribution and method route |
| Related Work | cited or provided source groups | gap and distinction |
| Methods | contribution and insight | experiment interpretation |
| Experiments | method claims, protocol, metrics | contribution strength and boundary |
| Discussion | results and failure modes | limitation and implication |
| Conclusion | proven contribution only | final bounded takeaway |

## Paragraph-To-Paragraph Flow

For adjacent paragraphs, check:

```text
Transition audit
| From paragraph | To paragraph | Required bridge | Missing or redundant content | Repair |
```

Each paragraph should make the next paragraph necessary. If two paragraphs can
swap positions without damaging the argument, the story chain is probably weak.

## Delete-Damage Test

For each paragraph or figure/table:

1. Delete it mentally.
2. Name the exact claim, evidence, boundary, or transition that breaks.
3. If nothing breaks, delete, merge, or repurpose it.
4. If a misunderstanding appears, add the missing bridge or boundary sentence.

## Output Contract

```text
Story-spine audit
| Node | Present? | Evidence anchor | Break risk | Repair route |

Section dependency audit
| Section | Promise made | Proof location | Boundary location | Status |

Transition audit
| From | To | Bridge needed | Action |
```

## Repair Algorithm

When the spine breaks, repair in this order:

1. Inventory every claim-bearing sentence in Abstract, Introduction,
   Experiments, Discussion, and Conclusion.
2. Assign each claim to one story node.
3. For each node, name the upstream basis and downstream proof.
4. If a claim has no downstream proof, downgrade, move to limitation/future
   work, or delete it.
5. If Methods has modules but no insight-to-mechanism link, rebuild the Methods
   reader path before polishing any prose.
6. If Results reports numbers but does not answer contribution questions, build
   the experiment-question map before drafting interpretation.
7. Recheck Abstract and Conclusion last; they may only state claims that survive
   the story-spine audit.

## Multi-Contribution Check

Use this when a paper has algorithm, system, benchmark, dataset, hardware, or
analysis contributions in the same draft.

```text
Contribution dependency map
| Contribution | Requires method object | Requires experiment | Depends on | Evidence sufficient? | Boundary |
```

Do not let a strong experiment for one contribution carry unsupported claims for
another contribution. A system demo does not prove algorithmic superiority; an
ablation does not prove deployment reliability; a benchmark result does not
prove broad robotics generalization.

## Worked Failure Example

```text
Story spine
| Node | Draft text symptom | Evidence anchor | Verdict | Repair |
| Problem | broad automation importance | one tabletop insertion fixture | too broad | define target visibility loss during insertion |
| Gap | "existing methods remain limited" | no nearest-neighbor distinction | unsupported | group prior routes by fixed-view, active sensing, and guarded execution assumptions |
| Insight | "combine perception, observation, guard, safety" | design notes | module list | state confidence-gated observation as the mechanism |
| Method | four modules listed | no input-output path | weak | write image -> visibility confidence -> view update / action gate |
| Evidence | 86 vs 71 vs 74 | one table | bounded | interpret as success improvement under evaluated condition |
| Boundary | one object family and fixture | notes | missing in Abstract | add boundary to Abstract, Results, Discussion, Conclusion |
| Implication | "industrial reliability" | no deployment evidence | overclaim | replace with narrower implication for tabletop insertion studies |
```

## Section Claim-Strength Diff

Use this when Abstract, Discussion, or Conclusion sounds stronger than Results:

```text
Cross-section claim diff
| Claim | Abstract strength | Intro strength | Results evidence | Discussion/Conclusion strength | Verdict | Safe repair |
```

Block the draft if any untested robustness, generalization, causality, or
deployment claim grows stronger after the Results section.
