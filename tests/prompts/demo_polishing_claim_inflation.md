# Demo Prompt: Conservative Polishing

Use `skills/engineering-polishing/SKILL.md` as the governing skill.

This is a recorded local demo prompt. Produce Markdown only. Do not edit files.
Do not invent experiments, citations, mechanisms, deployment evidence,
statistics, or venue readiness.

## Task

Polish the draft paragraph for an English engineering paper while preserving
the evidence boundary. Diagnose claim inflation before rewriting.

## Draft paragraph

"Our method is a robust and general solution for insertion. It works well in
realistic settings and shows strong performance against baselines. This
demonstrates that active observation is an effective mechanism for industrial
manipulation."

## Evidence

- Task: contact-rich peg insertion under partial visual occlusion.
- Full system: 84% success over 180 trials.
- Fixed overhead RGB-D camera: 69% success.
- Fixed side RGB-D camera: 72% success.
- Open-loop controller: 61% success.
- One robot arm.
- One tabletop fixture.
- One cylindrical peg family.
- No industrial test.
- No cross-robot test.
- No statistical significance test.
- No causal ablation isolating active observation.

## Required output

Use this structure:

1. Diagnosis
2. Claim-strength diff
3. Polished paragraph
4. Unsupported wording removed
5. Remaining evidence needed
