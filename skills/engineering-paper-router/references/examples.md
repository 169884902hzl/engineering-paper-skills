# Engineering Paper Router Examples

## Ambiguous Paper Revision

Input:

```text
Please improve my paper before submission.
```

Expected route:

```text
Recommended route
- Primary skill: engineering-validation
- Secondary skill: engineering-writing or engineering-polishing after blockers are known

Do not use first
| Skill | Why not primary |
| engineering-polishing | Readiness is unknown; polishing can hide structural blockers. |

Workflow order
| Step | Skill | Required input | Stop condition |
| 1 | engineering-validation | manuscript root, build command, target venue | stop if live draft is unknown |
| 2 | engineering-writing | validation blockers | stop if evidence is missing |
| 3 | engineering-polishing | stable revised text | stop if logic remains broken |
```

## Mixed Drafting Task

Input:

```text
I have method notes, result tables, and figure captions. Help me turn them into
a paper section plan.
```

Expected route:

- Primary: `engineering-writing`
- Secondary: `engineering-figure-table`
- Stop before final Abstract until contribution-evidence and figure/table
  responsibilities are defined.

## Reviewer Comments Plus Visual Issue

Input:

```text
Reviewer 2 says our ablation is weak and the caption overclaims robustness.
```

Expected route:

- Primary: `engineering-response`
- Secondary: `engineering-figure-table`
- Validation dependency: final response cannot claim changes until revised
  manuscript locations and line-number status are known.

## Figure Caption Plus Results Prose

Input:

```text
The result table has full and ablated success rates, and Fig. 5 shows the
workflow. The caption should say it proves robustness; the Results paragraph
also needs rewriting.
```

Expected route:

- Primary: `engineering-figure-table` for caption claim boundary.
- Secondary: `engineering-writing` for Results paragraph structure.
- Stop condition: do not use robustness wording unless stress or
  cross-condition evidence is provided.

## Source Notes To English Paper Text

Input:

```text
I have rough non-English notes with facts, guesses, and partial results. Turn
them into paper text.
```

Expected route:

- Primary: `engineering-writing` if a section argument is needed.
- Secondary: `engineering-polishing` only after the paragraph job and evidence
  boundary are stable.
- Required input: facts, assumptions, unsupported items, target section.

## Final Submission Check

Input:

```text
The paper reads well. Check whether it is ready for submission.
```

Expected route:

- Primary: `engineering-validation`
- Secondary: none until validation blockers are known.
- Stop condition: if build, citations, claim-evidence anchors, or live draft are
  not checked, overall readiness cannot be `READY`.
