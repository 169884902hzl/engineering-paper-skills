# Engineering Response Examples

## Missing Ablation

Input:

```text
Reviewer: Please add an ablation study.
Current fact: We have not run any ablation yet.
```

Expected behavior:

- Do not claim the ablation was added.
- Mark status as `Needs author input` or `Planned`.
- Draft a response only if the action is truthful.

## Misunderstood Method

Input:

```text
Reviewer: It is unclear whether the visual module is used during execution.
Current fact: It is used before guarded execution, but the Methods section does
not say this clearly.
```

Expected behavior:

- Classify as clarity/method description.
- Revise the Methods target first.
- Draft a concise response that names the clarification.

## Completed Change

Input:

```text
Reviewer: Define the metric in Table I.
Current fact: The revised caption now defines success rate as completed
insertions divided by total trials.
```

Expected behavior:

- Status: `Done with evidence`.
- Response can say the caption was revised.
- Do not invent line numbers unless final line numbers are provided.

## Five-Comment Package Sketch

| ID | Comment | Decision | Status | Response posture |
|---|---|---|---|---|
| R1.1 | Add ablation. | revise if data exists; otherwise planned | Needs author input | no completed-change claim |
| R1.2 | Method unclear. | revise Methods | Planned | clarify manuscript first |
| R2.1 | Caption overclaims. | revise caption | Done with evidence if caption changed | state exact caption change |
| R2.2 | Too much setup. | compress setup into table | Planned | preserve reproducibility |
| R2.3 | Add broader deployment. | defer with reason | Defer with reason | state evaluation boundary |

Line numbers remain pending until final build.

Possible tracker output:

| ID | Original comment | Type | Real complaint | Action | Evidence/change needed | Line-number status | Status |
|---|---|---|---|---|---|---|---|
| R1.1 | Add ablation. | experiment | component contribution is not isolated | planned or needs input | ablation result or explicit limitation | unavailable | Needs author input |
| R1.2 | Method unclear. | clarity | execution-time use is ambiguous | revise Methods | sentence explaining visual module timing | placeholder only | Planned |
| R2.1 | Caption overclaims. | figure/table | caption claims more than visible | revise caption | bounded caption text | placeholder only | Done with evidence if revised |
| R2.2 | Too much setup. | structure | setup interrupts results | move to table | setup table or compressed paragraph | placeholder only | Planned |
| R2.3 | Add broader deployment. | scope | reviewer wants external validity | defer with reason | boundary/limitation text | placeholder only | Defer with reason |

Possible response fragment:

```text
We agree that the previous caption overstated what the figure showed. We have
revised the caption to describe the visible workflow stages only and moved the
robustness claim to the Results discussion where it can be tied to the tested
conditions. Final line numbers will be inserted after the camera-ready build.
```
