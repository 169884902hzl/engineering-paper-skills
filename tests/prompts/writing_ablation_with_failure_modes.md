# Ablation With Failure Modes Prompt

Use $engineering-writing to draft one ablation paragraph.

This is a showcase-grade WRITE request. Produce manuscript prose first. Write
one complete ablation paragraph, not a component list.

Ablation rows:

- Depth-only grasp planner: 21% success.
- + Seal-pressure retry: 34%.
- + Depth completion and seal-pressure retry: 52%.
- + Depth completion, collision-aware candidate re-ranking, and seal-pressure
  retry: 69%.
- Full system with surface-normal consistency filter: 81%.

Interpretation notes:

- Seal-pressure retry mainly recovers picks that lose vacuum after contact but
  cannot choose a better grasp point by itself.
- Depth completion restores missing depth on transparent and reflective
  surfaces.
- Collision-aware re-ranking rejects candidates whose approach path would hit
  neighboring parts.
- The surface-normal consistency filter removes grasp points on curved edges
  where the cup cannot seal.
- The ablation is additive, not a fully isolated factorial design.

Boundary:
One task family, no statistical significance test, no isolated component swaps,
no deployment evaluation.

Requirements:

- Use component delta -> failure mode/capability -> contribution role ->
  do-not-claim.
- Identify where the largest improvement enters the pipeline.
- Do not claim causal proof, broad robustness, deployment readiness, or
  statistical significance.
