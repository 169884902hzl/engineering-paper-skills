# Shared Claim Strength

Use the weakest verb that still says the true thing.

## Verb Ladder

| Verb | Evidence needed |
|---|---|
| `is consistent with` | qualitative or partial support |
| `suggests` | trend, example, or limited comparison |
| `indicates` | repeated observation under stated conditions |
| `supports` | direct evidence for a bounded claim |
| `shows` | clear measured outcome under stated protocol |
| `demonstrates` | strong direct evidence across the stated evaluation |
| `confirms` | direct verification of the mechanism or property |

Avoid `proves`, `guarantees`, `fully robust`, `generalizes`, and `state of the
art` unless the manuscript provides the exact evidence those phrases require.

## Repair Pattern

```text
Requested claim: [strong claim]
Evidence available: [actual evidence]
Safe wording: [bounded claim]
Evidence needed for stronger wording: [missing test/source]
```

## Engineering Examples

| Available evidence | Safe wording | Unsafe wording |
|---|---|---|
| One ablation row shows a success drop after removing a component | "supports the contribution of the component under the tested protocol" | "proves the mechanism" |
| Stress test covers one perturbation range | "shows robustness within the evaluated range" | "fully robust" |
| Qualitative workflow image | "illustrates the execution sequence" | "validates the controller" |
| Direct timing measurement | "reduces runtime under the measured setup" | "is efficient in real-world deployment" |
