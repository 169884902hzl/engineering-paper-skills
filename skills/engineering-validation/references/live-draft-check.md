# Live Draft Check

Use this to avoid validating the wrong copy.

## Check

- manuscript root
- active `main.tex`
- included section order
- title
- author and blind-review state
- bibliography file
- figure/table inputs
- whether generated, camera-ready, or submission-copy directories are downstream
  only

## Active Draft Rule

Validate the source manuscript that the user is actively editing. Do not treat a
generated copy, camera-ready export, submission mirror, or archived snapshot as
the source unless the user explicitly says that copy is now active.

When a project has both a live draft and a downstream final/submission copy,
check the build inputs and timestamps before judging readiness.

If the active draft cannot be identified from project files or user instruction,
mark validation as blocked instead of guessing.

## Report

State which path was validated. If uncertain, stop and ask or mark validation as
blocked.
