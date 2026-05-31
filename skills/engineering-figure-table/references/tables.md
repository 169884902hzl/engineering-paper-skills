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

## Formatting

Keep table formatting consistent:

- spacing
- row height
- caption syntax
- horizontal rules
- decimal precision
- metric direction
- abbreviation notes
