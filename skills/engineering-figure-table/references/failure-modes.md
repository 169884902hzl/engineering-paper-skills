# Engineering Figure And Table Failure Modes

## Caption Overclaim

Risk: the caption says the visual proves a mechanism, robustness, or
generalization that the visual does not show.

Response:

- Remove or downgrade the claim.
- State `must not claim` in the visual audit.

## Table As Parameter Dump

Risk: the table lists many values without a reader action.

Response:

- Define whether the table compresses setup, compares results, supports an
  ablation, or explains a stress test.
- Remove columns that do not support the table responsibility.

## Inconsistent Names

Risk: figure labels, captions, tables, and prose use different names for the
same category or metric.

Response:

- Pick one canonical name.
- List every place that must change together.

## LaTeX Reference Damage

Risk: editing captions or labels breaks `\ref`, `\label`, or table notes.

Response:

- Preserve labels unless there is a direct reason to change them.
- If a label changes, list all affected references.
