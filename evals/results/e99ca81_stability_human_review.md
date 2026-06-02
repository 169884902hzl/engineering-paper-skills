# Multi-run Stability Human Review

Base commit: `e99ca8120a6174a9cdba7083bd71f739908c822c`
Evidence type: local three-run samples for three prompt families, not CI-controlled behavior proof.

| prompt family | best | median | worst | failure modes | hallucination check | output variance | stable? |
|---|---|---|---|---|---|---|---|
| results_showcase_v2 | run3 | run1 | run2 | minor differences in opening and boundary density | no unsupported mechanism or forbidden phrase detected | low to moderate | yes, for bounded Results prose |
| ablation_showcase_v2 | run2 | run3 | run1 | run1 is slightly more disclaimer-like at the end | no unsupported mechanism or forbidden phrase detected | low | yes, for contribution-role prose |
| zh_to_en_showcase_v2_rerun | run1 | run2 | run3 | run3 has a heavier final scope sentence; run2 logs a transient TLS handshake error before final output | no forbidden old wording detected | moderate | yes, with local-only caveat |

Conclusion: the three prompt families are stable enough for candidate-level public examples after blocker scanning. This is not enough to call the suite top-tier-ready.
