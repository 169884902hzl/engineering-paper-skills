# Engineering Polishing Examples

## Claim Downgrade

Input:

```text
Our method proves the mechanism and is totally robust. It improves success from
71% to 86%.
```

Expected behavior:

- Preserve `71%` and `86%`.
- Downgrade unsupported wording such as `proves` and `totally robust`.
- Do not add a mechanism or new experimental context.

Possible output:

```text
The results support the effectiveness of the proposed method, with success
increasing from 71% to 86% under the evaluated conditions.
```

## Source Notes To English

Input:

```text
Problem: pose noise hurts insertion.
Method: guarded execution after visual alignment.
Result: fewer failed contacts.
Guess: the observer probably improves contact reasoning.
```

Expected behavior:

- Produce English manuscript prose.
- Preserve the provided facts.
- Mark missing numbers or experimental conditions if the user wants a stronger
  claim.
- Do not state the guessed mechanism as fact.

Possible output:

```text
Guarded execution after visual alignment is used to reduce failed contacts
under pose noise. The available notes do not specify the evaluation protocol or
failure count, so the paragraph should not claim a measured improvement without
additional evidence.
```

## Logic Diagnosis Before Polish

Input:

```text
This paragraph says the method is robust, but no robustness test is given.
```

Expected behavior:

- Do not polish it into a stronger claim.
- Explain that the claim/evidence relation is broken.
- Offer a conservative rewrite or ask for robustness evidence.

Possible output:

```text
Diagnosis
- Paragraph job: results interpretation
- Main issue: robustness claim lacks a robustness test
- Evidence risk: final prose would overstate the available result

Polished version
The current evidence supports improved performance under the evaluated
condition, but it does not establish robustness across untested conditions.
```

## Paragraph-Level Flow Repair

Input:

```text
The controller improves the task. It has an observer camera. The baseline is
lower. This is important. The observer camera, active view, and auxiliary camera
make the method robust.
```

Expected behavior:

- Lock terminology to one component name.
- Move from claim to mechanism to evidence to boundary.
- Remove unsupported robustness unless a robustness test is provided.

Possible output:

```text
Terminology ledger
| Canonical term | Current variants found | Decision |
| observer camera | observer camera, active view, auxiliary camera | use observer camera |

Polished version
The controller uses an observer camera to maintain task-relevant visual input
during execution. Compared with the provided baseline, the method achieves a
higher task success rate under the evaluated condition; broader robustness
requires stress-test evidence.
```

## Before / After / Rationale Example

| Source sentence | Revised sentence | Rationale | Fact/evidence risk |
|---|---|---|---|
| Our method proves robustness in clutter. | The results support improved performance in the tested clutter regimes. | Downgrades `proves` and narrows the scope. | Does not claim untested regimes. |
| It uses an active camera, observer arm, and visual module. | It uses an active observer camera. | Locks terminology to one object. | Requires confirmation that these names refer to the same component. |

## Anti-AI Rhythm Repair

Input:

```text
Specifically, the method is robust, efficient, and accurate. Specifically, this
demonstrates the superiority of our framework.
```

Expected behavior:

- Remove repeated `Specifically`.
- Replace promotional adjectives with measured outcomes.
- Keep only claims supported by provided metrics.

## Sentence-By-Sentence Story Repair

Input:

```text
The proposed system is useful for contact-rich manipulation. It uses perception,
planning, and guarded control. The success rate is higher. This shows strong
robustness. The method may be extended to many domains.
```

Expected behavior:

- Assign a job to every sentence.
- Delete or merge generic sentences that add no evidence, transition, or
  boundary.
- Add a missing bridge if module names are listed without explaining how the
  information flows.
- Downgrade robustness and future-domain claims unless stress evidence is
  provided.

Possible output:

```text
Sentence role audit
| Sentence/span | Job | Needed because | Connection to previous/next | Evidence boundary | Action |
| The proposed system is useful... | Context | too generic as written | does not set a specific failure | no evidence | rewrite |
| It uses perception... | Method object | names components | lacks signal flow | method note only | add bridge |
| The success rate is higher. | Evidence | needs metric and protocol | supports local result | missing number/protocol | require evidence |
| This shows strong robustness. | Interpretation | overstates result | jumps beyond evidence | no stress test | downgrade |
| The method may be extended... | Outlook | not needed here | unsupported broad hand-off | no domain evidence | delete or make limitation-derived |

Polished version
The system addresses contact-rich manipulation by linking perception outputs to
guarded control decisions during execution. The available notes indicate a
higher success rate, but the result should be tied to the measured protocol
before making a final performance claim. Broader robustness or domain transfer
requires stress-test evidence.
```
