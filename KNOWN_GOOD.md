# Known-Good Commit Matrix

This repository uses a no-release beta process. External reviews should cite the
exact commit hash and the evidence artifacts below instead of assuming a release
tag implies readiness.

## Commit anchors

| Field | Value |
|---|---|
| Latest GPTPro-reviewed main commit | `6bec865f5c9c83a89a5b5448caff1f96a0c9c19a` |
| Latest GPTPro-reviewed commit message | `Strengthen metadata and audit evidence gates` |
| Current repository metadata/audit-gate baseline | current `main`; resolve with `git rev-parse HEAD` |
| Current behavior-audited model-output commit | `38b3d4d72660fbfe5705103e6bc27addac14668e` |
| Current structured-contract baseline | `38b3d4d72660fbfe5705103e6bc27addac14668e` |
| Latest local structured-contract attempt | `38b3d4d72660fbfe5705103e6bc27addac14668e` |
| Latest local structured-contract failure kept for diagnosis | `80d9c23b8b9e6fd42470df845547724d63a8cc48` |
| Current user-facing demo baseline | `e99ca8120a6174a9cdba7083bd71f739908c822c` rerun showcase evidence plus retained Results/Ablation from `ad6d5b4` |
| Current showcase v2 writing baseline | `e99ca8120a6174a9cdba7083bd71f739908c822c` rerun outputs, Methods v2, messy-note evidence, stability evidence, and benchmarks |
| Current rich writing model-output baseline | `078d53e7b5925cf7c56b3b4696c8a35b9ac8d475` |
| Current draft-first writing model-output baseline | `ce1478f66f50a27abe7dfe3d45ee31565ca6cb71` |
| Status | top-tier candidate, not top-tier ready |
| Release state | no GitHub release; commit-based beta |

The current `main` hash should always be resolved with `git rev-parse HEAD` or
the GitHub branch UI. This file records external-review and behavior-evidence
anchors; it does not try to embed the hash of its own future edits.

## Behavior evidence

