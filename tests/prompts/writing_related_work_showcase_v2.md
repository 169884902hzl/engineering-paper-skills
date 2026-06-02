# Related Work Showcase V2 Prompt

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
The paragraph should distinguish technical axes and nearest-neighbor
assumptions without making an unverified novelty claim.

Existing routes and limitations:

- Fixed-view insertion systems: support repeatable manipulation under controlled
  sensing geometry, but the observation geometry is chosen before visibility
  changes near contact.
- Active perception for manipulation or inspection: acquires additional views,
  but the supplied notes frame them around object coverage or detection
  confidence rather than insertion-pose refinement coupled to guarded execution.
- Force-guarded insertion controllers: detect unsafe contact and can stop or
  slow motion, but do not resolve upstream visual pose ambiguity.
- Closest neighboring line: perception with guarded insertion, but the supplied
  notes do not verify the same-loop combination of confidence-triggered view
  acquisition, insertion-pose refinement, and force/pose guarded execution.

Evidence:

- Citation placeholders available: [FixedViewInsertion],
  [ActivePerceptionManipulation], [ForceGuardedInsertion],
  [PerceptionGuardedInsertion].
- Exact citations and protocols are not verified in this prompt.

Boundary:

- Placeholder citations only.
- No verified nearest-neighbor citation audit.
- No proven novelty claim.
- No claim that prior work lacks a feature unless the prompt states it.

Forbidden claims:

- Do not claim definitive novelty.
- Do not claim prior work failed unless tied to supplied assumptions.
- Do not use meta-language such as `pending verified citations and protocols`
  as the manuscript sentence frame.

Style requirements:

- Produce manuscript prose first.
- Write technical-axis positioning, not paper-by-paper summary.
- Use citation placeholders where needed.
- End with a manuscript-ready bounded positioning sentence.
- Put verification needs after the draft if needed, not inside the manuscript
  prose.
- The final draft should sound like manuscript prose, not audit prose.
