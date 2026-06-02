# Full Section Methods Demo Prompt

Use $engineering-writing to draft a mini Methods section.

Paper type:
Robotics / engineering conference paper.

Task:
Contact-rich peg insertion under partial visual occlusion.

Source notes:

- The method is organized around resolving insertion-pose uncertainty before
  guarded contact execution.
- Inputs: overhead RGB-D observation, side RGB-D observation, candidate
  insertion pose, and confidence estimate.
- Intermediate representation: insertion pose estimate paired with confidence.
- If confidence is low, the system requests an additional view and updates the
  insertion pose.
- The refined pose estimate is passed to a guarded insertion controller.
- The controller executes insertion from the refined pose and stops on force or
  pose-deviation limits.
- The prompt does not provide formulas, thresholds, latency, calibration
  details, or pseudocode.

Requirements:

- Output exactly three manuscript paragraphs with blank lines between them.
- Paragraph 1: overview and organizing principle.
- Paragraph 2: component / intermediate representation.
- Paragraph 3: execution and safety.
- Do not output headings.
- Do not invent formulas, thresholds, latency, calibration, or deployment
  guarantees.
- Keep a clear reader path; do not write a module inventory.
