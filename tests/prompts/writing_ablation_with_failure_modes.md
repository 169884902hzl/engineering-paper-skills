# Ablation With Failure Modes Prompt

Use $engineering-writing to draft one ablation paragraph.

This is a showcase-grade WRITE request. Produce manuscript prose first. Write
one complete ablation paragraph, not a component list.

Ablation rows:

- Naive direct action hint: 17% success.
- + Geometry-aware execution: 23%.
- + Target-focused perception and geometry-aware execution: 44%.
- + Target-focused perception, overlay self-verification, and geometry-aware
  execution: 76%.
- Full system with mask-constrained grounding: 88%.

Interpretation notes:

- Geometry-aware execution mainly improves action realization but cannot choose
  the correct target by itself.
- Target-focused perception reduces scene-level ambiguity.
- Overlay self-verification rejects visually plausible but poorly grounded
  action hints.
- Mask-constrained grounding reduces spatial ambiguity near the target.
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
