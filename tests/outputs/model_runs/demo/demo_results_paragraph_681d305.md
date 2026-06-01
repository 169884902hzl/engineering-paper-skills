## 1. Experiment question

Does the proposed multi-view guarded insertion system improve insertion success over fixed-view and open-loop variants in the tested tabletop occlusion setup?

## 2. Manuscript paragraph

In the tabletop occlusion setup, the full multi-view guarded insertion system achieved an 84% insertion success rate over 180 trials. This was higher than the fixed overhead RGB-D camera variant at 69%, the fixed side RGB-D camera variant at 72%, and the open-loop controller at 61%, corresponding to absolute gains of 15, 12, and 23 percentage points, respectively. These results support a bounded system-level claim that combining multi-view perception with guarded execution improves insertion success in the tested single-arm, single-fixture, cylindrical-peg setting. However, the experiment does not isolate the individual effects of view selection and guarded execution, and it does not establish generalization across object families, robots, or deployment environments.

## 3. Claim-evidence note

The evidence supports a limited comparative claim: the full system achieved higher measured success than the fixed-view and open-loop variants in the stated tabletop protocol. The claim should remain descriptive because no confidence intervals, statistical significance tests, per-baseline trial counts, or component-isolating ablations are provided.

## 4. Claims to avoid

- The method is statistically significantly better than the baselines.
- The improvement is caused specifically by view selection alone.
- The improvement is caused specifically by guarded execution alone.
- The system generalizes to other object families, robots, fixtures, or industrial deployment.
- The method is robust under untested occlusion, geometry, or hardware conditions.