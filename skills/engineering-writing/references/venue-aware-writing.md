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
