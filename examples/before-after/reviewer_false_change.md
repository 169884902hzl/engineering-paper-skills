# Reviewer False Change

## Before

```text
Reviewer: Please add an ablation for the guarded execution module.
Draft response: We added the requested ablation and discuss it in Lines 123-130.
```

## Problem

The ablation has not been run, and final line numbers are not available.

## After

```text
Status: Needs author input

We agree that an ablation of the guarded execution module would directly test
its contribution. This experiment has not yet been added, so we cannot claim it
as a completed manuscript change. The current response should remain a revision
plan until the ablation result and final manuscript location are available.
```

## Skill Behavior

- Use `engineering-response`.
- Never claim unperformed experiments or invented line numbers.
- Keep final response separate from planned work.
