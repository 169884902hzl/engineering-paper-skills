# Revision Tracker

Use this to turn comments into concrete tasks.

## Tracker Fields

| Field | Required content |
|---|---|
| ID | `E.1`, `R1.1`, `A.1`, etc. |
| Original comment | exact short quote |
| Type | Logic, Structure, Expression, Data, Citation, or Format |
| Real complaint | one sentence |
| First target section | one section only |
| Second target section | optional, one section only |
| Target | one to three file/section locations |
| Decision | revise, defer with reason, or no change with reason |
| Prohibited over-edit | what must not be changed |
| Acceptance evidence | what proves the comment is handled |
| Verification | read lines, compile, inspect PDF, or check diff |
| Line-number status | provided, pending final build, or not applicable |
| Status | Done with evidence, Planned, Needs author input, Defer with reason, or No change with reason |

## Ten-Minute SOP

1. Copy the comment exactly.
2. Classify it.
3. Write the real complaint:
   `The issue is not [surface issue]; it is that [paper function] is not established.`
4. Choose one to three targets.
5. Choose decision.
6. Add prohibited over-edit.
7. Add acceptance evidence and verification.

If acceptance evidence cannot be written, do not edit yet.

## Decisions

- `revise`: the comment identifies a real issue or a needed clarification.
- `defer with reason`: the comment is valid but cannot be handled in this
  revision without unacceptable risk or missing evidence.
- `no change with reason`: the comment is based on a misunderstanding or outside
  scope, and the manuscript already makes the boundary clear.

Every `defer` or `no change` needs a scientific or scope reason, not a deadline
excuse.

## Filled Example

| ID | Original comment | Type | Real complaint | First target section | Decision | Acceptance evidence | Verification | Line-number status | Status |
|---|---|---|---|---|---|---|---|---|---|
| R1.1 | "Add ablation." | Data | Component support is not isolated. | Experiments | revise if data exists; otherwise planned | ablation table or limitation note | inspect Results and table | pending final build | Needs author input |
| R1.2 | "Method unclear." | Structure | Execution role is underspecified. | Methods | revise | paragraph names inputs, outputs, and execution gate | read Methods | pending final build | Planned |
