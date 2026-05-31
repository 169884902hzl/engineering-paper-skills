# Engineering Polishing Examples

## Claim Downgrade

Input:

```text
Our method proves the mechanism and is totally robust. It improves success from
71% to 86%.
```

Expected behavior:

- Preserve `71%` and `86%`.
- Downgrade unsupported wording such as `proves` and `totally robust`.
- Do not add a mechanism or new experimental context.

Possible output:

```text
The results support the effectiveness of the proposed method, with success
increasing from 71% to 86% under the evaluated conditions.
```

## Source Notes To English

Input:

```text
Problem: pose noise hurts insertion.
Method: guarded execution after visual alignment.
Result: fewer failed contacts.
```

Expected behavior:

- Produce English manuscript prose.
- Preserve the provided facts.
- Mark missing numbers or experimental conditions if the user wants a stronger
  claim.

## Logic Diagnosis Before Polish

Input:

```text
This paragraph says the method is robust, but no robustness test is given.
```

Expected behavior:

- Do not polish it into a stronger claim.
- Explain that the claim/evidence relation is broken.
- Offer a conservative rewrite or ask for robustness evidence.
