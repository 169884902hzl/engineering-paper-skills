---
name: engineering-polishing
description: Polish, restructure, or translate source notes into English engineering manuscript prose while preserving evidence boundaries. Use when the user asks to improve English academic style, paragraph flow, claim strength, anti-AI wording, terminology consistency, hedging, clarity, or publication-ready expression for engineering conference or journal papers.
---

# Engineering Polishing

Use this skill after the paper's claim and evidence are known. It improves
English manuscript prose without hiding structural or evidence problems.

## Core Stance

- Final output defaults to English manuscript prose.
- Do not invent facts, references, mechanisms, experiments, numbers, novelty, or
  limitations.
- Do not polish a broken argument as if it were correct.
- Diagnose the failure mode before rewriting.
- Preserve technical terms, variables, units, metric definitions, and evidence
  boundaries.
- Prefer restrained, concrete academic English over promotional language.

## When to Open Extra Files

| File | Open when |
|---|---|
| [references/fact-boundary.md](references/fact-boundary.md) | The source is a rough skeleton, non-English notes, or evidence is incomplete |
| [references/paragraph-function.md](references/paragraph-function.md) | Identifying paragraph job before rewriting |
| [references/engineering-topic-modules.md](references/engineering-topic-modules.md) | Polishing control, algorithm, data-driven, materials, process, or multi-physics paragraphs |
| [references/list-handling.md](references/list-handling.md) | Turning long lists of methods, challenges, advantages, or chapter plans into arguments |
| [references/paragraph-flow.md](references/paragraph-flow.md) | Paragraphs feel unclear, repetitive, poorly ordered, or hard to follow |
| [references/claim-strength.md](references/claim-strength.md) | Claims may overstate evidence, causality, robustness, generalization, or novelty |
| [references/anti-ai-prose.md](references/anti-ai-prose.md) | Text sounds generic, repetitive, slogan-like, template-like, or model-generated |
| [references/style-guardrails.md](references/style-guardrails.md) | Need sentence-level academic English, transitions, hedging, terminology, or mechanics |

## Workflow

1. Identify the section and paragraph job.
2. Apply fact-boundary checks when source notes are thin.
3. Diagnose the main problem:
   paper logic, section job, paragraph flow, claim/evidence mismatch, or
   sentence style.
4. Fix higher-level logic before sentence polish.
5. Preserve source facts and evidence boundaries.
6. Rewrite in English with concrete subjects, varied sentence shapes, and
   calibrated verbs.
7. Report any claim that still needs evidence.

## Default Output

```text
Polished version
[English prose]

Notes
- Claim/evidence issue:
- Terminology issue:
- Remaining risk:
```

If the user asks for output only, return only the polished prose.
