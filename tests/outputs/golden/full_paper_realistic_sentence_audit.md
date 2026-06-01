# Full-Paper Realistic Sentence Audit

This artifact is a sentence-level gold reference for
`tests/fixtures/full_paper/robot_active_observation_realistic_8page.md`.
It does not replace a full human markup, but it records the minimum decisions a
model output must preserve when auditing sentence necessity, placement,
claim-strength, and evidence boundary.

## Abstract Sentence Audit

| SID | Sentence job | Evidence anchor | Issue | Decision | Safe rewrite requirement |
|---|---|---|---|---|---|
| ABS-1 | Context/problem | one insertion task, one tabletop fixture | industrial workcell scope is broader than evidence | rewrite | name visibility-loss insertion, not broad industrial automation |
| ABS-2 | Gap | placeholder Related Work only | prior-work weakness is unverified | scaffold | avoid claiming all fixed-camera methods fail generally |
| ABS-3 | Method object | visibility-confidence state and guarded execution | `reason about where to look` overstates predefined view policy | rewrite | define confidence-gated view update/action gate |
| ABS-4 | Evidence | 84 percent vs 69/72/76/77/61 in one protocol | reliable, robust, causal, and scalable language exceeds evidence | downgrade | report bounded success-rate comparison |
| ABS-5 | Implication | no deployment, no cross-robot, no cross-fixture evidence | industrial deployment implication unsupported | delete or move to future work | state only evaluated-scope implication |

## Results Sentence Audit

| SID | Sentence job | Evidence anchor | Issue | Decision | Safe rewrite requirement |
|---|---|---|---|---|---|
| RES-1 | Experiment question | Table 1 | safe if it asks a bounded question | keep | state evaluated protocol |
| RES-2 | Numeric evidence | Table 1 | safe if counts and denominator are preserved | keep | preserve 84/69/72/76/77/61 values |
| RES-3 | Component interpretation | no-view and no-gate variants | `prove` would be too strong | hedge | use `consistent with` or `supports` |
| RES-4 | Reflective-surface observation | full-system-only 18/30 | no baseline or statistics | boundary | present as failure/stress observation |
| RES-5 | Takeaway | one robot/fixture/object family | cannot generalize | rewrite | close with bounded interpretation |

## Conclusion Sentence Audit

| SID | Sentence job | Evidence anchor | Issue | Decision | Safe rewrite requirement |
|---|---|---|---|---|---|
| CON-1 | Restate contribution | visibility-confidence state | `robust and general framework` revives unsupported title claim | rewrite | state bounded active-observation system |
| CON-2 | Mechanism summary | method state machine | `reasons about visibility` too broad unless defined | rewrite | describe confidence-gated view update/action gate |
| CON-3 | Evidence summary | Table 1 | causal proof unsupported | downgrade | say results support component contribution |
| CON-4 | Final implication | no deployment evidence | scalable industrial path unsupported | delete or future work | end with evaluated-scope boundary |

## Response Sentence Audit

| SID | Sentence job | Evidence anchor | Issue | Decision | Safe response requirement |
|---|---|---|---|---|---|
| RSP-1 | Opening politeness | reviewer comments | safe but empty alone | keep short | do not use thanks to hide unresolved work |
| RSP-2 | Completed changes | no stress-test artifact, empty Table 3 | false completion claim | block | mark as planned or needs data |
| RSP-3 | Method clarification | no final diff supplied | cannot cite exact lines | block final lines | use section placeholder until build/diff |
| RSP-4 | Figure caption change | figure workflow only | cannot validate robust execution | rewrite | say caption now describes workflow only |
| RSP-5 | Readiness claim | no build, citation, venue, diff checks | false readiness | block | mark `CANNOT_DETERMINE` |

## Required Model Behavior

- Do not accept any sentence that upgrades one-fixture evidence into industrial
  robustness, generality, or deployment readiness.
- Do not accept any response sentence that claims completed experiments, tables,
  citations, final line numbers, or readiness without supplied evidence.
- For every claim-bearing sentence, require an evidence anchor or downgrade the
  sentence.
- For every concluding sentence, check whether it revives a claim removed from
  the Abstract or Results.
