# Page Budget War Plan

Use this when a manuscript is over length. Cutting should protect evidence
anchors before improving style.

## Protected Anchors

Do not cut these first:

- one-sentence thesis and contribution list
- formulation bridge in Introduction
- method contract and main mechanism
- metric definitions and baseline fairness
- main result, ablation, and failure boundary
- caption/table notes needed to interpret evidence
- limitation that bounds the main claim

## Cut Order

| Priority | Cut target | Safe action | Risk |
|---|---|---|---|
| P1 | Repeated motivation | Merge duplicate problem statements | Low |
| P1 | Setup prose duplicated in tables | Move to setup table or table note | Low |
| P1 | Caption prose repeating body text | Keep visible evidence only | Low |
| P2 | Long Related Work inventory | Convert to axes and nearest-neighbor contrast | Medium |
| P2 | Implementation detail | Move to appendix or setup table if venue allows | Medium |
| P3 | Experiment subsections | Compress only after preserving Q1/Q2/Q3 evidence | High |
| P3 | Methods explanation | Cut examples before cutting mechanism | High |

## Forbidden Cut

Do not cut evenly across all sections. Even cuts often remove the exact sentence
that makes a claim verifiable.

## Output Pattern

```text
Page-budget plan
| Section | Current risk | Cut action | Protected anchor | Verification after cut |
```
