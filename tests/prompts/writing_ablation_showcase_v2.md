# Ablation Showcase V2 Prompt

Use $engineering-writing to draft a showcase-grade Ablation paragraph.

Target section:
Ablation.

Paper type:
Robotics / engineering conference paper.

Task:
Suction-cup bin picking of transparent and reflective parts.

Core bottleneck:
Identify the main bottleneck and recover contribution roles from the deltas.
The paragraph should explain where the largest improvement enters the pipeline.

Method:
A staged picking pipeline that adds seal-pressure retry, depth completion,
collision-aware candidate re-ranking, and a surface-normal consistency filter.

Evidence:

- Depth-only grasp planner: 21% success.
- + Seal-pressure retry: 34% success.
- + Depth completion and seal-pressure retry: 52% success.
- + Depth completion, collision-aware candidate re-ranking, and seal-pressure
  retry: 69% success.
- Full system with surface-normal consistency filter: 81% success.
- Seal-pressure retry mainly recovers picks that lose vacuum after contact but
  cannot choose a better grasp point by itself.
- Depth completion restores missing depth on transparent and reflective
  surfaces.
- Collision-aware re-ranking rejects candidates whose approach path would hit
  neighboring parts.
- The surface-normal consistency filter removes grasp points on curved edges
  where the cup cannot seal.

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
