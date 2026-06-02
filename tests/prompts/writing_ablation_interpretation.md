# Ablation Interpretation Prompt

Use $engineering-writing to draft one ablation paragraph from these rows.
Produce manuscript prose first.

Ablation rows:

- Naive direct action hint: 17% success.
- + Geometry-aware execution: 23%.
- + Target-focused perception and geometry-aware execution: 44%.
- + Target-focused perception, overlay self-verification, and geometry-aware execution: 76%.
- Full system with mask-constrained grounding: 88%.

Boundary:

- one task family
- no statistical significance test
- ablation supports component roles but does not prove a causal mechanism
- no deployment evaluation

Do not turn the ablation into a module list. Explain what each major jump
suggests and what it does not establish.