| Artifact | Status | Evidence level |
|---|---|---|
| `tests/outputs/model_runs/full_paper_realistic_audit_8da3ceb.md` | recorded local model run | `local_single_run` |
| `evals/results/8da3ceb_full_paper_model_eval.jsonl` | human-readable eval record for the local run | `local_single_run` |
| `tests/outputs/model_runs/full_paper_realistic_structured_audit_6bec865_failed.json` | recorded local structured-contract attempt | `local_single_run_failed` |
| `evals/results/6bec865_full_paper_model_eval.jsonl` | failure eval record for the strict structured contract | `local_single_run_failed` |
| `tests/outputs/model_runs/full_paper_realistic_structured_audit_80d9c23_failed.json` | recorded local structured-contract attempt after span checks; exact hidden-gold row matching failed | `local_single_run_failed` |
| `evals/results/80d9c23_full_paper_model_eval.jsonl` | failure eval record for the exact hidden-gold contract | `local_single_run_failed` |
| `tests/outputs/model_runs/full_paper_realistic_structured_audit_38b3d4d_pass.json` | recorded local structured-contract attempt after splitting schema checks from flexible issue-class behavior checks | `local_single_run` |
| `evals/results/38b3d4d_full_paper_model_eval.jsonl` | eval record for the local flexible behavior-contract pass | `local_single_run` |
| `tests/outputs/model_runs/demo/manifest.json` | manifest for recorded local user-facing demo outputs | `local_single_run` |
| `evals/results/681d305_demo_outputs_model_eval.jsonl` | eval record for demo-output provenance | `local_single_run` |
| `tests/outputs/model_runs/demo/demo_notes_to_manuscript_paragraph_2dc9571.md` | recorded local hero notes-to-manuscript paragraph demo | `local_single_run` |
| `evals/results/2dc9571_hero_demo_model_eval.jsonl` | eval record for the hero writing demo output | `local_single_run` |
| `tests/outputs/model_runs/writing/manifest_rich.json` | manifest for recorded local rich writing outputs at `078d53e` | `local_single_run` |
| `evals/results/078d53e_rich_writing_model_eval.jsonl` | strict local eval record for rich writing model outputs | `local_single_run` |
| `tests/outputs/model_runs/writing/manifest_showcase_v2.json` | manifest for recorded local showcase v2 writing outputs at `ad6d5b4` | `local_single_run` |
| `evals/results/ad6d5b4_showcase_v2_writing_eval.jsonl` | strict local eval record for showcase v2 writing model outputs | `local_single_run` |
| `evals/results/ad6d5b4_showcase_v2_human_review.md` | human review table for showcase v2 writing outputs | `local_single_run_review` |
| `tests/outputs/model_runs/writing/manifest_showcase_v2_rerun.json` | manifest for Abstract, Related Work, Chinese-to-English, Conclusion reruns and Methods v2 at `e99ca81` | `local_single_run` |
| `evals/results/e99ca81_showcase_v2_rerun_eval.jsonl` | eval JSONL for showcase reruns and Methods v2 | `local_single_run` |
| `evals/results/e99ca81_showcase_v2_rerun_human_review.md` | human review for showcase reruns and Methods v2 | `local_single_run_review` |
| `tests/outputs/model_runs/writing/manifest_messy_notes.json` | manifest for rough, incomplete, mixed, and contradictory notes prompts | `local_single_run` |
| `evals/results/e99ca81_messy_notes_eval.jsonl` | eval JSONL for messy-note robustness | `local_single_run` |
| `evals/results/e99ca81_messy_notes_human_review.md` | human review for messy-note robustness | `local_single_run_review` |
| `tests/outputs/model_runs/writing/manifest_stability.json` | three-run local stability sample for Results, Ablation, and Chinese-to-English prompts | `local_multi_run_sample` |
| `evals/results/e99ca81_stability_eval.jsonl` | eval JSONL for local stability samples | `local_multi_run_sample` |
| `evals/results/e99ca81_stability_human_review.md` | human review for local stability samples | `local_multi_run_review` |
| `tests/outputs/model_runs/writing/manifest_benchmark.json` | de-identified benchmark and full-section Results demo manifest | `local_single_run` |
| `evals/results/e99ca81_benchmark_human_review.md` | human review for de-identified benchmark prompts | `local_single_run_review` |
| `evals/results/e99ca81_full_section_human_review.md` | human review for full-section Results demo | `local_single_run_review` |
| `tests/outputs/model_runs/writing/manifest.json` | manifest for recorded local draft-first writing outputs at `ce1478f` | `local_single_run` |
| `evals/results/ce1478f_writing_model_eval.jsonl` | eval record for draft-first writing model outputs | `local_single_run` |
| `.github/workflows/behavior-regression.yml` | manual behavior-regression workflow | requires configured model command |
| `.github/workflows/qa.yml` | static QA plus optional behavior regression | behavior regression is `NOT_RUN` without secret |
| behavior-regression eval stub | generated by the manual workflow when a command template runs | `ci_single_run` pending human review |

## Demo output provenance

The README and Pages use two distinct example classes:

- Illustrative examples are hand-written and must be labeled as not recorded
  model-run outputs.
- Recorded demo outputs are raw local Codex final messages generated from prompt
  fixtures. The general demo set was generated at base commit `681d305`; the
  hero notes-to-manuscript paragraph demo was generated at base commit
  `2dc9571`. The full output paths and hashes are in
  `tests/outputs/model_runs/demo/manifest.json`.

Recorded demo outputs remain `local_single_run` evidence. They are useful for
showing real skill behavior, but they are not CI-controlled proof and do not
upgrade the project to top-tier ready.

Recorded demo command strings use `<repo-root>` placeholders in public
JSON/JSONL provenance files. Local absolute workspace paths are not part of the
published evidence contract.

## Showcase v2 and rerun writing output provenance

The showcase v2 writing outputs under `tests/outputs/model_runs/writing/` are
raw local Codex final answers generated from seven stricter showcase v2 prompt
fixtures at base commit `ad6d5b448be9c76b9c034d4fc599fe4d33296270`. They were
generated after installing this repository's edited `skills/_shared` and
`skills/engineering-*` directories into Codex home.

