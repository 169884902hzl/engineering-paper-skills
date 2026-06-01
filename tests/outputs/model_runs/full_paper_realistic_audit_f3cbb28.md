# Model Run: Full-Paper Realistic Audit

Source: local `codex exec` run on `tests/fixtures/full_paper/robot_active_observation_realistic_8page.md`.

Note: the command used `--output-last-message`, but the target directory did not exist at run time, so Codex reported a write failure after producing the final message. This file records the final message captured from the terminal output. It is a local model-run artifact, not a CI regression result.

## Full-paper audit verdict

Overall: **NOT_READY / PASS_WITH_BLOCKERS as a draft audit target**.

Highest-risk issue: the title, abstract, and response letter revive unsupported claims: `general`, `industrial`, `reliable`, `causal`, `robustness`, stress tests, Table 3, citations, and final line numbers. The evidence packet explicitly limits results to one robot, one fixture, one object family, no statistics, no verified citations, no final line numbers, and an empty Table 3.

Checks actually performed: local skill and rubric read, current Markdown read with line numbers, and targeted searches for claim/evidence terms.

Not run: build, citation verification, official venue check, stress-test artifact check, source-data check, figure-file check, or response-diff check.

## Story spine

| Node | Status | Audit |
|---|---:|---|
| Problem | Strong | Visibility loss during insertion is concrete. |
| Gap | Partial | Technical gap is plausible, but nearest prior work is unverified. |
| Insight | Stronger | Visibility-confidence loop is the real contribution. |
| Method | Partial | State machine is clearer than a module list, but detector, threshold, and calibration details are missing. |
| Evidence | Bounded | Supports only evaluated tabletop insertion: 84% versus 69/72/76/77/61. |
| Boundary | Strong in later text | Boundaries are present but not enforced in title, abstract, or response. |
| Implication | Overstated | Safe implication: controlled real-robot evidence for visibility-aware insertion, not general manufacturing readiness. |

## Claim-evidence audit

| Claim | Verdict | Repair |
|---|---:|---|
| General active observation for industrial workcells | Critical overclaim | Narrow title/abstract to tabletop visibility-loss insertion. |
| Full system improves success | Supported, bounded | Keep with protocol and counts. |
| Ablations prove causality | High overclaim | Use `suggest` or component-support wording. |
| Reflective trials demonstrate robustness | High overclaim | Present as stress observation, not validation. |
| Real-time system | Medium overclaim | Define timing budget or call Table 2 implementation context. |
| Calibration/frame alignment is reliable | Medium overclaim | Add residuals/drift or keep descriptive. |
| Prior work does not solve robust general insertion | Critical citation risk | Replace with taxonomy scaffold until citations are verified. |
| Industrial deployment readiness | Critical false response claim | Delete from manuscript and response. |

## Section claim inventory

| Section | Main claim | Status |
|---|---|---:|
| Title | General, robust, industrial | Fails evidence boundary. |
| Abstract | Reliable, causal, robust, scalable | Main overclaim cluster. |
| Introduction | Problem and contribution | Mostly good; self-audit prose should not remain final paper prose. |
| Related Work | Prior work gap | Not submission-ready; placeholders remain. |
| Methods | Visibility-confidence loop | Good core, but written partly as meta-instructions. |
| Experiments | Bounded real-robot comparison | Strongest section; needs protocol details and failure taxonomy. |
| Figures/Tables | Visual responsibility | Good audit notes, but final captions and data are not supplied. |
| Discussion | Honest limitations | Strong; should constrain abstract and title. |
| Conclusion | Bounded | Much safer than abstract. |
| Supplementary Notes | Source constraints | Useful evidence boundary, not final manuscript prose. |
| Response Letter | Claims all issues fixed | False against supplied materials. |

## Paragraph transition matrix

| From -> To | Verdict | Repair |
|---|---:|---|
| Intro problem -> prior routes -> active perception -> confidence loop | Good | Keep this order; it builds the mechanism. |
| Intro contributions -> unsupported broad-claim paragraph | Mixed | Move self-audit content to limitations or notes; final introduction should not self-audit. |
| Related Work visual/force/active/guarded lists -> gap | Weak | Rebuild around axes and nearest-neighbor distinction. |
| Methods module list -> state machine | Good | Define state machine first, then modules as implementation. |
| Experiments protocol -> variants -> results -> interpretation | Good | Add randomization, balancing, and failure coding. |
| Figures/Tables section | Audit prose, not paper prose | Convert to actual captions/table responsibilities. |
| Discussion evidence -> limitations -> future work | Good | Use it to rewrite title and abstract. |
| Response letter paragraph 1 -> paragraph 2 | Fails | Both repeat unsupported `we added/proved/validated` claims. |

## Paragraph job and deletion-damage table

