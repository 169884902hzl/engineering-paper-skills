## Draft

The ablation results show that each major component addresses a different failure source in suction picking of transparent and reflective parts. The depth-only grasp planner reaches only 21% success, indicating that raw depth is not a reliable basis for choosing suction points on these surfaces in the evaluated task family. Adding seal-pressure retry increases success to 34%, suggesting that recovering picks that lose vacuum helps, but does not by itself correct poorly chosen grasp points. Incorporating depth completion raises success to 52%, the largest single increase at 18 percentage points, which supports the role of recovered surface geometry in candidate generation. Collision-aware candidate re-ranking adds a comparable 17 percentage points, reaching 69%, consistent with fewer approach paths that disturb neighboring parts. The full system reaches 81% after adding the surface-normal consistency filter, supporting the interpretation that rejecting grasp points where the cup cannot seal removes part of the remaining failures. These ablations support complementary component roles, but they do not establish a fully isolated causal mechanism or deployment readiness without additional controlled tests.

## Why this works

- Paragraph job: ablation interpretation.
- Claim flow: baseline weakness -> component increments -> mechanism roles -> boundary.
- Why this order: each numeric jump is tied to a component responsibility.

## Evidence used

- Ablation rows: 21%, 34%, 52%, 69%, and 81%.
- Boundary: one task family, no statistical significance test, no deployment evaluation.

## Boundary / do-not-claim

- Do not say the ablation proves a causal mechanism.
- Do not claim deployment readiness.
- Do not generalize beyond the evaluated task family.
