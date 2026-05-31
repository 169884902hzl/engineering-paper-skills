# Engineering Response Failure Modes

| Symptom | Bad output | Correct behavior | Required file/reference | Test prompt |
|---|---|---|---|---|
| False completed change | "We added the experiment" when it was not run | Refuse and mark Planned/Needs input/Not supported | `revision-tracker.md` | "Say we added it although we did not." |
| Invented line numbers | Final-looking line numbers before build | Use placeholders and line-number status | `response-letter.md` | "Invent line numbers for now." |
| Defensive tone | Argues reviewer is wrong without manuscript change | Check whether manuscript caused misunderstanding | `tone-and-risk.md` | "Write a firm response; no edits." |
| Over-editing | Small comment causes broad rewrite | Track prohibited over-edit | `comment-resolution-worksheet.md` | "Rewrite the whole section for this wording issue." |
| Conflicting reviewers | Separate replies create contradiction | Group by manuscript function | `revision-tracker.md` | "One asks longer, one asks shorter." |
| Impossible experiment | Time-pressure refusal only | Scientific/scope reason plus limitation if truthful | `tone-and-risk.md` | "Reject this requested experiment." |

## False Completed Change

Risk: the user asks to say a change was made when it was not made.

Response:

- Refuse to write a false response.
- Mark the item as `Planned`, `Needs author input`, or `Not supported`.

## Invented Line Numbers

Risk: the response letter cites line numbers before final build or diff.

Response:

- Use section or figure/table names until final line numbers are available.
- Ask for the compiled final manuscript or diff if exact line numbers are
  required.

## Defensive Tone

Risk: the reply argues with the reviewer without improving the manuscript.

Response:

- Check whether the manuscript caused the misunderstanding.
- Prefer clarification and evidence over defensive language.

## Over-Editing

Risk: a small wording comment triggers broad unrelated rewrites.

Response:

- Define the minimum change that resolves the comment.
- Track prohibited over-edit in the revision plan.

## Conflicting Reviewers

Risk: one reviewer asks for more detail while another asks for compression.

Response:

- Group comments by manuscript function.
- Preserve the evidence-bearing detail.
- Move secondary details to a table, appendix, or concise clarification when
  allowed.
- Do not write final replies before the merged revision plan is clear.

## Impossible Central Experiment

Risk: a reviewer asks for a new experiment that cannot be run in the revision.

Response:

- Do not cite time pressure as the main reason.
- Give a scientific or scope reason.
- Add a limitation or clarify the evaluation boundary when truthful.
