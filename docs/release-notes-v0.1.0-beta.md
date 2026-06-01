# v0.1.0-beta - Evidence-bound engineering paper skills

This beta release packages Codex skills for evidence-bound engineering paper
writing, manuscript audit, polishing, figure/table claim checks, reviewer
response planning, and validation discipline.

## Highlights

- Full-paper realistic audit fixture for robotics-style engineering manuscripts.
- Story-spine, sentence-role, paragraph-transition, and section-dependency checks.
- Semantic expected-behavior specs for full-paper audit, AI-smell polishing, and
  figure/table claim consistency.
- Optional behavior regression workflow using `PROMPT_REGRESSION_COMMAND_TEMPLATE`.
- Response diff verification guidance and fixture.
- Venue-aware validation profiles for robotics, ML, and Nature-style venues.
- GitHub Pages landing page, citation metadata, and research-software metadata.

## Evidence Boundary

This is a beta. Golden outputs, static quality checks, and recorded local model
runs are review artifacts, not proof of stable top-tier behavior on arbitrary
unseen manuscripts.

## Known Limitations

- Behavior regression requires a configured model command template.
- Current structured checks are stronger than keyword checks but still not full
  semantic entailment.
- Citation truth, experiment truth, and venue compliance require external
  sources and user-provided artifacts.
- The suite does not replace real experiments, advisor review, citation
  verification, or official venue instructions.
