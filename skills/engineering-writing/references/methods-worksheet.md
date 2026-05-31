# Methods Worksheet

Use this when Methods notes arrive as modules, equations, implementation
details, or mixed bullets. The goal is a reader path, not a directory listing.

## Nine-Block Worksheet

| Block | First sentence role | Must answer | Must avoid | Evidence/source anchor |
|---|---|---|---|---|
| 1. Overview | State the method's central object or loop | What is being transformed, estimated, controlled, or executed? | Starting with a module list | System diagram, algorithm notes, pipeline summary |
| 2. Inputs and outputs | Define the contract | What enters and leaves the method? | Hidden assumptions about sensors or labels | Source variables, data schema, robot/task state |
| 3. Main state/object | Name the object that carries the method | What does each later step update? | Introducing several unrelated objects | Formulation notes, algorithm state |
| 4. Why before formula | Explain why the next formula exists | What failure or constraint motivates it? | Formula first, motivation later | Problem statement, observed failure |
| 5. Mechanism block | Explain the causal or procedural mechanism within evidence | How does the method change behavior? | Claiming unmeasured causality | Ablation, direct measurement, implementation trace |
| 6. Algorithm order | Give the execution order | What happens before what, and why? | Chronological code dump | Algorithm pseudocode, control loop |
| 7. Gate or fallback | Define stop, reject, or fallback behavior | What prevents unsafe or invalid execution? | Presenting safety as a slogan | Thresholds, checks, controller state |
| 8. Implementation boundary | State what is implementation detail vs method claim | What is fixed, tuned, or environment-specific? | Turning parameters into novelty | Configs, setup table, appendix |
| 9. Execution closure | Close with how this enables experiments | What exactly will Experiments evaluate? | New claims not used later | Task protocol, metric definition |

## Bad Patterns And Repairs

| Bad pattern | Why it fails | Repair |
|---|---|---|
| "Our method has perception, planning, and control." | Directory listing | Convert to a loop contract: input, state, update, action, gate |
| "Equation (1) computes the score." | Formula without why | Precede with the failure the score resolves |
| "The safety module ensures robustness." | Unsupported guarantee | State the observable gate and what it can and cannot prevent |
| "We then describe implementation details." | No reader job | Move parameters to setup table unless they support reproducibility or fairness |

## Output Skeleton

```text
Methods reader path
| Block | Paragraph job | Source anchor | Missing input |

Draft order
1. Overview and contract
2. State/formulation
3. Mechanism and algorithm
4. Gate/fallback and execution boundary

Do not write yet
- Claims without mechanism or experiment anchors:
```
