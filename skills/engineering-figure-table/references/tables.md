# Tables

Use this for setup, main results, ablation, and stress-test tables.

## Setup Table

Purpose: keep setup prose short.

Include:

- platform
- sensors
- task protocol
- object/task split
- shared constants needed for fairness

Exclude:

- long explanations better suited to Methods
- every low-level parameter when it is not needed for reproducibility

## Main Results Table

Purpose: support the main claim.

Include:

- methods
- primary metric
- secondary metrics tied to claims
- meaningful categories or conditions
- clear best/second-best marking only if the venue style allows it

Prose should interpret patterns, not read cells aloud.

## Ablation Table

Purpose: map components to contributions.

Include:

- full method
- one removed component per row
- metric most affected by removal
- contribution role in prose or note

Avoid abbreviations that require guessing.

## Ablation Matrix Contract

| Row | Removed component | Claim tested | Metric affected | Interpretation | Boundary |
|---|---|---|---|---|---|
| Full method | none | all contributions | primary metric | reference point | tested protocol only |
| w/o [component] | [component] | [contribution] | [metric] | [bounded drop/pattern] | do not infer untested mechanism |

If an ablation row cannot name the claim it tests, it is a component list rather
than evidence.

## Formatting

Keep table formatting consistent:

- spacing
- row height
- caption syntax
- horizontal rules
- decimal precision
- metric direction
- abbreviation notes
