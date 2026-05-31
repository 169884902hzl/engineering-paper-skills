# Experiments Worksheet

Use this when writing Experiments or Results from tables, logs, setup notes, or
claims. The section should prove bounded contributions, not recite tables.

## Evaluation Questions

Start by assigning the experiment section to concrete questions:

| Question | Section role | Required evidence |
|---|---|---|
| Q1: Does the full system improve the target task? | Main result | Task protocol, metric, baseline/comparison |
| Q2: Which component explains the improvement? | Ablation | Removed component, affected metric, boundary |
| Q3: Where does it work or fail? | Category/stress/failure analysis | Condition axis, failure envelope |
| Q4: Is the setup fair and reproducible? | Protocol/setup | Hardware, data, metrics, trial count, evaluation rule |

## Ten-Block Worksheet

| Block | First sentence role | Must contain | Must not contain |
|---|---|---|---|
| 1. Setup purpose | State what the experiments test | Contribution link | Generic "we evaluate" sentence |
| 2. Hardware/protocol | Define the testbed and trial rule | Platform, task, trial count if provided | Unprovided deployment claims |
| 3. Compared methods | Define baselines and variants | Exact names from source | Invented baselines |
| 4. Metrics | Define metric direction and meaning | Success, error, time, cost, or task metric | Ambiguous "performance" |
| 5. Main result | Answer Q1 | Overall trend and strongest provided evidence | Full table narration |
| 6. Category axis | Explain condition-level behavior | Object/scene/task axis if provided | New categories |
| 7. Ablation | Answer Q2 | Component removed and metric change | Causality stronger than ablation supports |
| 8. Stress/sensitivity | Answer Q3 | Stress variable and boundary | Universal robustness |
| 9. Failure envelope | State where method fails | Failure condition or limitation | Hiding failures |
| 10. Section closure | Tie evidence back to contribution | Bounded takeaway | New claim for Conclusion only |

## Result Paragraph Pattern

```text
[Question answered]. [Data/trend]. [Interpretation tied to method or setup].
[Boundary or failure condition].
```

## Bad Patterns And Repairs

| Bad pattern | Repair |
|---|---|
| "Table I shows all results." | State the evaluation question and one bounded takeaway. |
| "The method proves robustness." | Replace with the tested condition and stress evidence. |
| "The ablation proves the mechanism." | State what changes when the component is removed; reserve mechanism claims for direct evidence. |
| "Several failures occurred." | Name the failure envelope if source evidence exists; otherwise mark missing. |
