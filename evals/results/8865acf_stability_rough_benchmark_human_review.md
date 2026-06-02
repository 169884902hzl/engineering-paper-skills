# Rough-user And Benchmark Stability Human Review

Base commit: `8865acf6469b0dae32d16807c341c04bf249e2a3`

| Prompt family | Best | Median | Worst | Hallucination | Prose quality variance | Mechanism interpretation variance | Stable under rough/benchmark inputs? |
|---|---|---|---|---|---|---|---|
| rough-user Results | run3 | run1 | run2 | no | moderate; run2 uses more generic support wording | low; all preserve ranking and boundary | yes for evidence, not hero proof |
| rough-user Chinese notes | run3 | run2 | run1 | no | moderate; two runs use support wording | low; all preserve occlusion/view/update logic | yes for evidence, not hero proof |
| benchmark robotics Results | run1 | run2 | run3 | no | low | low; all preserve proposal, wrist verification, guarded lift | yes |
| benchmark ML systems Methods | run3 | run1 | run2 | no | low | low; all preserve freshness-bundle path and fallback boundary | yes |

Conclusion: the local three-run sample is stable enough to keep as public-beta evidence. It is not CI-controlled and does not prove top-tier readiness.
