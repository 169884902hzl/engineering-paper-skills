# Bad Sentence Repairs

Use this as a repair atlas for common engineering manuscript failure symptoms.

| Symptom | Bad sentence | Why it fails | Safer repair |
|---|---|---|---|
| Directory Methods | "The framework includes perception, planning, control, and safety." | Lists parts without reader path | "The framework updates one execution state from perception to guarded control; each stage supplies the next stage with the information needed for a bounded action." |
| Formula first | "We define \(s_i\) in Eq. (1)." | No motivation | "To rank candidates under partial observation, we compute a score \(s_i\) from the observable state..." |
| Naked number | "Our method achieves 92%." | No protocol or boundary | "Under the stated real-trial protocol, the full system achieves 92% success on the tested object family." |
| Overstrong causality | "This proves the observer improves reasoning." | Mechanism not directly measured | "This result is consistent with the observer preserving task-relevant visibility; direct mechanism evidence would require additional analysis." |
| Generic importance | "This is important for real-world robotics." | Empty motivation | "The failure matters when contact execution depends on target visibility after the gripper occludes the fixture." |
| Symmetric three-part prose | "It is robust, efficient, and general." | Slogan, no evidence split | Replace each adjective with a metric, condition, or remove it. |
| Caption overreach | "Fig. 3 validates robustness." | Visual cannot prove robustness | "Fig. 3 illustrates the workflow stages used during the tested insertion trials." |
| Related Work list | "A used X, B used Y, and C used Z." | Paper-by-paper inventory | Group by technical axis, then state the unresolved gap. |
| Future-work wish list | "Future work will apply this to all settings." | Unbounded promise | "Future work should test whether the same visibility assumption holds under different fixture geometries." |

## Repair Output

```text
Bad sentence audit
| Sentence | Symptom | Evidence risk | Repair |
```
