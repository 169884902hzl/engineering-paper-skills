## Draft

The ablation results show that each major component contributes to a different part of the execution chain. Directly querying action hints reaches only 17% success, indicating that raw image-space reasoning is not sufficient for reliable manipulation in the evaluated task family. Adding geometry-aware execution increases success to 23%, suggesting that better action realization helps, but does not by itself resolve perception and hint-validity errors. Incorporating target-focused perception raises success to 44%, which supports the role of cleaner task-centric observations in action-hint generation. Overlay self-verification further increases success to 76%, consistent with improved stability of the predicted interaction directions. The full system reaches 88% after adding mask-constrained grounding, supporting the interpretation that validity checks on interaction points reduce off-target contacts. These ablations support complementary component roles, but they do not establish a fully isolated causal mechanism or deployment readiness without additional controlled tests.

## Why this works

- Paragraph job: ablation interpretation.
- Claim flow: baseline weakness -> component increments -> mechanism roles -> boundary.
- Why this order: each numeric jump is tied to a component responsibility.

## Evidence used

- Ablation rows: 17%, 23%, 44%, 76%, and 88%.
- Boundary: one task family, no statistical significance test, no deployment evaluation.

## Boundary / do-not-claim

- Do not say the ablation proves a causal mechanism.
- Do not claim deployment readiness.
- Do not generalize beyond the evaluated task family.
