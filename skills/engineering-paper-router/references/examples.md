# Engineering Paper Router Examples

## Ambiguous Paper Revision

Input:

```text
Please improve my paper before submission.
```

Expected route:

- Primary: `engineering-validation`
- Secondary: `engineering-polishing`
- Required inputs: manuscript path, target venue, build command, known risks.

## Mixed Drafting Task

Input:

```text
I have method notes, result tables, and figure captions. Help me turn them into
a paper section plan.
```

Expected route:

- Primary: `engineering-writing`
- Secondary: `engineering-figure-table`

## Reviewer Comments

Input:

```text
Reviewer 2 says our ablation is weak and the caption overclaims robustness.
```

Expected route:

- Primary: `engineering-response`
- Secondary: `engineering-figure-table`
