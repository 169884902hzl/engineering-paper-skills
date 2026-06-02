# Results Showcase V2 Prompt

Use $engineering-writing to draft a showcase-grade Results paragraph.

Target section:
Results.

Paper type:
Robotics / engineering conference paper.

Task:
Contact-rich peg insertion under partial visual occlusion.

Core bottleneck:
The ranking should explain how visibility loss, depth uncertainty, and
unrecovered contact pose error determine the outcome. Do not merely read the
table.

Method:
Confidence-triggered multi-view insertion estimates insertion pose and
confidence from overhead and side RGB-D observations. Low confidence triggers an
additional view before guarded contact execution.

Evidence:

- Full system: 84% success over 180 trials.
- Fixed overhead camera: 69% success.
- Fixed side camera: 72% success.
- Open-loop controller: 61% success.
- Diagnostic axis 1: fixed overhead fails when the peg occludes the hole during
  final approach.
- Diagnostic axis 2: fixed side viewing improves lateral visibility but leaves
  unresolved depth uncertainty.
- Diagnostic axis 3: open-loop execution mainly carries pose errors into
  contact without recovery.
- Remaining failures: all available views ambiguous, or contact produces large
  pose deviation.

Boundary:

- One 7-DoF robot arm.
- One tabletop fixture.
- One cylindrical peg family.
- No confidence intervals.
- No statistical significance test.
- No cross-robot test.
- No industrial deployment test.
- No ablation isolating view selection from guarded execution.

Forbidden claims:

- Do not claim statistical significance.
- Do not claim component-level causal isolation.
- Do not claim cross-robot robustness.
- Do not claim industrial deployment readiness.
- Do not claim broad generalization.

Style requirements:

- Produce manuscript prose first.
- Use ranking -> key number -> diagnostic interpretation -> scientific scope.
- Use percentage points correctly.
- Explain why the ranking occurs through the diagnostic axes.
- Avoid table reading.
- Avoid generic frames such as `These results indicate` unless the sentence
  names a concrete mechanism.
- The final draft should sound like manuscript prose, not audit prose.
