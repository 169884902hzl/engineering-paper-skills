# Section Budget

Use this to judge section density.

## Abstract

Normal form: one paragraph, five functional moves.

Too thin:

- no baseline comparison
- no number or concrete evidence
- no data/supervision/evaluation boundary

Too dense:

- mechanism details
- multiple failure modes
- related-work mini-review

## Introduction

Normal form:

1. task context
2. central challenge
3. classical-route gap
4. partial-repair gap
5. second gap
6. formulation
7. contributions

Too thin: background + method + contributions only.
Too dense: related-work taxonomy or method details before formulation.

## Methods

Normal form:

- overview
- main object/formulation
- mechanism blocks
- execution/safety/deployment closure

Too thin: formulas without reader path.
Too dense: perception/model background, appendix-like safety, or setup details.

## Experiments

Normal form:

- short setup
- baselines and metrics
- overall result
- key axes/category analysis
- ablation
- stress/failure boundary

Too thin: pooled average and table only.
Too dense: setup longer than main results or per-object table narration.

## Conclusion

Normal form: one or two paragraphs.

Too thin: only `we proposed`.
Too dense: module recap, new results, or broad future-work list.

## Cut Order

1. Repeated setup details that can move to a table.
2. Caption prose that repeats the paragraph.
3. Long literature lists without a technical axis.
4. Results narration that reads table cells one by one.
5. Redundant transitions and generic importance claims.

Do not cut evenly across all sections. Protect formulation, contribution list,
main results, ablation, failure boundary, and final validation-related text.
