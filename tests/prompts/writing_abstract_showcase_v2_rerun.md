# Abstract Showcase V2 Rerun Prompt

Use $engineering-writing to draft a showcase-grade Abstract.

Target section:
Abstract, exactly six sentences.

Paper type:
Robotics / engineering conference paper.

Task:
Contact-rich peg insertion under partial visual occlusion.

Core bottleneck:
Peg-hole alignment cues degrade near contact, and a fixed or open-loop policy
can carry pose error into the least recoverable part of the motion.

Method:
Confidence-triggered multi-view insertion treats insertion pose and confidence
as the state to update before contact-rich execution. The system estimates pose
and confidence from overhead and side RGB-D observations, requests an additional
view when confidence is low, refines the pose estimate, and executes with a
guarded insertion controller that stops on force or pose-deviation limits.

Evidence:

- 84% success over 180 real-robot trials.
- Fixed overhead baseline: 69%.
- Fixed side baseline: 72%.
- Open-loop baseline: 61%.
- Remaining failures: fully ambiguous views and large contact-induced pose
  deviation.

Boundary:

- One 7-DoF robot arm.
- One tabletop fixture.
- One cylindrical peg family.
- No confidence intervals.
- No statistical significance test.
- No cross-robot evaluation.
- No industrial deployment evaluation.

Forbidden wording and claims:

- Do not introduce lateral jamming, jamming, binding, slip, compliance,
  deformation, fatigue, impact, or any physical mechanism not supplied above.
- Do not add unsupported physics.
- Do not claim statistical significance.
- Do not claim cross-robot generalization.
- Do not claim deployment readiness.
- Do not claim universal robustness.
- Do not use `without claiming`.

Style requirements:

- Produce manuscript prose first.
- Write exactly six sentences.
- Use a concrete supplied failure mode in the opening.
- Name the method object and information flow.
- Evidence boundary should be expressed as evaluation scope.
- Final sentence must be scope-aware, not disclaimer-like.
- The final draft should sound like manuscript prose, not audit prose.
