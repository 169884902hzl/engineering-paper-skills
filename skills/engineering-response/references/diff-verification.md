# Diff Verification

Use this before a response sentence claims that a manuscript change has already
been made.

## Gate

A response claim may be written as final only if all four anchors exist:

```text
Diff verification
| Response claim | Old manuscript anchor | New manuscript anchor | Location verified? | Status | Safe response |
```

- Old manuscript anchor: the reviewer-facing problem existed or was ambiguous.
- New manuscript anchor: the revised text, figure, table, experiment, or note is
  present.
- Location verified: section, figure/table ID, or final line number has been
  checked.
- Status: `Done with evidence`, `Planned`, `Needs author input`, or
  `Not supported`.

If any anchor is missing, do not write "we have added", "we now show", or final
line numbers. Use a plan, placeholder, or author-input note.

## Semantic Match Check

Location alone is not enough. The new manuscript text must actually perform the
change claimed in the response.

```text
Semantic diff verification
| Response sentence | Claimed change | New text evidence | Match? | Mismatch risk | Safe response |
```

- If the response says a claim was narrowed, the revised text must remove or
  hedge the stronger claim.
- If the response says an experiment or table was added, the revised text must
  include that experiment/table and the underlying data.
- If the response says a figure caption was changed, the caption must no longer
  claim evidence the figure cannot show.
- If the response says line numbers are final, the final PDF/source line mapping
  must have been checked after build.
- If the new text only changes wording but not the reviewer's complaint, mark
  the response `Not supported`.

## Unsafe To Safe

| Unsafe response | Why unsafe | Safe response |
|---|---|---|
| We added stress tests. | no stress-test data or revised text supplied | We cannot mark this as completed from the supplied material; add stress-test evidence or revise the claim boundary. |
| Lines 123-130 now explain the method. | final line numbers not verified | We will cite final line numbers after the revised PDF is built and checked. |
| The revised caption validates robustness. | caption cannot validate without experiment | We revised the caption to describe the workflow and removed robustness language. |
| We clarified the method. | may hide unchanged module list | We revised the Methods opening to define the visibility-confidence state and its execution gate. |
| We added Table 3. | no table/data supplied | We cannot claim a new table until the table and source data are supplied and checked. |

## Required Stop Condition

If the user asks for a final response package but manuscript diffs, line numbers,
or added experiments are not available, output a revision plan and unverified
items list instead of final response prose.
