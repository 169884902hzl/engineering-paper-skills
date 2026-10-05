# No-release beta changelog

This project currently uses commit-based beta tracking instead of GitHub
releases. Entries below document quality-gate changes that matter for external
review and reuse.

## Beginner guide, experiment pre-mortem, and LaTeX checker

- `engineering-paper-coach`: new guide mode for beginners. It reads the
  project folder or notes before asking, detects the paper stage (idea,
  experiments, results, draft, reviews), produces one deliverable per stage,
  asks at most three questions, and ends each reply with what was produced,
  what comes next, and what to bring. Direct mode keeps the one-answer
  behavior for specific tasks. Stage detail is in
  `references/stage-playbook.md`; a Chinese beginner guide is in
  `docs/quickstart-zh.md`.
- Added `skills/_shared/experiment-premortem.md`: the reviewer patterns applied
  to an experiment plan (matched controls, assumption logging, independent
  measurement of internal components, time and cost logging, decision rules,
  trial counts with 95% Wilson intervals, held-out conditions, what to log).
  `engineering-paper-auditor` gains an experiment plan pre-mortem section; the
  router sends plan reviews there and beginners to the coach.
- Added `skills/engineering-validation/scripts/paper_check.py` (standard
  library): duplicate labels, undefined references, missing citations,
  unreferenced floats, float first-reference order, percentages impossible for
  a stated trial count, uncited entries, and prose percentages absent from
  tables. Synthetic fixtures under `tests/fixtures/paper_check*` and
  `scripts/check_paper_check.py` run in CI.
- On two real submissions, the checker found the duplicate table label behind
  a wrong table reference that a reviewer flagged, a duplicate figure label,
  seven percentages impossible for the stated ten trials per condition, and
  three never-referenced figures. It reads source order, not compiled layout,
  so it cannot see float placement in the PDF, and it does not expand macros.

## Shift from writing rules to author experience

- Added `skills/_shared/reviewer-attack-patterns.md`: nine objection patterns
  drawn from two real review sets and a senior co-author's comments, written
  generically so that neither source paper is identifiable. Each pattern gives
  the trigger, how reviewers raise it, why authors miss it, and the cheapest
  pre-submission fix.
