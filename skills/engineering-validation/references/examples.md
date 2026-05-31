# Engineering Validation Examples

## Abstract Only

Input:

```text
Please tell me if the paper is ready. Here is only the abstract.
```

Expected behavior:

- Overall readiness: `CANNOT_DETERMINE`.
- Build: `NOT_RUN`.
- References: `NOT_RUN`.
- Claim-evidence audit: `PARTIAL`.
- Explain that only a local abstract audit was possible.

## LaTeX Project

Input:

```text
Check this paper repository before submission: /path/to/paper
```

Expected behavior:

- Identify the live draft.
- Read local instructions and build files.
- Run the smallest relevant build command if available.
- Report commands run, inspected files, failures, and unverified items.

## Evidence Audit

Input:

```text
Check whether each contribution in the Introduction is supported by Methods and
Experiments.
```

Expected behavior:

- Build a contribution-evidence table.
- Mark missing Methods or Experiments anchors.
- Do not certify readiness if build/citation/figure checks were not run.

## Build Pass But Logic Fail

Input:

```text
The PDF builds. Contribution 2 claims robustness, but no stress test or
cross-condition experiment is present.
```

Expected report:

```text
Validation result
- Build: PASS
- References: NOT_RUN
- Figures/tables: PARTIAL
- Claim-evidence audit: FAIL
- Private/stale wording scan: NOT_RUN
- Overall readiness: NOT_READY

Blocking issues
- The robustness contribution has no stress-test or cross-condition evidence.
```

## Full Readiness Report Shape

```text
Evidence
- Commands run:
- Files inspected:
- Outputs observed:
- Failures:
- Not verified:

Next actions
- ...
```

## Wrong Active Draft

Input:

```text
The repository has `paper/main.tex`, `submission/main.tex`, and a copied PDF.
The user does not say which source is active.
```

Expected report:

```text
Validation result
- Build: UNKNOWN
- References: UNKNOWN
- Figures/tables: UNKNOWN
- Claim-evidence audit: UNKNOWN
- Private/stale wording scan: NOT_RUN
- Overall readiness: CANNOT_DETERMINE

Blocking issues
- Active source draft is ambiguous.
```
