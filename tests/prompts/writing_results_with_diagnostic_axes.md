# Results With Diagnostic Axes Prompt

Use $engineering-writing to draft one Results paragraph.

This is a showcase-grade WRITE request. Produce manuscript prose first. Write
one complete engineering-paper Results paragraph.

Experiment question:
Does confidence-triggered view acquisition improve insertion success over
fixed-view and open-loop variants in the tested tabletop occlusion setup?

Results:

- Full system: 84% success over 180 trials.
- Fixed overhead camera: 69%.
- Fixed side camera: 72%.
- Open-loop controller: 61%.

Diagnostic notes:

- Fixed overhead failures mostly occur after the peg occludes the hole during
  the final approach.
- Fixed side camera improves lateral visibility but still fails when depth
  uncertainty dominates.
- Open-loop failures are mainly unrecovered pose errors after contact begins.
- The full system still fails when all views are ambiguous or when contact
  causes large pose deviation.

Boundary:
One 7-DoF robot arm, one tabletop fixture, one cylindrical peg family, no
confidence intervals, no statistical significance test, no cross-robot test, no
industrial deployment test, no ablation isolating view selection from guarded
execution.

Requirements:

- Use the sequence: ranking -> strongest number -> diagnostic interpretation ->
  operating boundary.
- Mention percentage points correctly.
- Do not claim statistical significance, causal isolation, cross-robot
  robustness, industrial deployment readiness, or broad generalization.
- Do not merely read the table.