- Added `skills/_shared/writing-process.md` (writing order, writing while
  results are incomplete, where published advice disagrees) and
  `skills/_shared/revision-moves.md` (global-to-local revision order and
  section moves observed in a senior author's revisions).
- `engineering-paper-auditor`: reviewer simulation is now the default for
  pre-submission review, ranked by what real reviewers lead with; the
  claim-by-claim audit tables are available on request.
- `engineering-writing` and `engineering-paper-coach`: removed rules that
  fought the model instead of informing it: the triple-repeated
  "write first, do not audit" override, fixed 120-220 word quotas, mandatory
  output templates, and the public-demo blocker list (still enforced for
  recorded demos by `scripts/check_public_writing_demos.py`). The same
  constraints were removed from `engineering-writing/manifest.yaml`, which now
  only routes to references. Kept the hard floor against invented results,
  citations, mechanisms, and completed work.
- `tests/expected`: dropped the output-heading requirements of the removed
  templates from seven behavior specs (coach and writing draft-first specs,
  `auditor_realistic`); numeric and content requirements are unchanged. The
  recorded golden outputs still pass. The optional real-model prompt
  regression was not rerun for this change.
- `engineering-figure-table`, `engineering-validation`, `engineering-response`,
  `engineering-polishing`, `engineering-paper-router`: short additions linking
  the new experience files (float numbering order, one job per float,
  misreading versus real-gap responses, revision order).
- Evidence: leave-one-paper-out reviewer-prediction test of an earlier
  version of the patterns (for each paper, a pattern file built only from the
  other paper's reviews) on two robotics papers with real reviews, Claude and
  Codex, one run per condition, blind scoring. Recall changed by at most one point (paper A: 8 to 9 and 6 to 7 of
  16; paper B: 9 to 9 of 10 for both models). The reviewers' top
  objection (the first objection of the first reviewer) moved to rank 1 in
  three of four runs; in one run another major objection dropped from rank 4
  to 8. Test materials contain
  unpublished manuscripts and confidential reviews and are not in this
  repository.
- Not done in this round: the roughly 80 existing reference files were left in
  place. Whether they still help current models needs a skill-off writing
  baseline, which has not been run; pruning waits for that result.

## Add citation gate, pattern library, scored audit mode, and Claude Code path

- Added `skills/_shared/citation-verification-workflow.md`: literature
  discovery stays external by design (deep-research tools, scholarly APIs);
  the suite now defines the verification ladder, intake table, and gate rules
  that let verified citations unlock Related Work positioning. Linked from
  the writing, validation, and response skills.
- Added `skills/engineering-writing/references/positive-patterns.md`:
  original pattern skeletons for pipeline systems, ablation-led component,
  rethinking, benchmark, and results-ladder writing.
- Added an opt-in scored audit mode to `engineering-paper-auditor` with three
  reviewer lenses and finding-anchored bands; default output remains
  unscored, and no weighted total is produced.
- README: added a Claude Code install path next to the Codex path, and a
  scope section that names literature discovery, paper reading, and slide
  building as out of scope with recommended external pairings.
- Made `scripts/check_public_writing_demos.py` parse on Python 3.8-3.11 by
  moving backslash expressions out of f-strings; CI already ran 3.12 and is
  unchanged.

## Strengthen public writing checks and rough-note evidence

- Upgraded `scripts/check_public_writing_demos.py` from fixed blocker strings
  to prompt-output comparison for physical mechanism terms in public writing
  artifacts.
- Synchronized public-demo reject patterns across `engineering-writing`
  manifest, skill instructions, and the RAL-style writing guide.
- Added real Codex CLI outputs for Conclusion rerun2, full-section Results v2,
  rough-user minimal prompts, rough/benchmark stability, verified-citation
  Related Work mode, realistic manuscript-note prompts, full-section Methods,
  and Chinese notes to Methods/Discussion.
- Added manifests, eval JSONL, and human reviews for the new evidence sets.
- Reworked README and Pages so shortened snippets are labeled as shortened
  excerpts, old rejected or superseded outputs stay in Evidence Archive, and
  per-card provenance is replaced by one compact evidence note.
- Evidence boundary: this remains a strong public beta and top-tier candidate,
  not top-tier-ready.

## Fix writing showcase blockers and add robustness evidence

- Added public recorded-demo reject rules to `engineering-writing` and the
  RAL-style writing guide for unsupported physical mechanisms, process-meta
  wording in manuscript prose, audit-disclaimer endings, Related Work
  verification prose inside the paragraph, and Conclusion limitation-inventory
  starts.
- Strengthened `engineering-paper-coach` so thin but sufficient evidence still
  produces a modest manuscript paragraph first, with strengthening notes after
  the draft.
- Added hard public-demo reject patterns and new writing flows to the
  `engineering-writing` manifest and expanded the writing rubric with blocker,
  manuscript-register, rough-note, and stability criteria.
- Added rerun prompts and real local Codex CLI outputs for Abstract, Related
  Work, Chinese-to-English, and Conclusion showcase v2 cases.
- Added Methods showcase v2, messy-note prompt fixtures, de-identified
  benchmark prompts, a full-section Results demo, and a local three-run
  stability sample for Results, Ablation, and Chinese-to-English prompts.
- Added `scripts/check_public_writing_demos.py` and wired it into
  `scripts/check_quality_assets.py` so public README and Pages surfaces cannot
  promote rejected or blocker-containing writing outputs.
- Reworked README and Pages into a value-first writing gallery, safety/audit
  examples, and an evidence archive with manifests, eval JSONL, human reviews,
  rejected outputs, and previous behavior evidence.
- Evidence boundary: this is still a top-tier candidate, not top-tier-ready.

## Improve showcase writing prompts and outputs

- Upgraded the `engineering-writing` WRITE contract from safe bounded drafting
  to showcase-grade manuscript generation with one internal self-revision pass.
- Added the `Showcase-Grade Writing Procedure` to require argument extraction,
  section-specific drafting, generic-frame removal, mechanism interpretation,
  and natural scientific-scope boundaries.
- Updated `engineering-paper-coach` so clear section-writing requests route to
  or inherit the stronger `engineering-writing` contract instead of shrinking
  into a safety rewrite.
- Strengthened `ral-style-writing-guide.md` with excellent-prose standards,
  section-specific sentence patterns, native-English reconstruction for Chinese
  notes, and an internal self-edit checklist.
- Added seven showcase v2 prompt fixtures and seven real local Codex CLI
  outputs under `tests/outputs/model_runs/writing/`.
- Added `tests/outputs/model_runs/writing/manifest_showcase_v2.json`,
  `evals/results/ad6d5b4_showcase_v2_writing_eval.jsonl`, and
  `evals/results/ad6d5b4_showcase_v2_human_review.md`.
- Updated README and Pages display so the first writing examples show input
  skeletons paired with recorded output excerpts. Older `ce1478f` outputs are
  retained as previous behavior links rather than main showcase excerpts.
- Evidence boundary: this is local single-run writing evidence only. It is not
  CI proof, multi-run stability proof, or top-tier-ready proof.

## Record rich writing model runs

- Generated eight fresh rich writing outputs in an interactive Codex CLI
  session from rich writing prompt fixtures at base commit `078d53e`.
- Added raw final-answer artifacts under `tests/outputs/model_runs/writing/`
  for Introduction, Methods, Results, Ablation, Related Work, Chinese notes to
  English prose, Abstract, and Conclusion writing cases.
- Added `tests/outputs/model_runs/writing/manifest_rich.json` with prompt
  paths, output paths, SHA-256 hashes, evidence level, CI-control status, and
  interactive-generation provenance.
- Added `evals/results/078d53e_rich_writing_model_eval.jsonl` with strict local
  scoring for draft-first behavior, manuscript-prose-first behavior, evidence
  use, boundary preservation, and showcase placement.
- Updated README and Pages so the homepage now showcases the richer Ablation,
  Results, and Methods outputs, while the older `ce1478f` outputs are retained
  as previous behavior evidence.
- This entry is local single-run writing evidence only. It is not CI proof,
  multi-run stability proof, or top-tier-ready proof.

## Record draft-first writing model outputs

- Ran local Codex in read-only mode against the six draft-first writing prompt
  fixtures at base commit `ce1478f`.
- Added raw final-answer artifacts under `tests/outputs/model_runs/writing/`.
- Added `tests/outputs/model_runs/writing/manifest.json` with prompt paths,
  output paths, command strings, SHA-256 hashes, evidence level, and CI-control
  status.
- Added `evals/results/ce1478f_writing_model_eval.jsonl` to record local
  single-run behavior checks for draft-first order, evidence use, boundary
  preservation, and audit/checklist regression risk.
- Updated README and Pages so recorded draft-first writing outputs are linked
  separately from maintainer-written golden examples.
- This entry is local single-run writing evidence only. It is not CI proof,
  multi-run stability proof, or top-tier-ready proof.

## Separate normal user path from maintainer evidence

- Added explicit README guidance that normal users only need `skills/_shared`
  and `skills/engineering-*`; `scripts/`, `tests/`, and `evals/` are for
  maintainers and reviewers.
- Moved first-screen provenance details for the notes-to-manuscript demo below
  the normal user path, while keeping full recorded output links and evidence
  boundaries later in the README.
- Added the `Problem / Prior limitation / Method / Evidence / Boundary` input
  template near Quick Start so users can ask for bounded manuscript prose
  without reading repository QA assets.
- Reworked the Pages homepage navigation and evidence wording so install/demo
  paths appear before maintainer quality evidence.
- Added `scripts/README.md` to label repository scripts as maintainer-only QA
  tools.
- Cleaned local absolute paths from JSON/JSONL demo and eval provenance records
  by replacing them with `<repo-root>`.
- Extended private/stale pattern scanning to HTML, JSON, and JSONL files.

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
