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

Possible output:

```text
Visual audit
| Item | Responsibility | Visible/tabulated evidence | Claim supported | Must not claim | Placement | Related prose action | Risk | Action |
| Fig. workflow | Explain execution sequence | detection, alignment, guarded insertion | workflow reader path | calibration robustness | Methods overview | cite as workflow only | overclaim | revise caption |

Caption
Fig. X illustrates the three-stage workflow used by the system: target
detection, visual alignment, and guarded insertion.
```

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

Possible output:

```text
Table plan
| Row | Claim tested | Metric affected | Boundary |
| Full | complete system performance | success rate | protocol needed |
| w/o guarded execution | guarded execution contribution | success rate drop | no causal wording beyond ablation |
```

## Setup Table

Input:

```text
The Methods section has a long paragraph listing cameras, image size, controller
rate, object count, and trial count.
```

Expected behavior:

- Recommend a setup table if the list interrupts the argument.
- Keep the prose focused on fairness and reproducibility.

## Visual Audit Example

| Item | Responsibility | Visible/tabulated evidence | Claim supported | Must not claim | Placement | Related prose action | Risk | Action |
|---|---|---|---|---|---|---|---|---|
| Fig. 2 | System reader path | roles and information flow | how components interact | success, robustness, causality | Methods overview | point to system contract | caption overreach | caption points to Methods sections |
| Table II | Ablation evidence | success drop after removing components | component contribution under protocol | universal mechanism proof | Results ablation paragraph | add boundary sentence | causal overclaim | add boundary note |

## Page-Budget Cut Example

Input: setup paragraph lists cameras, resolution, controller rate, object count,
trial count, and table repeats some values.

Expected behavior:

- Move reproducibility facts to setup table.
- Keep baseline fairness in prose.
- Do not cut main result or ablation explanation first.
