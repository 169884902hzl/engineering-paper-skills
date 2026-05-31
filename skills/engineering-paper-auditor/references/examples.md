# Engineering Paper Auditor Examples

## Contribution Without Evidence

Input:

```text
Contribution: the system is robust to occlusion.
Evidence: one main result table; no stress test or occlusion split.
```

Expected output:

```text
Audit verdict
- Overall status: PASS_WITH_BLOCKERS
- Highest-risk issue: robustness claim has no stress-test or condition-axis evidence

Claim-evidence audit
| Claim | First stated | Method anchor | Experiment anchor | Figure/table anchor | Status | Repair route |
| robust to occlusion | contribution list | active observation method | missing stress/occlusion evidence | main result table only | FAIL | engineering-writing + engineering-validation |
```

## Methods Directory

Input:

```text
Methods paragraph: The system has perception, planning, control, and safety
modules.
```

Expected output:

- Finding severity: High.
- Symptom: module list, no reader path.
- Repair route: `engineering-writing` with `methods-worksheet.md`.

## Caption Overclaim

Input:

```text
Fig. 5 shows workflow phases. Caption: "Fig. 5 validates robustness."
```

Expected output:

- Finding severity: High.
- Must not claim: robustness validation.
- Repair route: `engineering-figure-table`.

## Ready Claim Without Checks

Input:

```text
User asks if paper is ready. Only abstract is provided.
```

Expected output:

- Overall status: `CANNOT_DETERMINE`.
- Route: `engineering-validation`.
- Not verified: build, citations, full claim-evidence audit, figures/tables.
