## 1. Verdict

Figure 3 and Table 1 support only a limited claim: the full system reports a higher success rate than the listed baselines under the tested protocol.

They do not support claims of statistical significance, causal validation, robust generalization, industrial deployment readiness, or solving insertion under occlusion.

## 2. Panel/table responsibility map

| Item | Responsibility | Evidence shown | Claim supported | Boundary |
|---|---|---|---|---|
| Figure 3A | System overview | RGB-D observation, confidence estimate, view request, guarded execution, stop states | Describes the proposed workflow | Cannot prove robustness, causality, or deployment readiness |
| Figure 3B | Qualitative example | One successful tabletop insertion sequence | Illustrates one successful trial | Cannot establish generalization, robustness, or typical behavior |
| Figure 3C | Quantitative comparison | Success rates: 84%, 69%, 72%, 61% | Full system has the highest reported success rate among shown methods | No confidence intervals, error bars, trial counts, or statistical tests |
| Table 1 | Source-data summary | Full system has 180 trials; baseline trial counts not stated | Partially documents the full-system denominator | Baseline denominators are missing, so comparison strength is limited |

## 3. Unsupported caption/prose claims

| Claim | Status | Reason |
|---|---|---|
| “proves” | Unsupported | The figure reports observations and rates; it does not prove a mechanism. |
| “robustly solves industrial insertion under occlusion” | Unsupported | The provided evidence is tabletop insertion plus success rates, with no industrial deployment or occlusion stress-test evidence. |
| “validate the causal role of view selection” | Unsupported | Fixed-camera baselines suggest an association, but causal attribution requires controlled protocol details and matched comparisons. |
| “deployment-ready performance” | Unsupported | No live deployment duration, failure recovery, safety, hardware variability, or field evidence is shown. |
| “significantly outperforms all baselines” | Unsupported | No confidence intervals, per-baseline trial counts, or statistical tests are provided. |
| “robust generalization to realistic insertion settings” | Unsupported | No task diversity, environment split, object variation, occlusion levels, or held-out setting evidence is provided. |

## 4. Safe caption

**Figure 3. Active-observation workflow and insertion success rates under the tested protocol.**  
(A) System workflow from RGB-D observation and confidence estimation to view request, guarded execution, and stop states. (B) Representative sequence from one successful tabletop insertion trial. (C) Reported success rates for the full system and three baselines: fixed overhead camera, fixed side camera, and open-loop controller. Error bars, confidence intervals, and per-baseline trial counts are not shown.

## 5. Safe result prose

The full system achieved the highest reported success rate among the evaluated methods, with 84% success compared with 69% for the fixed overhead camera baseline, 72% for the fixed side camera baseline, and 61% for the open-loop controller. Because Figure 3C does not include uncertainty estimates or per-baseline trial counts, these results should be interpreted as descriptive comparisons under the tested protocol rather than evidence of statistical significance or deployment-ready robustness.

## 6. Source-data checks required before stronger claims

- Provide trial counts for every condition in Figure 3C and Table 1.
- Verify that plotted success rates exactly match the underlying source data.
- Define the success criterion and confirm it is identical across methods.
- Report confidence intervals or error bars for each condition.
- Run and report appropriate statistical tests before claiming significant improvement.
- Confirm that all methods were evaluated under matched task, scene, camera, and controller conditions.
- Document whether failed, aborted, or excluded trials were included in the denominator.
- Provide occlusion-specific trials before claiming robustness under occlusion.
- Provide task/environment diversity or held-out evaluations before claiming generalization.
- Provide real deployment logs and safety/failure recovery evidence before claiming deployment readiness.