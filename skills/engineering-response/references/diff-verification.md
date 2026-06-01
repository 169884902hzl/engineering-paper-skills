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

## Unsafe To Safe

| Unsafe response | Why unsafe | Safe response |
|---|---|---|
| We added stress tests. | no stress-test data or revised text supplied | We cannot mark this as completed from the supplied material; add stress-test evidence or revise the claim boundary. |
| Lines 123-130 now explain the method. | final line numbers not verified | We will cite final line numbers after the revised PDF is built and checked. |
| The revised caption validates robustness. | caption cannot validate without experiment | We revised the caption to describe the workflow and removed robustness language. |

## Required Stop Condition

If the user asks for a final response package but manuscript diffs, line numbers,
or added experiments are not available, output a revision plan and unverified
items list instead of final response prose.
