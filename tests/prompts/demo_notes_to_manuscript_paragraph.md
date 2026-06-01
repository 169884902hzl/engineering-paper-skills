# Demo Prompt: Notes To Manuscript Paragraph

Use `engineering-writing`.

This prompt is for a user-facing recorded demo. Produce Markdown only. Do not
edit files. Do not invent experiments, citations, baselines, metrics,
statistical results, figures, line numbers, deployment evidence, or novelty.

## Task

Turn the author notes below into one English manuscript paragraph suitable for
an Introduction-to-method summary or early Results framing paragraph in a
robotics conference paper.

The output must include:

1. `Manuscript paragraph`
2. `Why this is evidence-bound`
3. `Claims not supported by the supplied notes`

The paragraph must follow this argument path:

`problem -> prior limitation -> method object -> evidence -> boundary`

## Author notes

Target paper type:
Robotics conference paper.

Problem:
Contact-rich insertion fails when visual occlusion hides the peg-hole alignment
and the controller continues with a poor pose estimate.

Prior limitation:
Fixed overhead or side cameras can lose task-relevant visibility during
insertion. Open-loop insertion does not react to pose uncertainty or contact
deviations.

Method:
The system uses overhead and side RGB-D observations. It estimates insertion
pose and confidence. When confidence is low, it requests an additional view. A
guarded insertion controller stops if force or pose deviation exceeds a limit.

Evidence:
Full system: 84% success over 180 trials.
Fixed overhead camera: 69%.
Fixed side camera: 72%.
Open-loop controller: 61%.

Boundary:
One 7-DoF robot arm.
One tabletop fixture.
One cylindrical peg family.
No confidence intervals.
No statistical significance test.
No cross-robot test.
No industrial deployment test.
No ablation isolating view selection from guarded execution.

## Output constraints

- Write one polished English manuscript paragraph, not a bullet-only audit.
- Use the supplied numbers exactly.
- Mention the boundary in prose.
- Do not claim statistical significance.
- Do not claim robustness beyond the tested setup.
- Do not claim industrial deployment readiness.
- Do not claim the causal effect of view selection because no isolating ablation
  is supplied.
