# Paragraph-To-Paragraph Transition Audit

Use this when each paragraph seems reasonable alone but the section still feels
jumpy, repetitive, or hard to follow.

## Audit

```text
Transition audit
| From paragraph | To paragraph | Expected bridge | Missing link | Redundant content | Repair |
```

## Rules

- Each paragraph should make the next paragraph necessary.
- If two paragraphs can swap positions without harming the argument, the story
  is weak.
- If a paragraph starts with a connector but the relation is unclear, replace
  the connector with the actual logical relation.
- If a paragraph repeats the previous paragraph's takeaway, merge or delete.

## Pair-Level Failure Patterns

| Pattern | Symptom | Repair |
|---|---|---|
| Solution before problem | P1 describes modules; P2 explains why fixed perception fails | move problem/gap before method |
| Result before task | P1 reports success rate; P2 defines the task | define task and protocol before numbers |
| Citation list before axis | P1 lists papers; P2 says gap remains | group papers by technical axis first |
| Limitation before evidence | P1 says one fixture only; P2 gives main result | put limitation after the evidence it bounds |
| Connector without relation | P2 starts with "Moreover" but changes topic | name the actual relation or add a bridge |
| Repeated takeaway | P2 restates P1 with different words | merge or delete |

## Worked Pair Audits

```text
Transition audit
| From paragraph | To paragraph | Expected bridge | Missing link | Redundant content | Repair |
| broad automation importance | module list method | problem -> gap -> insight | no concrete failure mode | none | insert visibility-loss gap before method |
| fixed-camera baseline result | no-guarded ablation result | evidence escalation | no experiment question | repeated "better" wording | frame Q1 baseline and Q2 ablation |
| active perception papers | guarded control papers | uncertainty -> execution gate | why active sensing needs guarded execution | citation list cadence | add bridge: when visibility confidence drops, execution must change |
```

## Output Requirement

For any section with three or more paragraphs, report at least one transition
table. If no transition issue exists, state why each adjacent pair is necessary
in the current order.
