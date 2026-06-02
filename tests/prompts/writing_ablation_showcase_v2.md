# Ablation Showcase V2 Prompt

Use $engineering-writing to draft a showcase-grade Ablation paragraph.

Target section:
Ablation.

Paper type:
Robotics / engineering conference paper.

Task:
Contact-rich action grounding for visually ambiguous insertion targets.

Core bottleneck:
Identify the main bottleneck and recover contribution roles from the deltas.
The paragraph should explain where the largest improvement enters the pipeline.

Method:
A staged action-grounding pipeline that adds geometry-aware execution,
target-focused perception, overlay self-verification, and mask-constrained
grounding.

Evidence:

- Naive direct action hint: 17% success.
- + Geometry-aware execution: 23% success.
- + Target-focused perception and geometry-aware execution: 44% success.
- + Target-focused perception, overlay self-verification, and geometry-aware
  execution: 76% success.
- Full system with mask-constrained grounding: 88% success.
- Geometry-aware execution mainly improves action realization but cannot choose
  the correct target by itself.
- Target-focused perception reduces scene-level ambiguity.
- Overlay self-verification rejects visually plausible but poorly grounded
  action hints.
- Mask-constrained grounding reduces spatial ambiguity near the target.

Boundary:

- One task family.
- Additive rows, not a fully isolated factorial design.
- No statistical significance test.
- No isolated component swaps.
- No deployment evaluation.

Forbidden claims:

- Do not claim independent causal proof.
- Do not claim statistical significance.
- Do not claim broad robustness.
- Do not claim deployment readiness.

Style requirements:

- Produce manuscript prose first.
- Use component delta -> failure mode or capability -> contribution role ->
  scientific scope.
- Identify the main bottleneck.
- Use contribution-level language, not a component inventory.
- Avoid generic `improves performance` wording when a concrete role is supplied.
- The final draft should sound like manuscript prose, not audit prose.
