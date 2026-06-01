# Fixture: Methods Module Directory

## Flawed manuscript input

Our method contains three modules. The perception module detects the target and
the gripper. The observer module moves the auxiliary camera to a better view.
The control module executes the insertion policy. The safety module stops the
robot if confidence is low. The full framework is shown in Fig. 2. The method
is robust because the observer camera provides more information and the safety
module avoids dangerous actions.

The section reads like a directory. It names components but not the state that
flows across them. It does not say what input each module receives, what output
it gives the next module, when the observer moves, what confidence means, what
threshold triggers guarded execution, or how the safety stop is recovered. The
robustness claim appears inside Methods without experiment or stress evidence.
The figure reference is also doing too much work; it cannot replace the method
reader path.

## Expected audit pressure

The skill should build a Methods reader path: system state, active observation
condition, policy input, guarded-action trigger, fallback, and boundary. It
should move robustness evidence to Experiments or downgrade it to a design
intent. It should identify which sentence is a method object and which sentence
is unsupported interpretation.

## Failure modes

- Module directory.
- Formula or component before motivation.
- Method section contains result claim.
- Figure reference hides missing method logic.
