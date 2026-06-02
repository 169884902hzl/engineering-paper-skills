## Draft

The execution path begins with overhead and side RGB-D observations, which are used to estimate the insertion pose and an associated confidence score. When the confidence score is low, the system requests an additional view before continuing the insertion attempt. The guarded insertion controller then executes the motion while monitoring force and pose deviation, and the attempt is stopped if either the force threshold or the pose-deviation limit is exceeded. The run is finally labeled as insertion success or failure. This overview defines the information flow from observation to guarded execution, while leaving the confidence formula, threshold values, calibration procedure, timing behavior, and pseudocode to be specified before a complete Methods section is finalized.

## Why this works

- Paragraph job: Methods overview.
- Claim flow: input -> state estimate -> view request -> guarded execution -> output.
- Why this order: each sentence hands off the output of one step to the next step.

## Evidence used

- RGB-D observations.
- Insertion pose estimate and confidence score.
- Additional-view request under low confidence.
- Guarded insertion controller and stop conditions.

## Boundary / do-not-claim

- Do not claim performance, deployment, or calibrated thresholds.
- Add the confidence formula, threshold values, calibration procedure, timing, and pseudocode before final Methods prose.
