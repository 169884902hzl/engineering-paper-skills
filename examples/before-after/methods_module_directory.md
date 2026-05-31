# Methods Module Directory

## Before

```text
Our method contains a perception module, target detector, controller, and safety
module. The perception module detects the target. The controller moves the
gripper. The safety module stops the system.
```

## Problem

The paragraph lists modules but does not define the method contract, state,
execution order, gate, or fallback.

## After

```text
The method is organized around a closed-loop execution state. The observer
camera provides a target-and-gripper view to the detector, which updates the
target state used by the guarded insertion controller. At each execution step,
the confidence gate either permits the controller to continue or stops execution
when the visible state is insufficient. This contract defines the information
flow evaluated by the subsequent ablation.
```

## Skill Behavior

- Use `engineering-writing` with `methods-worksheet.md`.
- Convert module lists into reader paths.
- Keep safety claims tied to the observable gate.
