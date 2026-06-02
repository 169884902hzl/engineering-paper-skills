# Methods Showcase V2 Prompt

Use $engineering-writing to draft a showcase-grade Methods overview paragraph.

Target section:
Methods overview.

Paper type:
Robotics / engineering conference paper.

Task:
Explain the method path for contact-rich peg insertion under partial visual
occlusion.

Organizing principle:
Resolve pose uncertainty before guarded contact execution, because uncertainty
that enters contact is harder to correct safely.

Inputs:

- Overhead RGB-D observation.
- Side RGB-D observation.
- Candidate insertion pose and confidence estimate.

Intermediate object:
An insertion pose estimate paired with a confidence score.

Transformation and handoff:

- Estimate insertion pose and confidence from the available RGB-D observations.
- If confidence is low, request an additional view.
- Use the new view to update the insertion pose.
- Hand the refined pose estimate to the guarded insertion controller.

Execution and safety boundary:

- The guarded controller executes insertion from the refined pose estimate.
- It stops on force or pose-deviation limits.
- The prompt does not provide formulas, thresholds, latency, calibration
  details, or pseudocode.

Style requirements:

- Produce manuscript prose first.
- Start from the organizing principle, not just `Given inputs`.
- Include input -> intermediate object -> transformation -> handoff ->
  execution/safety boundary.
- Explain why the reader path is ordered that way.
- Do not write a module inventory.
- Do not invent formulas, thresholds, latency, calibration, or pseudocode.
