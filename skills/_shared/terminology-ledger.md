# Terminology Ledger

Use this shared reference when multiple skills edit the same manuscript or when
the user asks for more varied wording.

## Core Rule

Technical names should be stable. Vary sentence structure, not the names of
methods, modules, datasets, object categories, metrics, tasks, or experimental
conditions.

## Ledger

| Canonical term | Allowed short form | Do not use | Applies to | Notes |
|---|---|---|---|---|
| method/system name | only if introduced | new synonyms | title, abstract, methods, experiments | Keep capitalization fixed |
| object/category name | table abbreviation if defined | partial rename | captions, tables, result text | Rename everywhere or nowhere |
| metric name | symbol if defined | near-synonym metric | tables, figures, results | Keep direction clear |
| baseline name | exact label from experiment | invented baseline | experiments, abstract | Do not create baselines |
| mechanism name | exact source term | stronger mechanism | methods, discussion | Do not turn assumptions into terms |

## Output Pattern

When terminology risk is present, include:

```text
Terminology ledger
| Canonical term | Current variants found | Decision | Locations to update |
```

## Failure Pattern

Bad: "observer camera", "active view", "mobile eye", and "auxiliary camera" all
refer to the same component without definition.

Correct behavior: choose one canonical term from the source or ask the author to
choose; keep the rest only as explicitly introduced short forms.
