## Manuscript paragraph

Contact-rich insertion can fail when visual occlusion hides peg-hole alignment and the controller continues from a poor pose estimate. Fixed overhead or side RGB-D cameras may lose task-relevant visibility during insertion, while open-loop insertion does not react to pose uncertainty or contact deviations. We study a system that uses overhead and side RGB-D observations to estimate insertion pose and confidence, requests an additional view when confidence is low, and applies a guarded insertion controller that stops when force or pose deviation exceeds a limit. In 180 trials, the full system achieved 84% success, compared with 69% for a fixed overhead camera, 72% for a fixed side camera, and 61% for an open-loop controller. This evidence supports a bounded system-level improvement in the tested setup, but it is limited to one 7-DoF robot arm, one tabletop fixture, and one cylindrical peg family, with no confidence intervals, no statistical significance test, no cross-robot test, no industrial deployment test, and no ablation isolating view selection from guarded execution.

## Why this is evidence-bound

- The paragraph uses only the supplied task setting, method components, and success rates.
- The comparison is framed as a system-level result, not as proof that view selection alone caused the gain.
- The boundary is stated directly in prose.
- The paragraph avoids claims about statistical significance, cross-robot robustness, or deployment readiness.

## Claims not supported by the supplied notes

- View selection independently caused the improvement.
- The full system is statistically significantly better than the baselines.
- The method is robust across robots, fixtures, peg families, or industrial settings.
- The system is ready for deployment outside the tested tabletop setup.
- The guarded controller and additional-view request mechanism have been separately isolated by ablation.