# No-release beta changelog

This project currently uses commit-based beta tracking instead of GitHub
releases. Entries below document quality-gate changes that matter for external
review and reuse.

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
