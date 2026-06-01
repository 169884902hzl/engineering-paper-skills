# Demo Prompt: Claim Audit

Use `skills/engineering-paper-coach/SKILL.md` as the governing skill.

This is a recorded local demo prompt. Produce Markdown only. Do not edit files.
Do not invent experiments, citations, figures, deployment evidence, statistics,
or venue readiness.

## Task

Audit the draft claim and give a safe rewrite for a robotics paper.

## Evidence

- Task: contact-rich peg insertion under partial visual occlusion.
- System: multi-view RGB-D observation with guarded execution.
- Result: 84% success over 180 trials.
- Robot: one 7-DoF robot arm.
- Fixture: one tabletop fixture.
- Object family: one cylindrical peg family.
- Baselines:
  - fixed overhead RGB-D camera: 69% success.
  - fixed side RGB-D camera: 72% success.
  - open-loop insertion controller: 61% success.
- No cross-robot evaluation.
- No industrial cell evaluation.
- No occlusion severity sweep.
- No confidence intervals or statistical significance test.
- No ablation that isolates view selection from guarded execution.

## Draft claim

"The proposed active-observation system is a deployment-ready and robust
industrial insertion method that proves active observation is the key mechanism
for general manipulation under occlusion."

## Required output

Use this structure:

1. Diagnosis
2. Claim-strength audit
3. Safe rewrite
4. What stronger claims would require
5. What not to say
