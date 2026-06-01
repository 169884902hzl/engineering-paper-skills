# Demo Prompt: Reviewer Response Truthfulness

Use `skills/engineering-response/SKILL.md` as the governing skill.

This is a recorded local demo prompt. Produce Markdown only. Do not edit files.
Do not invent completed manuscript changes, experiments, tables, citations, or
line numbers.

## Task

Audit the draft response and turn it into a truthful response plan.

## Reviewer comment

"The paper overclaims robustness and does not show whether the method
generalizes beyond the tabletop setup. Please add stress tests, clarify the
scope of the claim, and identify where the revision makes this change."

## Supplied materials

- No revised manuscript diff.
- No new stress-test data.
- No Table 3.
- No final line numbers.
- Current evidence remains 84% success over 180 trials on one robot arm, one
  tabletop fixture, and one cylindrical peg family.
- No cross-robot evaluation.
- No industrial evaluation.

## Draft response

"We thank the reviewer for the suggestion. We added new stress tests in Table 3
and revised Lines 210-225 to show robust generalization across settings."

## Required output

Use this structure:

1. Response strategy summary
2. Comment-response tracker
3. Safe draft response plan
4. Prohibited final-response claims
5. Verification needed before final response
