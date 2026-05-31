# Shared Evidence Boundary

Use this rule set whenever a task touches manuscript claims, prose, figures,
responses, or validation.

## Non-Negotiable Rule

Do not invent:

- experiments, trials, results, metrics, or statistical tests
- mechanisms, causal chains, ablations, or stress regimes
- citations, datasets, baselines, platforms, object categories, or venues
- novelty, robustness, generalization, limitations, or future work
- manuscript edits, line numbers, figures, tables, or response actions

## Evidence Classes

| Evidence class | Safe claim |
|---|---|
| Method only | what the method is designed to do |
| Qualitative example | what the example illustrates |
| Local quantitative result | what happened under the tested condition |
| Ablation or stress test | which component or condition is supported |
| Direct measurement | the measured mechanism or relationship |

If evidence is weaker than the requested claim, downgrade the claim and name the
missing evidence.

## Required Boundary Behavior

- If evidence is absent, ask for it or use placeholders.
- If the user asks for stronger prose, keep the claim at the evidence level.
- If the user asks for citation-like support, require provided or verified
  sources.
- If validation was not run, report `NOT_RUN` rather than implying readiness.