GPTPro review kept Results with diagnostic axes and Ablation rows as strong
hero candidates, but required reruns for Abstract, Related Work,
Chinese-to-English, and Conclusion. The rerun pass at
`e99ca8120a6174a9cdba7083bd71f739908c822c` adds those reruns, a Methods v2
showcase, messy-note prompts, a local three-run stability sample, de-identified
benchmark prompts, and a full-section Results demo.

The current first-screen showcase uses four outputs: Results, Ablation,
Chinese-to-English rerun, and Methods v2. Abstract, Related Work, Conclusion,
and the full-section Results demo are gallery items when their human review
allows it. The old Abstract, Related Work, Chinese-to-English, and Conclusion
showcase v2 outputs are evidence-only or rejected artifacts.

These artifacts remain candidate-level local evidence. The stability sample
improves confidence over one-off demos, but it is still not CI-controlled proof
and does not upgrade the project to top-tier ready. Full output paths and
SHA-256 hashes are recorded in
`tests/outputs/model_runs/writing/manifest_showcase_v2.json`,
`tests/outputs/model_runs/writing/manifest_showcase_v2_rerun.json`,
`tests/outputs/model_runs/writing/manifest_messy_notes.json`,
`tests/outputs/model_runs/writing/manifest_stability.json`, and
`tests/outputs/model_runs/writing/manifest_benchmark.json`.

## Rich writing output provenance

The rich writing outputs under `tests/outputs/model_runs/writing/` are raw local
Codex final answers generated from eight rich writing prompt fixtures at base
commit `078d53e7b5925cf7c56b3b4696c8a35b9ac8d475`. They were generated after
installing this repository's current `engineering-writing` and
`engineering-paper-coach` skill files into Codex home.

The current user-facing showcase uses three of those outputs: Ablation rows to
contribution-level ablation prose, Results with diagnostic axes, and Methods
overview reader path. The Introduction, Related Work, Chinese notes, Abstract,
and Conclusion outputs are kept in the demo gallery. These artifacts remain
`local_single_run` evidence; they are not CI-controlled proof, not multi-run
stability proof, and not top-tier-ready proof. Their full output paths and
SHA-256 hashes are recorded in
`tests/outputs/model_runs/writing/manifest_rich.json`.

## Draft-first writing output provenance

The draft-first writing outputs under `tests/outputs/model_runs/writing/` are
raw local Codex final answers generated from the writing prompt fixtures at base
commit `ce1478f66f50a27abe7dfe3d45ee31565ca6cb71`. They were generated after
installing this repository's current `skills/_shared` and `skills/engineering-*`
directories into Codex home.

These outputs are useful evidence for WRITE-mode and coach draft-first behavior,
but they remain `local_single_run` artifacts. They are not CI-controlled proof,
not multi-run stability proof, and not top-tier-ready proof. Their full output
paths, command strings, and SHA-256 hashes are recorded in
`tests/outputs/model_runs/writing/manifest.json`.

## Normal user boundary

Normal skill users only need `skills/_shared` and `skills/engineering-*`.
The `scripts/`, `tests/`, and `evals/` directories are maintainer/reviewer
evidence assets for repository QA, provenance checks, and behavior review.

## Known limitations

- Showcase v2 prompts are richer than many messy user notes, so the outputs may
  still be stronger than default behavior on thin source material.
- The messy-note prompts and de-identified benchmarks improve coverage, but
  they remain local artifacts and do not replace broad user-study evidence.
- The stability evidence is a local three-run sample for three prompt families,
  not a public CI-controlled stability benchmark.
- Human reviews are local reviewer records, not an external panel score.
- No public CI-controlled model-run artifact is available for `6bec865`,
  `80d9c23`, or `38b3d4d`.
- Structured JSON expectations check required fields, rows, and grounded spans;
  they now separate strict schema checks from flexible issue-class behavior
  checks, but are still not full semantic entailment.
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
