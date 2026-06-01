# Paragraph-To-Paragraph Transition Audit

Use this when each paragraph seems reasonable alone but the section still feels
jumpy, repetitive, or hard to follow.

## Audit

```text
Transition audit
| From paragraph | To paragraph | Expected bridge | Missing link | Terminology drift | Claim-strength drift | Redundant content | Repair |
```

## Rules

- Each paragraph should make the next paragraph necessary.
- If two paragraphs can swap positions without harming the argument, the story
  is weak.
- If a paragraph starts with a connector but the relation is unclear, replace
  the connector with the actual logical relation.
- If a paragraph repeats the previous paragraph's takeaway, merge or delete.
- If a key object changes names across adjacent paragraphs, add a terminology
  drift row before polishing.
- If a bounded claim in one paragraph becomes a broad claim in the next, add an
  adjacent claim-strength drift row and downgrade the later paragraph.
- If a paragraph claims an experiment, table, figure, or citation that the
  previous paragraph only framed as planned or missing, mark the pair as a
  false escalation.

## Pair-Level Failure Patterns

| Pattern | Symptom | Repair |
|---|---|---|
| Solution before problem | P1 describes modules; P2 explains why fixed perception fails | move problem/gap before method |
| Result before task | P1 reports success rate; P2 defines the task | define task and protocol before numbers |
| Citation list before axis | P1 lists papers; P2 says gap remains | group papers by technical axis first |
| Limitation before evidence | P1 says one fixture only; P2 gives main result | put limitation after the evidence it bounds |
| Connector without relation | P2 starts with "Moreover" but changes topic | name the actual relation or add a bridge |
| Repeated takeaway | P2 restates P1 with different words | merge or delete |
| Terminology drift | P1 calls the mechanism `visibility-confidence state`; P2 calls it `active reasoning framework` | choose one term or define the relation |
| Adjacent claim-strength drift | P1 says one tabletop fixture; P2 says industrial robustness | carry the boundary forward or downgrade P2 |
| False evidence escalation | P1 says stress tests are planned; P2 says stress tests validate robustness | keep planned status or add actual evidence |

## Worked Pair Audits

```text
Transition audit
| From paragraph | To paragraph | Expected bridge | Missing link | Redundant content | Repair |
| broad automation importance | module list method | problem -> gap -> insight | no concrete failure mode | none | broad importance becomes broad solution | none | insert visibility-loss gap before method |
| fixed-camera baseline result | no-guarded ablation result | evidence escalation | no experiment question | metric names stable | repeated "better" wording | repeated "better" wording | frame Q1 baseline and Q2 ablation |
| active perception papers | guarded control papers | uncertainty -> execution gate | why active sensing needs guarded execution | active perception vs active reasoning | bounded survey becomes robust solution | citation list cadence | add bridge: when visibility confidence drops, execution must change |
| one-fixture limitation | industrial deployment conclusion | boundary -> implication | boundary not carried forward | fixture vs workcell | bounded result becomes deployment readiness | none | rewrite conclusion around evaluated setting |
```

## Output Requirement

For any section with three or more paragraphs, report at least one transition
table. If no transition issue exists, state why each adjacent pair is necessary
in the current order.
