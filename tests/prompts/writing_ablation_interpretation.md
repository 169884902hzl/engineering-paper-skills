# Ablation Interpretation Prompt

Use $engineering-writing to draft one ablation paragraph from these rows.
Produce manuscript prose first.

Ablation rows:

- Depth-only grasp planner: 21% success.
- + Seal-pressure retry: 34%.
- + Depth completion and seal-pressure retry: 52%.
- + Depth completion, collision-aware candidate re-ranking, and seal-pressure retry: 69%.
- Full system with surface-normal consistency filter: 81%.

Boundary:

- one task family
- no statistical significance test
- ablation supports component roles but does not prove a causal mechanism
- no deployment evaluation

Do not turn the ablation into a module list. Explain what each major jump
suggests and what it does not establish.
