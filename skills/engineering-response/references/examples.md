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
