# Demo Prompt: Methods Execution Path

Use `skills/engineering-writing/SKILL.md` as the governing skill.

This is a recorded local demo prompt. Produce Markdown only. Do not edit files.
Do not invent algorithms, equations, thresholds, sensors, or guarantees.

## Task

Convert a module list into a Methods execution path for an engineering paper.
Expose what cannot yet be written because the author did not supply details.

## Rough method notes

- Inputs: RGB-D observations from an overhead camera and a side camera.
- State estimate: insertion pose estimate and a confidence score.
- View request: when confidence is low, request another view.
- Control: guarded insertion controller.
- Stop conditions: force threshold exceeded or pose deviation exceeds limit.
- Output: insertion success/failure.

## Missing details

- No formula for confidence score.
- No exact force threshold.
- No exact pose-deviation limit.
- No timing or latency.
- No calibration procedure.
- No pseudocode supplied.

## Required output

Use this structure:

1. Methods diagnosis
2. Execution-path paragraph scaffold
3. Information that can enter prose now
4. Placeholders that must not be invented
5. Safe Methods paragraph
