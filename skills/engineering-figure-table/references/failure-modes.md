# Engineering Figure And Table Failure Modes

| Symptom | Bad output | Correct behavior | Required file/reference | Test prompt |
|---|---|---|---|---|
| Caption overclaim | Caption says figure proves robustness | State visible evidence and must-not-claim | `captions.md`, `visual-contract.md` | "Make this workflow figure prove robustness." |
| Table as parameter dump | Table has many columns and no reader action | Assign setup/result/ablation/stress role | `tables.md` | "Put every parameter in one table." |
| Inconsistent names | Caption rename does not reach table/prose | Produce coordinated rename list | `consistency.md`, `_shared/terminology-ledger.md` | "Rename only this caption." |
| Reference damage | Caption edit breaks label/reference chain | Preserve labels or list all affected refs | `consistency.md` | "Change figure labels freely." |
| Causality from outcomes | Success-rate table proves mechanism | Use bounded outcome language | `_shared/claim-strength.md` | "Say this table proves causality." |

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

## Causality From Visuals Or Outcome Tables

Risk: a workflow figure or final success-rate table is used to claim causality.

Response:

- State what the visual or table directly shows.
- Move causal language to an ablation, stress test, or direct measurement only
  when such evidence exists.
- Use bounded wording such as `reports`, `shows`, or `is consistent with`.
