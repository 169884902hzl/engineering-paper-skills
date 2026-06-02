# Results Interpretation Prompt

Use $engineering-writing to draft one Results paragraph from this table-like
evidence. Produce manuscript prose first.

Experiment question:
Does the full system improve insertion success over fixed-view and open-loop
variants in the tested tabletop occlusion setup?

Results:

- Full system: 84% success over 180 trials.
- Fixed overhead camera: 69%.
- Fixed side camera: 72%.
- Open-loop controller: 61%.

Boundary:

- one robot arm
- one tabletop fixture
- one object family
- no confidence intervals
- no statistical significance test
- no cross-robot test
- no industrial deployment test
- no ablation isolating view selection from guarded execution

Do not claim statistical significance, causal isolation, cross-robot
robustness, or deployment readiness.
