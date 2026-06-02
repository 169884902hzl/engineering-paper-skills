# Full Section Results Demo Prompt

Use $engineering-writing to draft a compact mini Results section.

Paper type:
Robotics / engineering conference paper.

Task:
Contact-rich peg insertion under partial visual occlusion.

Main result evidence:

- Full system: 84% success over 180 trials.
- Fixed overhead: 69%.
- Fixed side: 72%.
- Open-loop: 61%.
- Diagnostic axes: overhead loses the hole near final approach; side view
  preserves lateral visibility but leaves depth uncertainty; open-loop carries
  pose error into contact.

Ablation evidence:

- Naive direct action hint: 17%.
- + Geometry-aware execution: 23%.
- + Target-focused perception and geometry-aware execution: 44%.
- + Target-focused perception, overlay self-verification, and geometry-aware
  execution: 76%.
- Full mask-constrained grounding: 88%.
- Rows are additive, not factorial.

Failure boundary:

- Remaining failures occur when all available views are ambiguous or when
  contact produces large pose deviation.
- One 7-DoF robot arm, one tabletop fixture, one cylindrical peg family.
- No confidence intervals, statistical significance test, cross-robot test, or
  deployment study.

Output requirements:

- Generate three paragraphs in this order:
  1. main results paragraph
  2. ablation paragraph
  3. failure boundary paragraph
- Maintain the evidence boundary across paragraphs.
- Avoid repeated phrases.
- Do not invent extra results, mechanisms, or claims.
