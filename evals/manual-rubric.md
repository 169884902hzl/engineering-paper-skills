# Manual Top-Tier Paper Rubric

Use this rubric for human review of skill outputs on long-form fixtures. Static
checks and golden strings are smoke tests only; this rubric judges paper quality.

| Criterion | 1 - Fail | 3 - Partial | 5 - Strong |
|---|---|---|---|
| Claim-evidence alignment | major claims lack anchors | most claims bounded, some gaps missed | every major claim has method, experiment, figure/table, citation, or limitation anchor |
| Story spine | sections are a list | problem, method, and evidence connect loosely | problem, gap, insight, method, evidence, boundary, implication form a clear chain |
| Sentence necessity | many decorative or redundant sentences | some sentence roles identified | every sentence has function, placement, connection, and evidence boundary |
| AI smell | generic importance, adjective stacks, and mechanical connectors remain | some patterns removed | prose is concrete, restrained, and source-grounded |
| Venue awareness | no venue-specific constraints considered | venue family noted but not operationalized | checklist, limitations, reproducibility, figure, citation, and disclosure needs are explicit |
| Response truthfulness | claims unverified changes | placeholders exist but some claims are vague | every response maps to action, evidence, and verification state |
| Validation honesty | dry read is treated as ready | some checks marked `NOT_RUN` | all required checks use `PASS`, `FAIL`, `PARTIAL`, `NOT_RUN`, or `UNKNOWN` correctly |

Reviewers should record the fixture, skill route, output path, score for each
criterion, blocking failures, and one concrete repository change suggested by
the failure.
