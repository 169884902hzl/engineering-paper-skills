# Conclusion Showcase V2 Prompt

Use $engineering-writing to draft a showcase-grade Conclusion.

Target section:
Conclusion, exactly two paragraphs.

Paper type:
Robotics / engineering conference paper.

Task:
Contact-rich peg insertion under partial visual occlusion.

Core bottleneck:
The conclusion should recover the system-level contribution and state a
specific operating boundary, not end as a disclaimer.

Method:
Confidence-triggered multi-view insertion estimates insertion pose and
confidence from overhead and side RGB-D observations, requests another view when
confidence is low, refines the pose estimate, and uses guarded execution with
force and pose-deviation stops.

Evidence:

- Full system: 84% success over 180 trials.
- Fixed overhead camera: 69%.
- Fixed side camera: 72%.
- Open-loop controller: 61%.
- The study does not isolate view selection from guarded execution.
- Remaining failures occur when all available views are ambiguous or when
  contact produces large pose deviation.

Boundary:

- One 7-DoF robot arm.
- One tabletop fixture.
- One cylindrical peg family.
- No statistical significance test.
- No cross-robot evaluation.
- No deployment study.
- No isolated component causality.

Forbidden claims:

- Do not claim deployment readiness.
- Do not claim broad robustness.
- Do not claim causal proof for view selection or guarded execution.
- Do not introduce new results or new method terms.

Style requirements:

- Produce manuscript prose first.
- Use two paragraphs.
- Paragraph 1: method object, strongest evidence, bounded takeaway.
- Paragraph 2: concrete operating boundary and future work derived from failure
  regimes.
- Avoid the sentence `The remaining failures identify the current operating
  boundary.`
- Final draft should sound like manuscript prose, not audit prose.
