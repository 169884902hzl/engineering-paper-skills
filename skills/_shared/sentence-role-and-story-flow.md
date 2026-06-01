# Sentence Role And Story Flow

Use this whenever a paragraph is drafted, polished, audited, shortened, or
reordered. A paper sentence is not decorative. It must do necessary work in the
argument.

## Core Rule

Every sentence must pass the full top-tier sentence audit. A sentence that
sounds fluent but fails one of these checks is not ready for manuscript prose.

| Gate | Question | If the answer is weak |
|---|---|---|
| Function | What paper job does this sentence perform? | assign a job or delete it |
| Necessity | If this sentence is removed, what becomes missing or easier to misunderstand? | delete or merge it |
| Placement | Why does it belong here rather than another section or paragraph? | move it |
| Connection | How does it follow from the previous sentence and prepare the next one? | add a bridge or reorder |
| Evidence boundary | What fact, method detail, result, figure/table, citation, or limitation supports it? | hedge, mark unsupported, or remove |
| Ambiguity | Could a reader misread actor, object, scope, causality, robustness, or generalization? | name the ambiguity and rewrite |
| Redundancy source | Does it repeat the previous sentence, heading, table, caption, or common background? | delete, merge, or make it do new work |
| AI-smell pattern | Does it use empty importance, adjective stacking, vague subjects, or mechanical connectors? | replace with concrete paper function |
| Claim-strength delta | Did the rewrite make the claim stronger than the source? | restore the original boundary |

If a sentence can be removed without losing meaning, evidence, transition, or
boundary, it is redundant. If a sentence is missing and the reader can
misunderstand the claim, method, evidence, or boundary, add the missing sentence.

## Allowed Sentence Jobs

Use one primary job per sentence:

| Job | Sentence should do |
|---|---|
| Context | define the task, setting, object, or reader need |
| Gap | isolate the unresolved limitation |
| Prior-route limit | state what existing method classes cover and miss |
| Bridge | connect the previous idea to the next necessary step |
| Method object | introduce the system object, state, variable, module, or procedure |
| Mechanism | explain how a method component changes the relevant condition |
| Protocol | specify setup, metric, baseline, trial, dataset, or comparison condition |
| Evidence | report a measured result, visual observation, or table-supported pattern |
| Interpretation | explain what the evidence supports, locally and boundedly |
| Boundary | state what is not shown, not tested, or not claimed |
| Hand-off | close the paragraph and make the next paragraph necessary |

Do not let one sentence do unrelated jobs, such as opening a gap while also
claiming a result and adding a limitation. Split or move it.

## Claim Types

Every claim-bearing sentence should be tagged with one primary type:

| Claim type | Required support |
|---|---|
| Background | source, accepted field fact, or clearly local framing |
| Method | method section detail, algorithm, system object, or implementation note |
| Result | protocol, metric, comparison, figure, or table |
| Comparative | named baseline, fairness condition, metric, and boundary |
| Causal/mechanistic | ablation, intervention, direct measurement, or explicit hypothesis wording |
| Robustness/generalization | stress test, held-out condition, cross-domain trial, or downgrade |
| Limitation | observed failure, untested condition, or declared assumption |

If support is absent, the action is not `keep`; it is `downgrade`, `delete`,
`move`, or `mark evidence needed`.

## Paragraph Story Test

For each paragraph, the sentence chain should be recoverable as:

```text
Previous basis -> paragraph job -> sentence roles -> paragraph takeaway -> next need
```

Good paragraph chains often look like:

- `context -> gap -> method route -> evidence route -> boundary`
- `method object -> mechanism -> execution condition -> safety/fallback`
- `protocol -> comparison -> observed pattern -> bounded interpretation`
- `prior route -> unresolved failure -> formulation bridge -> contribution`

If the paragraph is only a list of facts, modules, papers, or numbers, rebuild
the sentence chain before polishing wording.

## Redundancy And Missing-Sentence Tests

Ask two questions for each sentence:

1. Remove test: if removed, what exact misunderstanding or missing step appears?
2. Addition test: if a reader may jump to a wrong conclusion here, what sentence
   is needed to block that misunderstanding?

Examples:

| Problem | Diagnosis | Repair |
|---|---|---|
| `This is important.` | no function, no object | replace with the concrete failure or reader need |
| `The system has perception, planning, and control.` | module list without relation | explain the state or signal passed across modules |
| `The method improves success.` | evidence missing | add protocol and metric, or downgrade |
| `This proves robustness.` | evidence boundary exceeded | limit to tested conditions or require stress evidence |
| `Future work will apply it broadly.` | unsupported hand-off | tie future work to a stated limitation |

## Sentence Audit Output

```text
Sentence role audit
| SID | Sentence/span | Job | Claim type | Evidence anchor | Needed because | Placement | Previous link | Next obligation | Ambiguity risk | Redundancy source | AI-smell pattern | Claim-strength risk | Action | Safe rewrite | Evidence needed for stronger wording |
```

Actions are `keep`, `merge`, `move`, `split`, `add bridge`, `downgrade`, or
`delete`.

Do not hide this audit when the user asks for stronger wording, shorter prose,
top-tier polish, or reviewer-like critique. If the user asks for prose only,
include at least a minimal unsupported/ambiguity note when any sentence would
otherwise mislead the reader.
