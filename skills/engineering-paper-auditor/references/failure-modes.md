# Engineering Paper Auditor Failure Modes

| Symptom | Bad output | Correct behavior |
|---|---|---|
| Auditor rewrites instead of audits | Produces final manuscript prose | Return findings and repair routes |
| Audit invents missing evidence | Assumes ablation, citations, or line numbers exist | Mark missing inputs and stop |
| Style notes hide blockers | Lists wording issues before claim-evidence failure | Lead with Critical/High findings |
| Validation is implied | Says manuscript is ready after reading text | Hand off to `engineering-validation` |
| Vague criticism | "Needs improvement" without location or evidence | Tie each finding to claim, section, visual, or missing input |

## Minimum Finding Shape

```text
| Severity | Location | Finding | Evidence | Repair route | Stop condition |
```
