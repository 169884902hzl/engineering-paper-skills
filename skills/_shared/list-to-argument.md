# List To Argument

Use this shared reference when source material arrives as bullets, module names,
result rows, reviewer comments, or caption claims.

## Core Rule

A list is not yet an argument. Before turning it into manuscript prose or a
response plan, assign each item a function.

| List item type | Convert to | Do not convert to |
|---|---|---|
| Module names | Reader path with inputs, outputs, and dependencies | Directory-style Methods prose |
| Result rows | Evaluation question, trend, evidence, and boundary | Table narration |
| Advantages | Claim-evidence map | Promotional adjectives |
| Reviewer comments | Revision tracker with acceptance evidence | Polite response text only |
| Figure panels | Visual responsibility map | Caption-only description |

## Conversion Steps

1. Group items by function, not by arrival order.
2. Identify the controlling question: what should the reader learn from this
   group?
3. Keep one main claim per paragraph or tracker item.
4. Attach evidence, boundary, and required verification.
5. Drop or park list items that do not support the current section job.

## Failure Pattern

Bad:

```text
The system contains perception, planning, control, and safety modules.
```

Better structure:

```text
The method is organized around one closed-loop state update: perception defines
the observable target state, planning converts that state into a constrained
motion intent, and guarded control executes the intent while stopping on
low-confidence observations.
```

Only use the better structure if the dependencies are supported by the provided
method notes or source files.
