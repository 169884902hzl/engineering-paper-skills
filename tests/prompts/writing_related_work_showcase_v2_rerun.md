# Related Work Showcase V2 Rerun Prompt

Use $engineering-writing to draft a showcase-grade Related Work positioning
paragraph.

Target section:
Related Work.

Paper type:
Robotics / engineering conference paper.

Task:
Position a contact-rich insertion pipeline that combines confidence-triggered
view acquisition, insertion-pose refinement, and guarded execution.

Core bottleneck:
Distinguish technical axes and nearest-neighbor assumptions without making an
unverified novelty claim.

Existing routes and limitations:

- Fixed-view insertion systems: support repeatable manipulation under controlled
  sensing geometry, but the observation geometry is chosen before visibility
  changes near contact.
- Active perception for manipulation or inspection: acquires additional views,
  but the notes frame them around object coverage or detection confidence
  rather than insertion-pose refinement coupled to guarded execution.
- Force-guarded insertion controllers: detect unsafe contact and can stop or
  slow motion, but do not resolve upstream visual pose ambiguity.
- Closest neighboring line: perception with guarded insertion, but the notes do
  not verify the same-loop combination of confidence-triggered view acquisition,
  insertion-pose refinement, and force/pose guarded execution.

Citation placeholders:
[FixedViewInsertion], [ActivePerceptionManipulation], [ForceGuardedInsertion],
[PerceptionGuardedInsertion].

Boundary:

- Placeholder citations only.
- No verified nearest-neighbor citation audit.
- No proven novelty claim.
- No claim that prior work lacks a feature unless the prompt states that
  assumption.

Forbidden wording and claims:

- Do not claim definitive novelty.
- Do not claim prior work failed unless tied to supplied assumptions.
- Do not write `supplied notes`, `supplied positioning`, `available evidence`,
  `without claiming`, `pending verified citations`, `Unsupported`, or
  `not verified` inside the manuscript paragraph.
- Do not discuss citation verification inside the manuscript paragraph.

Style requirements:

- Produce manuscript prose first under `## Draft`.
- Use citation placeholders.
- Write technical-axis positioning, not a paper-by-paper summary.
- End with a bounded technical gap bridge.
- Put verification needs after the draft under `## Evidence boundary`, not
  inside the draft.
- The draft should sound like manuscript prose, not audit prose.
