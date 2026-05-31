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
