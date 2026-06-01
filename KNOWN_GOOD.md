# Known-Good Commit Matrix

This repository uses a no-release beta process. External reviews should cite the
exact commit hash and the evidence artifacts below instead of assuming a release
tag implies readiness.

## Current public audit commit

| Field | Value |
|---|---|
| Commit | `d03d683ef473b48b6e47f2abb6532ca0dfe1ccf3` |
| Commit message | `Add structured audit contracts` |
| Status | top-tier candidate, not top-tier ready |
| Release state | no GitHub release; commit-based beta |

## Behavior evidence

| Artifact | Status | Evidence level |
|---|---|---|
| `tests/outputs/model_runs/full_paper_realistic_audit_8da3ceb.md` | recorded local model run | `local_single_run` |
| `evals/results/8da3ceb_full_paper_model_eval.jsonl` | human-readable eval record for the local run | `local_single_run` |
| `.github/workflows/behavior-regression.yml` | manual behavior-regression workflow | requires configured model command |
| `.github/workflows/qa.yml` | static QA plus optional behavior regression | behavior regression is `NOT_RUN` without secret |

## Known limitations

- No public CI-controlled model-run artifact is available for `d03d683`.
- Structured JSON expectations check required fields, rows, and grounded spans;
  they are not full semantic entailment.
- Full-paper fixtures include synthetic robotics, ML, and systems cases; they do
  not replace de-identified real manuscript benchmarks.
- Venue profiles contain static policy summaries and reachable official URLs;
  they do not replace live official policy extraction.
- Sentence-level audits remain sampled rather than exhaustive across a complete
  8-12 page manuscript.

## Review instruction

When requesting an external review, ask the reviewer to inspect this file, the
current commit hash, the model-run artifact, the eval JSONL, the structured JSON
golden output, and `docs/quality-gates.md`.
