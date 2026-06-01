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
