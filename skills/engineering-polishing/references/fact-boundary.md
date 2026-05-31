# Fact Boundary

Use this before expanding rough notes or polishing sparse source material.

## Rules

- Use only facts provided by the user or visible in the manuscript.
- Do not add literature, model names, datasets, test conditions, results, or
  causal explanations.
- Keep terms, abbreviations, variables, units, metrics, and explicit
  experiment/simulation relations, but reorganize expression rather than copying
  a sample sentence pattern.
- If method and evidence are missing, write a bounded setup or placeholder, not
  a complete claim.
- If a number lacks unit, baseline, condition, or metric meaning, do not use it
  as proof.
- If a relation is unclear, use descriptive connection rather than causal
  language.
- Claim strength must not exceed evidence strength:
  - method only -> do not claim effect
  - experiment only -> do not claim mechanism
  - trend only -> do not claim quantitative gain
  - local result only -> do not claim broad generalization

## Thin Input Handling

If two or more are missing, downgrade:

- object
- problem
- method
- evidence

Safe output:

```text
This paragraph can only state [known object/problem]. Evidence for [missing
claim] is not provided.
```

## Preserve

- technical terms
- abbreviations
- equations and symbols
- units and metrics
- explicit uncertainty
- stated limitations

## Data Handling

Data is not decoration. If a paragraph includes a number, explain which
performance judgment, comparison, or mechanism interpretation it supports. If
the source does not provide that relation, keep the number descriptive.
