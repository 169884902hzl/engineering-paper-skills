# Demo Prompt: Figure And Table Claim Check

Use `skills/engineering-figure-table/SKILL.md` as the governing skill.

This is a recorded local demo prompt. Produce Markdown only. Do not edit files.
Do not invent panels, source data, statistics, or deployment evidence.

## Task

Audit whether the figure, table, caption, and result prose support the stated
claims.

## Figure 3

- Panel A: workflow diagram showing RGB-D observation, confidence estimate,
  view request, guarded execution, and stop states.
- Panel B: a single qualitative sequence from one successful tabletop insertion
  trial.
- Panel C: bar chart with success rates:
  - full system: 84%.
  - fixed overhead camera: 69%.
  - fixed side camera: 72%.
  - open-loop controller: 61%.
- Panel C does not show confidence intervals, error bars, or per-condition trial
  counts.

## Table 1

| Method | Success rate | Trials shown |
|---|---:|---:|
| Full system | 84% | 180 |
| Fixed overhead camera | 69% | not stated |
| Fixed side camera | 72% | not stated |
| Open-loop controller | 61% | not stated |

## Draft caption

"Figure 3 proves that active observation robustly solves industrial insertion
under occlusion. The results validate the causal role of view selection and show
deployment-ready performance."

## Draft result prose

"The full system significantly outperforms all baselines and demonstrates robust
generalization to realistic insertion settings."

## Required output

Use this structure:

1. Verdict
2. Panel/table responsibility map
3. Unsupported caption/prose claims
4. Safe caption
5. Safe result prose
6. Source-data checks required before stronger claims
