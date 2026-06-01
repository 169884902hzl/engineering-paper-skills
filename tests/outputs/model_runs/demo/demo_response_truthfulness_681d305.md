## 1. Response strategy summary

- Package status: Revision plan only, not a final reviewer response.
- Main risk: The draft falsely claims added stress tests, Table 3, final line numbers, and broad generalization.
- Response mode: Truthful partial-compliance plan.
- Current evidence boundary: 84% success over 180 trials on one robot arm, one tabletop fixture, and one cylindrical peg family.
- Safe strategy: Narrow robustness/generalization claims, add an explicit limitation, and only mention stress tests or Table 3 after data and manuscript changes exist.

## 2. Comment-response tracker

| ID | Reviewer concern | Type | Severity | Real complaint | Action | Evidence/change needed | Prohibited overclaim | Status |
|---|---|---:|---:|---|---|---|---|---|
| R1 | Paper overclaims robustness | Claim strength | High | Robustness claim exceeds current evidence | Revise robustness language to tested-condition scope | Manuscript diff showing narrowed claims | “robust generalization across settings” | Planned |
| R1 | No evidence beyond tabletop setup | Evaluation scope | High | Generalization is unsupported | State evaluation boundary and limitation | Text naming one robot arm, one tabletop fixture, one cylindrical peg family | Cross-robot, industrial, or broad setting generalization | Planned |
| R1 | Add stress tests | Missing experiment | High | Reviewer wants additional evaluation | Mark as author-input needed unless data are supplied | Stress-test protocol, raw results, table/figure, analysis | “We added stress tests in Table 3” | Needs author input |
| R1 | Identify where revision makes this change | Response traceability | Medium | Reviewer needs revision location | Use section-level placeholder now; final line numbers only after build | Verified manuscript diff and final PDF/source line mapping | “Lines 210-225” | Needs author input |

## 3. Safe draft response plan

Thank the reviewer and acknowledge that the original wording may have overstated the evidence.

Planned response content:

> We thank the reviewer for pointing out that the robustness and generalization claims need clearer boundaries. Based on the current evidence, we will revise the manuscript to limit the claim to the tested setup: 84% success over 180 trials using one robot arm, one tabletop fixture, and one cylindrical peg family. We will also add an explicit limitation noting that the current evaluation does not include cross-robot, industrial, or broader object-family testing. If additional stress-test data are added during revision, we will report the protocol, results, and table location after the data and manuscript changes are verified. Final section and line references will be provided after the revised manuscript is built and checked.

Minimum manuscript edits to support this response:

- Replace broad robustness/generalization language with tested-condition language.
- Add a limitation stating no cross-robot evaluation, no industrial evaluation, and no evaluation beyond the current tabletop fixture and cylindrical peg family.
- Add stress tests only if real data are supplied.
- Add Table 3 only if the table and source data exist.
- Add final line numbers only after the revised manuscript is compiled and verified.

## 4. Prohibited final-response claims

- “We added new stress tests.”
- “We added Table 3.”
- “Lines 210-225 were revised.”
- “The method generalizes across settings.”
- “The method is robust beyond the tabletop setup.”
- “The method was evaluated across robots.”
- “The method was validated in industrial settings.”
- “The revision demonstrates generalization.”

## 5. Verification needed before final response

- Revised manuscript diff showing narrowed robustness/generalization claims.
- Verified limitation text in the manuscript.
- Stress-test data, protocol, and analysis if stress tests are to be claimed.
- Actual Table 3 and its source data if Table 3 is to be cited.
- Final compiled manuscript or source-to-PDF mapping before citing line numbers.
- Check that the response wording matches the manuscript changes exactly.