# Abstract From Rich Evidence Prompt

Use $engineering-writing to draft a six-sentence Abstract.

This is a showcase-grade WRITE request. Produce manuscript prose first.

Task:
Contact-rich robotic insertion under partial visual occlusion.

Problem:
Alignment cues degrade during final approach, and pose errors become hard to
recover after contact begins.

Prior limitations:

- Fixed overhead and side cameras cannot actively recover task-relevant
  visibility.
- Open-loop insertion does not react to pose uncertainty or contact deviation.
- Force-guarded controllers can stop unsafe motion but do not resolve upstream
  visual ambiguity.

Method:
Confidence-triggered multi-view insertion. The system estimates insertion pose
and confidence from overhead and side RGB-D observations, requests an additional
view when confidence is low, refines the pose estimate, and executes insertion
with force and pose-deviation guards.

Evidence:
84% success over 180 real-robot trials.
Baselines: fixed overhead 69%, fixed side 72%, open-loop 61%.

Boundary:
One 7-DoF robot arm, one tabletop fixture, one cylindrical peg family, no
statistical significance test, no cross-robot test, no deployment test.

Requirements:

- Six sentences only.
- Sentence 1: task difficulty.
- Sentence 2: concrete failure consequence.
- Sentence 3: method.
- Sentence 4: main pipeline.
- Sentence 5: execution/safety grounding.
- Sentence 6: evidence and boundary.
- Do not claim deployment readiness, broad robustness, statistical
  significance, or general novelty proof.
