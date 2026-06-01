# Demo Prompt: Results Paragraph

Use `skills/engineering-writing/SKILL.md` as the governing skill.

This is a recorded local demo prompt. Produce Markdown only. Do not edit files.
Do not invent experiments, citations, figures, statistics, objects, venues, or
deployment evidence.

## Task

Draft a Results paragraph and include a short claim-evidence note. The paragraph
should be usable in an English robotics conference paper only if the evidence
supports it.

## Experiment question

Does the proposed multi-view guarded insertion system improve insertion success
over fixed-view and open-loop variants in the tested tabletop occlusion setup?

## Protocol and results

- Full system: 84% success over 180 trials.
- Fixed overhead RGB-D camera: 69% success.
- Fixed side RGB-D camera: 72% success.
- Open-loop controller: 61% success.
- All trials use one 7-DoF robot arm, one tabletop fixture, and one cylindrical
  peg family.

## Boundary

- No confidence intervals.
- No per-condition trial counts beyond the full-system count.
- No statistical significance test.
- No object-family variation.
- No cross-robot evaluation.
- No industrial deployment test.
- No ablation that separates view selection from guarded execution.

## Required output

Use this structure:

1. Experiment question
2. Manuscript paragraph
3. Claim-evidence note
4. Claims to avoid
