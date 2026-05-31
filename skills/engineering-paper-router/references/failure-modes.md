# Engineering Paper Router Failure Modes

| Symptom | Bad route | Correct behavior | Stop condition |
|---|---|---|---|
| Writing instead of routing | Starts drafting final prose | Output route, missing inputs, and next prompt only | User explicitly asks to continue after route |
| Single-skill bias | Forces mixed task into writing only | Name primary and secondary skills with order | Any visual, response, or validation subtask exists |
| Validation omitted | Treats "ready" as polish request | Include `engineering-validation` | User asks complete, fixed, ready, submittable, final |
| Polishing before structure | Sends broken Results paragraph to polishing | Route to writing/experiments first | Claim/evidence/boundary unclear |
| Caption task swallowed by writing | Handles caption overclaim as sentence polish | Route to figure-table | Claim depends on visual/table support |
| Writing before evidence | Routes thin evidence to final drafting | Route to scaffold and missing inputs | Method, evidence, or boundary absent |
| False response path | Routes reviewer comment directly to response text | Route to response tracker and validation dependency | Change not done or line numbers unknown |

## Router Self-Check

Before returning, ask:

1. Does the user request contain more than one operation?
2. Is any operation about readiness or final status?
3. Is any requested claim unsupported by provided evidence?
4. Could a different skill prevent a stronger failure than the primary skill?

If the answer to 2 or 3 is yes, include the stop condition in the next prompt.
