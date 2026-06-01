# Demo Prompt: Related Work Nearest-Neighbor Distinction

Use `skills/engineering-writing/SKILL.md` as the governing skill.

This is a recorded local demo prompt. Produce Markdown only. Do not edit files.
Do not invent paper titles, authors, citations, experiments, or claims.

## Task

Turn the supplied related-work notes into a technical positioning plan. Do not
write fake citations. Identify nearest neighbors, the axes of distinction, and
what evidence is missing before the paper can make a strong novelty claim.

## Paper under development

- Task: contact-rich insertion under partial visual occlusion.
- Proposed system: multi-view RGB-D observation requests an additional view when
  confidence is low; guarded execution stops under force or pose-deviation
  limits.
- Evidence: one tabletop robot setup; 84% success over 180 trials; fixed-view
  and open-loop baselines.

## Prior-work notes supplied by author

- Group A: fixed-camera insertion systems. They use one overhead or side camera
  and do not request additional views during execution.
- Group B: active perception for manipulation. They choose viewpoints for
  grasping or inspection, but the author has not supplied evidence that they
  handle contact-rich insertion.
- Group C: force-guarded insertion controllers. They stop or adjust based on
  force thresholds, but the author has not supplied evidence that they use
  view-request policies.
- Group D: industrial insertion systems. The author has not supplied exact
  citations or comparable protocols.

## Required output

Use this structure:

1. Related-work risk diagnosis
2. Technical axes table
3. Nearest-neighbor distinction
4. Safe Related Work paragraph scaffold
5. Citation/evidence still needed
