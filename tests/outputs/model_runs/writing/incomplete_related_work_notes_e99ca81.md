**Draft**

Vision-based manipulation often uses fixed-camera observations to estimate object or task pose, a setup that is well suited when the relevant geometry remains visible during the manipulation sequence [CITE: fixed-camera manipulation]. Active view-selection methods broaden the observation process by choosing additional viewpoints, often for coverage, inspection quality, or grasp planning [CITE: active view selection]. In parallel, tactile, force, or compliance-based guarded insertion methods address uncertainty during execution by detecting contact conditions and adapting or stopping the insertion motion [CITE: guarded insertion]. This work is positioned between these axes: confidence-triggered RGB-D view acquisition is used to refine the insertion pose before guarded execution, linking additional observation to a pre-execution pose-refinement decision rather than only to general scene coverage or grasp-oriented perception [CITE: active perception for manipulation]. The closest comparison set should include work that couples perception with compliant or guarded insertion [CITE: perception and compliant insertion].

**Citation Verification Needs**

- Verify representative fixed-camera manipulation papers where pose estimation assumes continued visibility.
- Verify active view-selection papers focused on coverage, inspection, or grasp planning.
- Verify tactile, force, or compliant guarded insertion papers for execution-stage contact handling.
- Find and verify the nearest paper combining perception with compliant or guarded insertion before writing a sharper distinction.