# Engineering Figure And Table Examples

## Workflow Figure

Input:

```text
The figure shows a three-step workflow: detection, alignment, guarded insertion.
The draft caption says it proves calibration robustness.
```

Expected behavior:

- Assign responsibility: workflow explanation.
- Remove the robustness claim unless robustness evidence is visible or tabulated.
- Write a caption that describes what the figure actually shows.

## Ablation Table

Input:

```text
Table II lists success rates for Full, w/o guarded execution, and w/o visual
alignment.
```

Expected behavior:

- Assign responsibility: contribution support and component ablation.
- Check whether rows map to contribution claims.
- Ask for trial counts and evaluation conditions if absent.

## Setup Table

Input:

```text
The Methods section has a long paragraph listing cameras, image size, controller
rate, object count, and trial count.
```

Expected behavior:

- Recommend a setup table if the list interrupts the argument.
- Keep the prose focused on fairness and reproducibility.
