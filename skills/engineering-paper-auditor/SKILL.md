---
name: engineering-paper-auditor
description: Audit English engineering manuscripts like a strict reviewer without drafting final prose. Use when the user asks to review, diagnose, critique, find paper weaknesses, check claim-evidence logic, inspect section boundaries, identify overclaims, assess figures/tables against claims, or produce a paper-quality action list before writing, polishing, response drafting, or validation.
---

# Engineering Paper Auditor

Use this skill to find manuscript weaknesses before rewriting. It does not
produce final paper prose; it produces a prioritized audit and repair plan.

## Core Stance

- Audit before rewriting.
- Findings must be tied to manuscript text, source evidence, figures/tables, or
  explicitly missing inputs.
- Do not invent missing experiments, references, mechanisms, line numbers, or
  completed edits.
- Separate paper-quality blockers from style notes.
- If the user asks whether the manuscript is ready, hand off to
  `engineering-validation` for build, citation, and final-readiness checks.

## Boundaries

- Use `engineering-writing` after audit findings have been turned into section
  rewrite tasks.
- Use `engineering-polishing` only after claim/evidence structure is stable.
- Use `engineering-figure-table` for detailed caption, table, or visual redesign.
- Use `engineering-response` for reviewer/advisor comment replies.
- Use `engineering-validation` for readiness, build, reference, and final status.

## When to Open Extra Files

| File | Open when |
|---|---|
| [references/audit-rubric.md](references/audit-rubric.md) | Running a full manuscript or section audit |
| [references/examples.md](references/examples.md) | Needing concrete audit output examples |
| [references/failure-modes.md](references/failure-modes.md) | Avoiding audit overreach, rewriting, or unsupported conclusions |
| [../_shared/evidence-boundary.md](../_shared/evidence-boundary.md) | Any claim may exceed available evidence |
| [../_shared/claim-strength.md](../_shared/claim-strength.md) | Auditing novelty, robustness, causality, or generalization language |
| [../_shared/citation-boundary.md](../_shared/citation-boundary.md) | Related Work, citations, or source support are part of the audit |
| [../_shared/list-to-argument.md](../_shared/list-to-argument.md) | A section reads like a list rather than an argument |
| [../_shared/sentence-role-and-story-flow.md](../_shared/sentence-role-and-story-flow.md) | A paragraph may contain redundant, misplaced, missing, or disconnected sentences |
| [../_shared/terminology-ledger.md](../_shared/terminology-ledger.md) | Terms, metrics, categories, or method names drift across sections |

## Workflow

1. Identify the audit scope: full paper, section, figure/table set, response
   package, or claim-evidence map.
2. Extract the paper's one-sentence thesis and stated contributions if present.
3. Build a claim-evidence audit table.
4. Check section jobs: Abstract, Introduction, Related Work, Methods,
   Experiments, Discussion, Conclusion.
5. Check figure/table responsibility against the claims they are asked to
   support.
6. Audit sentence roles when a paragraph is unclear: every sentence must be
   necessary, placed correctly, connected to neighboring sentences, and bounded
   by evidence.
7. Flag overclaims, missing anchors, section drift, table narration, caption
   overreach, sentence redundancy, terminology drift, and unsupported readiness
   claims.
8. Produce a prioritized action list and route each action to the correct skill.

## Default Output

```text
Audit verdict
- Overall status: PASS / PASS_WITH_BLOCKERS / CANNOT_DETERMINE
- Highest-risk issue:
- Not verified:

Claim-evidence audit
| Claim | First stated | Method anchor | Experiment anchor | Figure/table anchor | Status | Repair route |

Section-boundary findings
| Location | Symptom | Why it matters | Repair route |

Sentence role findings
| Sentence/span | Job | Needed because | Connection issue | Evidence boundary | Action |

Figure/table findings
| Item | Claim requested | Evidence visible/tabulated | Must not claim | Repair route |

Prioritized action list
| Priority | Action | Owner skill | Required input | Stop condition |
```
