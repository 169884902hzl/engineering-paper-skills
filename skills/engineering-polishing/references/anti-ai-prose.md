# Anti-AI Prose

Use this when text sounds generic or mechanically generated.

## Symptoms

- empty importance claims
- repeated `By ..., we ...` sentence starts
- three equal parallel clauses
- vague pronouns such as `it`, `this`, `both`, or `these` with unclear referents
- invented coined terms
- promotional adjectives without evidence
- transitions such as `Specifically` repeated as a crutch
- conclusion-like sentences inside Results
- list-like prose mistaken for reasoning
- invented intermediate steps used to make a paragraph sound complete
- claim-strength inflation during polishing, such as changing `suggests` to
  `demonstrates` without new evidence
- whole-paragraph cadence where every sentence has the same promotional rhythm
- source-note expansion: English prose contains facts not present in the notes

## Fixes

- Replace vague subjects with concrete technical nouns.
- Vary sentence length and relation.
- Convert lists into causal, contrastive, or evidence chains.
- Delete adjectives that evidence does not define.
- Replace coined terms with plain technical wording unless the paper formally
  defines the term.
- Keep one paragraph to one message.
- If the source is thin, make the prose shorter rather than inventing support.
- Preserve the original claim strength unless the user supplies stronger
  evidence.
- Report `Unsafe stronger wording rejected` when the requested polished version
  would add unsupported robustness, generality, causality, or readiness.

## Bad-to-Good Examples

Bad:

```text
The proposed system is robust, efficient, and general.
```

Better:

```text
The proposed system improves success rate in the tested occlusion regimes while
maintaining comparable cycle time.
```

Bad:

```text
This demonstrates the effectiveness of our method.
```

Better:

```text
The improvement over the fixed-camera baseline suggests that active observation
helps preserve the visual signal during the final approach.
```

## Micro Repairs

| Pattern | Bad | Better |
|---|---|---|
| empty importance | This problem is very important. | The task fails when the visual target leaves the camera view. |
| repeated transition | Specifically, the system first... Specifically, it then... | The system first... It then... |
| vague pronoun | This improves robustness. | Active observation improves success under the tested occlusion regimes. |
| coined term | We introduce a robustification module. | We add a guarded execution stage. |
| symmetric list | The method is accurate, efficient, and robust. | The method improves success while keeping cycle time within the tested range. |
| invented bridge | This naturally leads to optimal insertion. | This provides the pose estimate used by the insertion policy. |
| claim inflation | These results prove robust generalization. | These results support the method within the tested fixture and object family. |
| source expansion | The method works across industrial lighting. | The source notes do not include a lighting-change test. |
