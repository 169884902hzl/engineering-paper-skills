# Methods Reader Path Prompt

Use $engineering-writing to draft a Methods overview paragraph from these module
notes. Produce manuscript prose first.

Method notes:

- Input: overhead and side RGB-D observations.
- State: insertion pose estimate and confidence score.
- View request: when confidence is low, request an additional view.
- Controller: guarded insertion controller.
- Stop conditions: force threshold exceeded or pose deviation exceeds a limit.
- Output: insertion success or failure.

Missing:

- confidence formula
- threshold values
- calibration procedure
- timing or latency
- pseudocode

Do not add experiments, baselines, citations, equations, threshold values,
deployment claims, or result claims.
