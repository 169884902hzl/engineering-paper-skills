# Venue-Aware Writing

Use this when a target venue family is named or implied. Do not copy a venue's
tone blindly; adjust claim scope, evidence reporting, limitation placement, and
validation requirements.

## Venue Families

| Venue family | Writing risk | Required emphasis |
|---|---|---|
| Nature/Science/Cell style journals | broad significance can become overclaim | concise problem, strong evidence, explicit limitation |
| NeurIPS/ICML/ICLR | novelty claims can outrun reproducibility | assumptions, limitations, comparison fairness, checklist facts |
| ICRA/IROS/RA-L/RSS/CoRL | system demos can overstate robustness | protocol, baselines, ablation, failure cases, deployment boundary |
| IEEE/ACM systems | architecture may sound like a product description | workload, baseline, mechanism, reproducibility, measured tradeoff |

## Required Output

```text
Venue-aware writing check
| Venue family | Claim risk | Required evidence | Limitation placement | Writing adjustment |
```

If the venue is unknown, use conservative engineering-conference defaults and
avoid journal-scale significance language.

## Venue Profiles

### Nature / Science / Cell Style

- Summary/Abstract must make the broad significance understandable without
  hiding the experimental boundary.
- Strong field implication requires multiple independent evidence anchors.
- Figure legends must explain visible evidence; they cannot replace Methods.
- Discussion may interpret significance but must not introduce untested
  mechanisms or revive deleted claims.

### NeurIPS / ICML / ICLR

- Abstract and Introduction claims must match assumptions, limitations,
  reproducibility details, and empirical scope.
- If baselines, seeds, variance, hyperparameters, or data splits are missing,
  avoid comparative superiority language.
- Limitations should be visible, not buried after strong generalization claims.
- Do not imply deployment reliability from benchmark-only or simulation-only
  results.

### CoRL / ICRA / IROS / RA-L / RSS

- Distinguish algorithmic novelty, system integration, hardware contribution,
  benchmark contribution, and demonstration.
- Real-robot evidence must state task, object family, fixture, robot, trial
  count, protocol, and failure modes.
- One robot, one object family, or one fixture cannot support broad robustness
  or industrial deployment claims.
- Page budget makes deletion-damage testing mandatory: every paragraph must
  support a claim, method mechanism, evidence, boundary, or transition.

### IEEE / ACM Systems

- Architecture descriptions must be tied to measured tradeoffs, workload, and
  baselines.
- Avoid product-like reliability language unless operational evidence exists.
- Reproducibility and configuration details should support interpretation, not
  become a parameter dump.
