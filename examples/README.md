# Examples

This directory gives quick task examples. The executable prompt specifications
used for release QA live in `tests/prompts/`.

## Router

```text
Use $engineering-paper-router to route this task. I have a draft abstract, a
result table, and reviewer comments, and I do not know which skill should run
first.
```

Expected behavior: choose primary and secondary skills, list required inputs,
and avoid drafting final prose during routing.

## Writing

```text
Use $engineering-writing to draft a five-sentence abstract from these facts:
- Problem: contact-rich insertion is sensitive to pose error.
- Method: perception-guided policy with guarded execution.
- Evidence: 92% success over 50 real-robot trials.
- Boundary: one object family and one fixture geometry.
Do not add citations, baselines, objects, or extra numbers.
```

Expected behavior: English abstract plus bounded claim-evidence mapping.

## Polishing

```text
Use $engineering-polishing to improve this paragraph without changing facts:
Our method proves the mechanism and is totally robust. It improves success from
71% to 86%.
```

Expected behavior: preserve the numbers and downgrade unsupported wording.

## Figure/Table

```text
Use $engineering-figure-table to rewrite this caption. The figure only shows a
three-step workflow, but the current caption claims robustness.
```

Expected behavior: caption describes visible workflow and flags the unsupported
robustness claim.

## Response

```text
Use $engineering-response to create a response tracker. Reviewer asks for an
ablation, but no ablation has been run.
```

Expected behavior: no false completed-change claim; status remains planned or
needs author input.

## Validation

```text
Use $engineering-validation to check whether my paper is ready. I only provide
the abstract.
```

Expected behavior: overall readiness is `CANNOT_DETERMINE`; build and reference
checks are `NOT_RUN`.
