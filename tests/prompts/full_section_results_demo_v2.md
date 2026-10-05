# Full Section Results Demo V2 Prompt

Use $engineering-writing to draft a compact mini Results section.

Paper type:
Robotics / engineering conference paper.

Task:
Contact-rich peg insertion under partial visual occlusion.

Source notes:

- Full system: 84% success over 180 trials.
- Fixed overhead camera: 69%.
- Fixed side camera: 72%.
- Open-loop controller: 61%.
- Overhead view loses the hole near final approach.
- Side view preserves lateral visibility but leaves depth uncertain.
- Open-loop execution carries pose error into contact.
- Ablation rows: fixed overhead camera with force-guarded insertion 69%;
  + pose-confidence estimation 70%; + confidence-triggered additional view 78%;
  + pose refinement from the additional view 81%; full system with
  pose-deviation stop 84%.
- Ablation rows are additive, not factorial.
- Remaining failures occur when all available views are ambiguous or when
  contact produces large pose deviation.
- Evaluation uses one 7-DoF robot arm, one tabletop fixture, and one cylindrical
  peg family.
- No confidence intervals, statistical significance test, cross-robot test,
  deployment study, or component-level causal isolation are supplied.

Output requirements:

- Output exactly three manuscript paragraphs.
- Paragraph 1: main result.
- Paragraph 2: ablation interpretation.
- Paragraph 3: failure boundary / operating envelope.
- Separate the paragraphs with blank lines.
- Do not output a heading.
- Do not use `They do not establish...` as the final tail sentence.
- End paragraph 3 with a concrete failure regime or operating envelope, not an
  audit disclaimer.
- Do not invent statistical significance, deployment readiness, broad
  generalization, or causal isolation.
