# Evidence Audit

Use this before saying paper logic is complete.

## Anchors

Check that these exist and align:

- one-sentence thesis
- contribution list
- Methods support for each contribution
- Experiments support for each contribution
- main results interpretation
- ablation or diagnostic evidence
- failure or limitation statement
- conclusion without new claims

## Claim-Evidence Audit Table

| Claim | First stated | Method anchor | Experiment anchor | Figure/table anchor | Status | Fix |
|---|---|---|---|---|---|---|
|  |  |  |  |  | PASS / FAIL / PARTIAL / UNKNOWN |  |

Rules:

- A claim with no method anchor cannot be a contribution.
- A claim with no experiment anchor cannot be an Abstract or Conclusion
  headline.
- A figure/table anchor must support the same claim, not only a related visual.

## Claim Search

Search for strong words:

```text
prove
confirm
guarantee
robust
generalize
fully
eliminate
state-of-the-art
training-free
```

For each, ask whether the paper directly supports the regime.

## Citation Check

Flag:

- result interpretation with no citation when it depends on prior theory
- related work paragraph that lists papers but never states the gap
- citation placed after a sentence it does not support
- missing citation near a broad field claim