| Span | Job | Delete damage | Action |
|---|---|---|---|
| Intro failure mode | Define failure mode | High | Keep. |
| Prior-route overview | Place prior routes | Medium | Keep after citation verification. |
| Active-perception bridge | Connect active perception to execution | High | Keep. |
| Confidence-loop paragraph | State mechanism | High | Promote to method spine. |
| Contribution paragraph | State contribution and boundary | High | Keep, make final prose. |
| Draft self-audit | Expose unsupported broad claims | Low as manuscript prose | Move to notes; use content to constrain claims. |
| Related-work topic list | Organize prior work | Medium | Restructure and verify citations. |
| Method critique/meta text | Design note | High as design note, low as final prose | Convert to authorial methods. |
| Result interpretation | Bounded evidence interpretation | High | Keep; this is the safest evidence paragraph. |
| Figure/table instructions | Visual responsibility plan | Medium | Convert to captions/tables; remove meta wording. |
| Discussion boundaries | Limit claims | High | Keep and use to repair abstract. |
| Response claims | Assert completed revisions | Negative damage if deleted | Replace entirely after real revisions exist. |

## Sentence role samples

| Sentence/span | Role | Issue | Action |
|---|---|---|---|
| `general active observation framework` | Claim | Generality unsupported | Downgrade. |
| `ablations prove` | Interpretation | Causal strength too high | Use bounded component-support language. |
| `demonstrate robustness` / `scalable route` | Implication | Unsupported robustness/deployment | Delete or move to future work. |
| `draft should define` | Editorial note | Not manuscript prose | Rewrite as method definition. |
| Bounded result interpretation | Evidence boundary | Correctly bounded | Keep as model sentence. |
| Boundary sentence | Boundary | Correctly blocks overclaim | Keep. |
| Response completion claim | Response claim | Contradicts supplied evidence | Replace, not polish. |

## Figure/table audit

| Item | Can support | Must not claim |
|---|---|---|
| Figure 1 | System components and information flow | Robustness or reasoning proof. |
| Figure 2 | Execution sequence and state transitions | Robustness validation. |
| Figure 3 | Main success-rate comparison | Statistical significance without tests/uncertainty. |
| Figure 4 | Qualitative failure/success examples | General industrial performance. |
| Table 1 | Variants, counts, success rates | Sole causal proof. |
| Table 2 | Measured latency context | Real-time industrial readiness without timing budget. |
| Table 3 | Nothing yet | Any stress-test result; it has no data. |

## Source-note expansion audit

| Source note | Expanded claim | Verdict |
|---|---|---:|
| Observer camera seems to help | Reliable/general active observation | Over-expanded. |
| Gate probably prevents bad insertions | Causal proof | Over-expanded. |
| Could transfer if alignment updated | Generalizes to platforms/workcells | Over-expanded. |
| Reflective case only full system | Robustness to industrial conditions | Over-expanded. |
| Related Work not final | Citations added | False unless sources are supplied. |
| Do not claim stress robustness | New stress-test Table 3 | Direct contradiction. |
| Line numbers placeholders | Final line numbers included | Direct contradiction. |

## Response diff verification

**NOT_RUN as a response-diff check**: no revised manuscript diff was supplied.

Internal consistency read only:

| Response claim | Conflict |
|---|---|
| Added stress-test section and Table 3 | Evidence says Table 3 is planned/empty. |
| Added citations | Bibliography is placeholder only. |
| Exact final line numbers | Evidence says no final line numbers and placeholders remain. |
| Figure 2 validates robustness | Manuscript says Figure 2 cannot validate robustness. |
| Ready for industrial deployment | Evidence excludes deployment, cross-robot, and cross-fixture tests. |

## Venue readiness

No official venue check was run. Venue is undecided and official instructions are not supplied.

Content-level readiness: not ready for CoRL/ICRA/RA-L submission as-is. The real-robot comparison is promising, but blockers remain: unsupported broad claims, placeholder citations, missing protocol details, no failure taxonomy, no validated figures/tables, false response claims, and no build/source artifacts.

## Validation result

**CANNOT_MARK_READY**.

Reason: supplied materials explicitly lack LaTeX project, PDF, bibliography, source data, figure files, official venue instructions, revised manuscript diff, and final response line numbers. The line references in the run came from reading the supplied Markdown only; they do not verify the response letter's claimed final line numbers.

## Prioritized repair plan

| Priority | Repair | Owner route |
|---|---|---|
| P0 | Rewrite response letter to remove false claims about stress tests, Table 3, citations, line numbers, robustness validation, and deployment readiness. | `engineering-response` |
| P0 | Narrow title and abstract to one-robot/tabletop/visibility-loss insertion evidence. | `engineering-writing` |
| P1 | Convert meta-audit prose in Methods, Results, Figures/Tables, and Supplementary Notes into final manuscript prose or remove it. | `engineering-writing` |
| P1 | Rebuild Related Work from verified nearest-neighbor citations; keep taxonomy placeholders until sources exist. | `citation-verification` + `engineering-writing` |
| P1 | Add missing experiment protocol details: randomization, balancing, failure coding, counts, uncertainty policy. | Author input + `engineering-writing` |
| P2 | Add failure taxonomy or downgrade mechanism-level interpretation. | Author input |
| P2 | Finalize Figure 3/Table 1 as evidence anchors; keep Table 3 out unless data exist. | `engineering-figure-table` |
| P3 | Run actual build, citation, venue, figure, source-data, and response-diff validation only after revised artifacts exist. | `engineering-validation` |
