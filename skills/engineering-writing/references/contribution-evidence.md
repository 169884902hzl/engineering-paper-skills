# Contribution and Evidence

Use this before writing Abstract, Introduction, Results, or Conclusion.

## One-Sentence Thesis

Write one sentence before drafting:

```text
In [task/setting], we address [gap] by [method/formulation], supported by
[evidence], within [boundary].
```

If this sentence cannot be completed, the paper is not ready for strong prose.

## Contribution-Evidence Table

| Contribution | First stated | Mechanism or method support | Evidence support | Overclaim risk |
|---|---|---|---|---|
|  |  |  |  |  |

Rules:

- A contribution without method support is not ready for Introduction.
- A contribution without evidence is not ready for Abstract or Conclusion.
- If evidence supports only a trend, do not claim a mechanism.
- If evidence is local, do not claim generalization.
- If a stress test shows sensitivity, write the boundary as clearly as the gain.

## Claim Strength Ladder

From weaker to stronger:

- `is consistent with`
- `indicates`
- `supports`
- `shows`
- `demonstrates`
- `confirms`

Default to the first three unless the mechanism is directly measured.

## Common Overclaims

- writing `robust` without the stress regime
- writing `generalizable` without cross-task or cross-platform evidence
- writing `calibration-robust` when only a narrower error trend is shown
- writing `training-free` as if no data, detector, or prior model is used
- writing `proves` when the experiment only supports an interpretation

Repair by shrinking the claim to the measured condition.
