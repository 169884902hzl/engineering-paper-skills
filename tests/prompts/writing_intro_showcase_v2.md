# Introduction Showcase V2 Prompt

Use $engineering-writing to draft a showcase-grade Introduction opening.

Target section:
Introduction opening, two paragraphs.

Paper type:
Robotics / engineering conference paper.

Task:
Contact-rich robotic insertion under partial visual occlusion.

Core bottleneck:
The hard part is not generic perception accuracy. The visible alignment cue
changes as the peg approaches the hole, exactly when contact makes recovery
less forgiving.

Existing routes and limitations:

- Fixed overhead RGB-D: can initialize alignment early, but the peg can occlude
  the hole during final approach.
- Fixed side RGB-D: improves lateral visibility, but can leave depth uncertainty
  unresolved.
- Open-loop insertion: executes efficiently, but carries uncertain pose
  estimates into contact.
- Force-guarded control: can stop unsafe contact, but does not resolve the
  upstream visual ambiguity that caused the uncertain pose.

Method:
Confidence-triggered multi-view insertion estimates insertion pose and
confidence from overhead and side RGB-D observations, requests another view when
confidence is low, refines the pose estimate, and executes with force and
pose-deviation stops.

Evidence:

- The full system later evaluates at 84% success over 180 trials.
- Baselines: fixed overhead 69%, fixed side 72%, open-loop 61%.
- Remaining failures occur when all available views are ambiguous or contact
  produces large pose deviation.

Boundary:

- One 7-DoF robot arm.
- One tabletop fixture.
- One cylindrical peg family.
- No statistical significance test.
- No cross-robot or deployment evaluation.

Forbidden claims:

- Do not claim solved insertion.
- Do not claim broad robustness.
- Do not claim deployment readiness.
- Do not claim verified novelty over all prior work.

Style requirements:

- Produce manuscript prose first.
- Open with a concrete operational difficulty, not `X remains challenging`.
- Explain why existing routes fail as the execution stage changes.
- Motivate the method as a formulation, not as a module list.
- Keep result numbers secondary; this is an Introduction opening.
- The final draft should sound like manuscript prose, not audit prose.
