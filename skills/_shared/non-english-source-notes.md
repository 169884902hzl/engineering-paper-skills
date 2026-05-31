# Shared Non-English Source Notes

Final manuscript prose defaults to English. Non-English material can be used as
source notes, not as final manuscript language, unless the user explicitly asks
otherwise.

## Conversion Steps

1. Extract facts: objects, methods, variables, metrics, conditions, and results.
2. Extract assumptions: hypotheses, guesses, shorthand, or author intent.
3. Extract unsupported claims: statements that need evidence before publication.
4. Write English prose only from facts and explicitly bounded assumptions.
5. Report unsupported claims instead of hiding them in fluent English.

## Output For Thin Notes

```text
Facts
- ...

Assumptions
- ...

Unsupported claims
- ...

English draft or scaffold
[bounded prose]
```

## Mixed-Note Example

Source notes:

```text
Problem: insertion often fails when the target is occluded.
Method: active observation keeps the gripper and target visible.
Assumption: this may improve contact reasoning.
Result: success improves from 71% to 86% in the provided trials.
```

Allowed prose:

```text
The method uses active observation to keep the gripper and target visible during
insertion. In the provided trials, success increases from 71% to 86%. The
available notes do not directly verify the proposed contact-reasoning
mechanism.
```
