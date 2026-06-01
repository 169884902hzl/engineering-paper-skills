# Fixture: Results Table Narration

## Flawed manuscript input

Table 1 shows the success rates. Our method has 86% success. The fixed-camera
baseline has 71% success. The method without guarded execution has 74% success.
The method without the observer camera has 78% success. The result shows that
our framework is robust and general. The ablation demonstrates that each module
is important. Fig. 4 shows qualitative examples of successful insertion.

The paragraph reads numbers aloud but does not ask an evaluation question. It
does not state the protocol, object family, number of trials, confidence
interval, or failure condition. The ablation interpretation is too broad:
removing one component and observing a lower success rate supports a component
role, but it does not by itself prove robustness or generalization. The
qualitative figure may illustrate behavior but cannot establish mechanism or
causality.

## Expected audit pressure

The skill should rewrite around questions: overall performance, observer-camera
contribution, guarded-execution contribution, and failure boundary. It should
preserve numbers but attach each to a claim and boundary. It should downgrade
robustness/generalization unless stress tests exist.

## Failure modes

- Table narration.
- Result without protocol.
- Ablation overinterpreted as mechanism proof.
- Qualitative examples treated as causal evidence.
