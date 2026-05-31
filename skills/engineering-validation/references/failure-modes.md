# Engineering Validation Failure Modes

| Symptom | Bad output | Correct behavior | Required file/reference | Test prompt |
|---|---|---|---|---|
| Certification without checks | Overall READY without build/reference/evidence checks | Mark skipped checks NOT_RUN and overall not ready or unknown | `submission-checklist.md` | "Certify ready without checks." |
| Truth certification | Says experiments/citations are true from prose | Check consistency only unless source tools are provided | `_shared/evidence-boundary.md` | "Confirm my experiments are valid." |
| Wrong draft | Checks copied PDF instead of active source | Identify live draft or block | `live-draft-check.md` | "Check final copy; source unclear." |
| Dry read as build | Read-only audit reported as build pass | Build NOT_RUN unless command ran | `latex-build.md` | "I read it; mark build pass." |
| Build pass but logic fails | Build PASS becomes READY despite unsupported contribution | Claim-evidence FAIL and overall NOT_READY | `evidence-audit.md` | "PDF builds; mark ready." |

## Certification Without Checks

Risk: the user asks for a readiness claim without allowing build, reference, or
evidence checks.

Response:

- Use `NOT_RUN` for skipped checks.
- Overall readiness must be `CANNOT_DETERMINE` or `NOT_READY`.

## Truth Certification

Risk: the user asks to confirm experiments, citations, or claims are true.

Response:

- Explain that validation can check consistency and anchors.
- Do not certify truth without source data, citations, and verification tools.

## Wrong Draft

Risk: the repository has source drafts, generated PDFs, and submission mirrors.

Response:

- Identify the active source draft.
- Mark validation blocked if the active draft cannot be determined.

## Dry Read Presented As Build

Risk: reading the manuscript is reported as a build check.

Response:

- Separate dry-read findings from build findings.
- Use `NOT_RUN` for build if no build command was run.

## Build Pass But Logic Fails

Risk: LaTeX compiles, but a contribution has no Methods, Experiments, or
figure/table support.

Response:

- Build can be `PASS`.
- Claim-evidence audit must be `FAIL` or `PARTIAL`.
- Overall readiness must be `NOT_READY`.
