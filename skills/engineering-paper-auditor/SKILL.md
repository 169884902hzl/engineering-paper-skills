---
name: engineering-paper-auditor
description: Audit English engineering manuscripts like a strict reviewer without drafting final prose. Use when the user asks to review, diagnose, critique, find paper weaknesses, check claim-evidence logic, inspect section boundaries, identify overclaims, assess figures/tables against claims, produce a paper-quality action list before writing, polishing, response drafting, or validation, predict what reviewers will attack, or run a pre-mortem on an experiment plan, proposal, or results-table skeleton before the experiments finish.
---

# Engineering Paper Auditor

Use this skill to find manuscript weaknesses before a reviewer does. It does
not produce final paper prose; it produces a ranked list of objections and the
cheapest fixes.

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
| [../_shared/reviewer-attack-patterns.md](../_shared/reviewer-attack-patterns.md) | Any pre-submission review or reviewer simulation |
| [../_shared/experiment-premortem.md](../_shared/experiment-premortem.md) | An experiment plan, proposal, or results-table skeleton exists but experiments are not finished |
| [references/audit-rubric.md](references/audit-rubric.md) | Running a full manuscript or section audit |
| [references/examples.md](references/examples.md) | Needing concrete audit output examples |
| [references/failure-modes.md](references/failure-modes.md) | Avoiding audit overreach, rewriting, or unsupported conclusions |
| [references/story-continuity-audit.md](references/story-continuity-audit.md) | Auditing whether paper sections form a coherent story |
| [references/paragraph-to-paragraph-transition-audit.md](references/paragraph-to-paragraph-transition-audit.md) | Paragraphs are individually plausible but the section feels jumpy |
| [references/claim-resurrection-audit.md](references/claim-resurrection-audit.md) | Abstract, Discussion, or Conclusion may revive unsupported claims |
| [references/scored-audit-mode.md](references/scored-audit-mode.md) | The user explicitly asks for scores, a scored review panel, or a scored reviewer simulation |
| [../_shared/story-spine.md](../_shared/story-spine.md) | Full-paper or multi-section audit needs story dependency checks |
| [../_shared/evidence-boundary.md](../_shared/evidence-boundary.md) | Any claim may exceed available evidence |
| [../_shared/claim-strength.md](../_shared/claim-strength.md) | Auditing novelty, robustness, causality, or generalization language |
| [../_shared/citation-boundary.md](../_shared/citation-boundary.md) | Related Work, citations, or source support are part of the audit |
| [../_shared/ai-assisted-writing-policy.md](../_shared/ai-assisted-writing-policy.md) | The audit may need to flag AI-smell, disclosure, or author-verification risk |
| [../_shared/list-to-argument.md](../_shared/list-to-argument.md) | A section reads like a list rather than an argument |
| [../_shared/sentence-role-and-story-flow.md](../_shared/sentence-role-and-story-flow.md) | A paragraph may contain redundant, misplaced, missing, or disconnected sentences |
| [../_shared/terminology-ledger.md](../_shared/terminology-ledger.md) | Terms, metrics, categories, or method names drift across sections |

## Reviewer Simulation (Default For Pre-Submission Review)

Use this whenever the user asks what reviewers will say, whether the paper is
convincing, or for a pre-submission check.

1. Read the manuscript as a skeptical reviewer from the closest neighboring
   field. Ask what that reviewer would compare the work against: the simplest
   alternative configuration, the principled method from the adjacent field,
   and a baseline given the same capability or prior.
2. Walk the patterns in
   [reviewer-attack-patterns.md](../_shared/reviewer-attack-patterns.md) as
   prompts. Report any problem the manuscript gives evidence for, whether or
   not a pattern names it; skip patterns that are not triggered.
3. Rank by what real reviewers lead with. In observed review sets, reviewers
   led with comparison validity (handicapped baselines), reliance on
   unvalidated assumptions or components, and practical cost (hardware, time,
   compute). In a small blind test, models without the pattern checklist
   often put internal-consistency checks (numeric slips, metric definitions)
   at the top and pushed the reviewers' main objection down to rank 2-7. Rank
   by consequence instead: a numeric or metric error that changes a headline
   number, a comparison, or reproducibility belongs with the major
   objections; only non-substantive slips go to the mechanical list.
4. Give the three objections most likely to appear in an actual report first,
   then at most seven more. Long undifferentiated lists hide the objections
   that decide the outcome.
5. For each objection, give the cheapest pre-submission fix: a matched
   control, a measurement, an operating-envelope paragraph, a wording change,
   or a reframing of a weak baseline as a reference configuration.

```text
Reviewer simulation
| Rank | Pattern | Trigger in manuscript | Objection as a reviewer would write it | Cheapest fix before submission |

Mechanical issues: [non-substantive slips: typos, labels that resolve correctly, formatting]
Not triggered: [pattern ids]
Needs author input: [facts the manuscript does not state]
```

## Experiment Plan Pre-mortem (Before Experiments)

Use this when an experiment plan, a proposal, or a results-table skeleton
exists but the experiments are not finished. Follow
[experiment-premortem.md](../_shared/experiment-premortem.md): map each claim
to the comparison that would support it, plan matched controls, measurements,
logging, and trial counts against P1-P6 and P8, and return the plan table,
the cheapest additions, and the claims to drop or narrow now. Choose the mode
by what is being reviewed: experiments still to be run get the pre-mortem;
arguments and results already written get Reviewer Simulation. A draft with
partial results can need both.

## Detailed Audit (On Request)

Use when the user asks for a claim-by-claim or section-by-section audit.

1. Identify the audit scope: full paper, section, figure/table set, response
   package, or claim-evidence map.
2. Extract the one-sentence thesis and stated contributions.
3. Build the claim-evidence and story-spine audits before local style notes.
4. Check section jobs and figure/table responsibility against the claims they
   are asked to support.
5. Flag overclaims, missing anchors, section drift, table narration, caption
   overreach, terminology drift, and unsupported readiness claims.
6. Produce a prioritized action list and route each action to the right skill.

```text
Audit verdict
- Overall status: PASS / PASS_WITH_BLOCKERS / CANNOT_DETERMINE
- Highest-risk issue:
- Not verified:

Claim-evidence audit
| Claim | First stated | Method anchor | Experiment anchor | Figure/table anchor | Status | Repair route |

Prioritized action list
| Priority | Action | Owner skill | Required input | Stop condition |
```

## Scored Audit Mode

Off by default. Use it only when the user explicitly asks for scores, a
review panel, or scored reviewer simulation. The protocol, lens table, and
band anchors are in
[references/scored-audit-mode.md](references/scored-audit-mode.md).

- Three reviewer lenses pass independently: method rigor, experimental
  evidence, contribution and positioning.
- Bands are heuristic triage anchored to listed findings, not acceptance
  predictions; no weighted total is produced.
- Material that was not inspected is `CANNOT_DETERMINE`, not a low band.
