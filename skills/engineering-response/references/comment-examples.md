# Comment Examples

Use this to route common comments.

## Experiments Read Like a Report

Real complaint: evidence is not tied to the contribution.

First target: Experiments.

Fix:

- add overall result interpretation
- split by meaningful task/object/condition axes
- add failure boundary
- make ablation map to contribution

Prohibited over-edit: do not rewrite Methods first.

## Methods Read Like Modules

Real complaint: reader path is missing.

First target: Methods overview and first main-object subsection.

Fix:

- state system roles
- explain why the main signal/model appears first
- connect modules through data/control flow

Prohibited over-edit: do not add more modules or formulas to look complete.

## Claim Is Too Strong

Real complaint: claim exceeds evidence.

First target: Experiments and contribution list.

Fix:

- downgrade verbs
- state tested regime
- move unsupported mechanism back to Methods or Discussion
- add limitation if needed

Prohibited over-edit: do not delete all interpretation and leave table narration.

## Caption Is Vague

Real complaint: visual responsibility is unclear.

First target: figure/table and caption.

Fix:

- state visual responsibility
- caption only visible/tabulated information
- align text reference with figure role

Prohibited over-edit: do not use caption to patch missing Results logic.

## Related Work Is a Citation List

Real complaint: taxonomy and nearest-neighbor distinction are missing.

First target: Related Work or Introduction literature paragraphs.

Fix:

- group by technical axes
- end each axis with a limitation
- isolate the nearest neighbor
- bridge to the paper's uncovered combination

Prohibited over-edit: do not add more citations without changing structure.

## Conclusion Is Empty

Real complaint: the paper does not recover its final supported claim.

First target: Conclusion.

Fix:

- paragraph 1: method + strongest stable evidence
- paragraph 2: boundary + future work derived from boundary

Prohibited over-edit: do not introduce new claims or revive removed analysis.

## Abstract Sounds Promotional

Real complaint: the abstract does not bind problem, method, evidence, and
boundary.

First target: Abstract.

Fix:

- sentence 1: task and failure mode
- sentence 2: existing route gap
- sentence 3: method core
- sentence 4: evaluation boundary
- sentence 5: strongest stable evidence

Prohibited over-edit: do not add new results or unsupported adjectives.
