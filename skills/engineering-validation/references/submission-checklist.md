# Submission Checklist

Use this for final read-only inspection.

## Last-Pass Order

1. Confirm live draft and input order.
2. Confirm title, author, and blind-review state.
3. Confirm PDF page count and bibliography count.
4. Check thesis, contributions, main results, ablations, and limitations.
5. Check figure/table captions, labels, metric names, and category names.
6. Search for overclaims and AI-looking patterns.
7. Compile and run diff checks.
8. If syncing to a final copy, compile that copy too.

## Final Questions

- What is the biggest remaining risk: logic, format, citation, author state, or
  build?
- Did the last edit reduce that risk?
- Is any claimed completion backed by a command or file inspection?

## Status Labels

- `ready`: all required checks passed
- `ready_with_risks`: build passed but minor known risks remain
- `needs_fix`: actionable problem found
- `blocked`: missing files, ambiguous source draft, or command failure prevents
  validation

Do not use `ready` if any required build, bibliography, page, citation, figure,
or evidence-anchor check was skipped.
