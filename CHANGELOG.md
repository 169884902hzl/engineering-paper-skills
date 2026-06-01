# No-release beta changelog

This project currently uses commit-based beta tracking instead of GitHub
releases. Entries below document quality-gate changes that matter for external
review and reuse.

## Replace first-screen safety examples with writing demo

- Removed the README first-screen `Quick Illustrative Examples` block because it
  emphasized claim rejection and response safety before showing manuscript
  writing value.
- Added `tests/prompts/demo_notes_to_manuscript_paragraph.md` as a hero writing
  prompt for rough notes to bounded manuscript prose.
- Ran local Codex in read-only mode to generate
  `tests/outputs/model_runs/demo/demo_notes_to_manuscript_paragraph_2dc9571.md`.
- Added `evals/results/2dc9571_hero_demo_model_eval.jsonl` to record the local
  single-run evidence level, command, output hash, and limitations.
- Updated README and Pages so the first screen shows a recorded notes-to-prose
  output excerpt; claim audit, response truthfulness, and validation examples
  remain available later as safety and audit examples.

## Rework user examples and demo-first documentation

- Moved quality evidence links out of the README's first usage path and into a
  maintainer/reviewer section.
- Rewrote the README opening around `$engineering-paper-coach`, quick examples,
  Quick Start, and a skill chooser.
- Added practical README examples for research-note skeletons, bounded Results
  prose, conservative polishing, figure/table caption checks, and readiness
  triage.
- Reordered the Pages demo so practical Markdown examples appear before
  structured JSON artifacts and model-run evidence.
- GPTPro later flagged these examples as ambiguous because they looked like
  unlabelled model outputs. The follow-up fix labels hand-written examples as
  illustrative and adds recorded local demo outputs with prompt fixtures,
  artifact paths, and hashes.

## Record user-facing local demo outputs

- Added demo prompt fixtures for claim audit, Results writing, conservative
  polishing, figure/table source-data consistency, response truthfulness,
  validation readiness, Related Work nearest-neighbor distinction, and Methods
  execution path.
- Ran local Codex in read-only mode to generate raw demo final-message outputs
  under `tests/outputs/model_runs/demo/`.
- Added `tests/outputs/model_runs/demo/manifest.json` with prompt paths, output
  paths, command strings, SHA-256 hashes, evidence level, and CI-control status.
- Added `evals/results/681d305_demo_outputs_model_eval.jsonl` to record that these are
  local single-run demo outputs, not CI-controlled behavior proof.
- Updated README and Pages so hand-written examples are explicitly labeled as
  illustrative and recorded outputs are linked separately.

## Add README and Pages use-case examples

- Added README input/output examples that show conservative claim audit and
  figure/table claim checking without requiring readers to inspect quality-gate
  artifacts first.
- Added Pages demo input/output cards for coach auditing, figure/table
  caption checks, and reviewer response truthfulness.
- Kept examples evidence-bound: they show `NOT_READY`, unsupported response
  claims, and safe rewrites rather than top-tier-readiness claims.

## 38b3d4d - Split behavior contract and add coach skill

- Added `engineering-paper-coach` as a lightweight Markdown-first user entry
  skill inspired by the simple skill shape of `phd-writing`.
- Added a minimal coach prompt, expected spec, and golden output.
- Added a schema-only full-paper structured contract beside the flexible
  behavior contract.
- Changed structured behavior checks from exact hidden-gold row matching to
  issue-class and status-class matching.
- Changed span checks to allow fixture-grounded token coverage when a model
  combines two valid source snippets.
- Added `docs/contract-failure-analysis.md` to explain why the old local run
  failed exact matching while still catching substantive blockers.
- Recorded a local Codex structured-audit run at `38b3d4d` as
  `local_single_run`; it passes the flexible issue-class behavior contract but
  remains non-CI evidence and not top-tier-ready proof.

## 80d9c23 - Add span-grounded audit evidence checks

- Added source/evidence span-origin checks and hidden-gold row checks for the
  structured full-paper audit contract.
- Added behavior-regression eval stub generation for manual CI runs.
- Recorded a real local Codex structured-contract attempt against this commit
  as `local_single_run_failed`; the output missed required readiness labels,
  hidden-gold row matches, paragraph-transition rows, and response-truthfulness
  rows.
- This entry is failure evidence, not a passing behavior proof.

## 6bec865 - Strengthen metadata and audit evidence gates

- Added `KNOWN_GOOD.md` and `CHANGELOG.md` as no-release version anchors.
- Added `scripts/check_metadata_files.py` and wired it into QA.
- Changed `CITATION.cff` to `commit-based-beta` to avoid implying a release.
- Added source/evidence span fields, response semantic fields, and evidence
  level fields to structured artifacts and eval JSONL.
- Added `policy_snapshot` metadata to static venue profiles.
- Added inline demo snippets to the Pages demo gallery.
- A later strict local structured-contract run against this commit was recorded
  as failure evidence because the model output did not satisfy span-origin,
  status, and hidden-gold row checks.

## d03d683 - Add structured audit contracts

- Added structured JSON audit prompt, expected spec, and golden output for
  full-paper audit behavior.
- Added ML benchmark and systems artifact fixtures to reduce single-domain
  coverage.
- Added no-release quality documentation, Pages demo pages, discovery docs, and
  standard sitemap/robots files.
- Removed release-gate workflow and release-note artifact to avoid implying a
  stable release process.
- Recorded `8da3ceb` local model-run evidence and eval JSONL as candidate-level
  behavior evidence, not top-tier-ready proof.

## 8da3ceb - Add public beta discovery and model-run evidence

- Added GitHub Pages homepage and demo links.
- Added local model-run artifact for the realistic full-paper audit case.
- Added eval record for the local model-run output.
- Strengthened README evidence-boundary language and repository metadata.

## f383bb9 - Add semantic behavior regression checks

- Added behavior-regression workflow entry point with required command mode.
- Added semantic expected-behavior groups for full-paper audit, polishing, and
  figure/table checks.
- Added response diff fixture checks and venue-profile URL refresh checks.

## f1625f3 and earlier

- Built the initial full-paper realistic fixture, story-spine references,
  response diff guidance, venue profiles, and static quality checks.
