# Final Read-Only Check

Use this for the final submission window. Avoid broad rewrites unless a blocking
problem is found.

## Minute 1: Confirm Live Draft

Check:

- active manuscript root
- `main.tex` input order
- whether a downstream final copy exists

If the active source is ambiguous, stop and mark validation blocked.

## Minutes 2-5: Title, Authors, Blind State

Check:

- title
- author block
- anonymous or non-anonymous submission mode
- acknowledgements and funding if relevant

Build success does not matter if blind-review state is wrong.

## Minutes 6-10: PDF Baseline

Check:

- `main.pdf` is fresh
- page count
- bibliography count
- obvious missing references or broken floats

If page count or bibliography count changed, explain why.

## Minutes 11-15: Structural Anchors

Check:

- formulation bridge
- contribution list
- main results interpretation
- ablation or diagnostic evidence
- limitation/failure boundary

These are the load-bearing elements.

## Minutes 16-20: Figures, Tables, Captions

Check:

- motivation figure is not a mini Methods section
- framework figure still guides Methods
- workflow figure claims only visible sequence
- table notes define categories and metrics
- category names are consistent

## Minutes 21-25: High-Risk Wording

Search for:

- `stems from`
- `proves`
- `confirms`
- `robust`
- `generalizable`
- repeated `Specifically`
- vague pronouns with multiple referents

Downgrade or clarify if unsupported.

## Minutes 26-30: Build Gate

Run the local build and consistency commands. Record exact outputs.

Do not claim readiness without this evidence.
