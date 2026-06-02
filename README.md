# Engineering Paper Skills

Evidence-bound Codex skills for **engineering paper writing**, **manuscript
audit**, **reviewer response**, **figure/table claim checks**, and **research
paper validation** for robotics, machine learning, control, and systems papers.

Most users should start with **`$engineering-paper-coach`**. Give it research
notes, draft text, results, figures, or reviewer comments; it will either write
within the supplied evidence, downgrade unsupported claims, or tell you what
evidence is missing.

Normal users only need `skills/_shared` and `skills/engineering-*`. The
`scripts/`, `tests/`, and `evals/` directories are for maintainers and
reviewers, not for ordinary skill use.

This is a beta skill suite. It does not replace experiments, citation
verification, advisor review, official venue instructions, or author judgment.
It should not invent methods, baselines, citations, metrics, figures, line
numbers, deployment tests, or submission readiness.

## What It Can Write

The example below shows the normal user path: paste the paper problem, prior
limitation, method, evidence, and boundary; get bounded manuscript prose. The
full provenance for this example is linked later in this README.

**Input**

```text
Use $engineering-writing to turn these notes into one English manuscript
paragraph.

Target paper type:
Robotics conference paper.

Problem:
Contact-rich insertion fails when visual occlusion hides the peg-hole alignment
and the controller continues with a poor pose estimate.

Prior limitation:
Fixed overhead or side cameras can lose task-relevant visibility during
insertion. Open-loop insertion does not react to pose uncertainty or contact
deviations.

Method:
The system uses overhead and side RGB-D observations. It estimates insertion
pose and confidence. When confidence is low, it requests an additional view. A
guarded insertion controller stops if force or pose deviation exceeds a limit.

Evidence:
Full system: 84% success over 180 trials.
Fixed overhead camera: 69%.
Fixed side camera: 72%.
Open-loop controller: 61%.

Boundary:
One 7-DoF robot arm.
One tabletop fixture.
One cylindrical peg family.
No confidence intervals.
No statistical significance test.
No cross-robot test.
No industrial deployment test.
No ablation isolating view selection from guarded execution.
```

**Example manuscript paragraph**

```text
Contact-rich insertion can fail when visual occlusion hides peg-hole alignment
and the controller continues from a poor pose estimate. Fixed overhead or side
RGB-D cameras may lose task-relevant visibility during insertion, while
open-loop insertion does not react to pose uncertainty or contact deviations.
We study a system that uses overhead and side RGB-D observations to estimate
insertion pose and confidence, requests an additional view when confidence is
low, and applies a guarded insertion controller that stops when force or pose
deviation exceeds a limit. In 180 trials, the full system achieved 84% success,
compared with 69% for a fixed overhead camera, 72% for a fixed side camera, and
61% for an open-loop controller. This evidence supports a bounded system-level
improvement in the tested setup, but it is limited to one 7-DoF robot arm, one
tabletop fixture, and one cylindrical peg family, with no confidence intervals,
no statistical significance test, no cross-robot test, no industrial deployment
test, and no ablation isolating view selection from guarded execution.
```

**Why this is evidence-bound**

- It uses the supplied problem, prior limitation, method, numbers, and boundary.
- It does not add citations, baselines, objects, robots, statistics, or
  deployment evidence.
- It turns rough notes into manuscript prose instead of only refusing unsafe
  claims.

Better input evidence produces better manuscript prose. If evidence is missing,
the skill should downgrade the claim, write a scaffold, or mark the gap instead
of inventing results.

## Quick Start

```bash
git clone https://github.com/169884902hzl/engineering-paper-skills.git
cd engineering-paper-skills
cp -a skills/_shared skills/engineering-* ~/.codex/skills/
```

Restart Codex, then run:

```text
Use $engineering-paper-coach to turn these research notes into one bounded
English manuscript paragraph:

Problem:
[what fails or matters]

Prior limitation:
[what existing approach cannot handle]

Method:
[what your method does]

Evidence:
[numbers, comparisons, figures, tables, or qualitative evidence]

Boundary:
[what is not tested or not supplied]
```

## Which Skill Should I Use First?

| Task | Start with |
|---|---|
| I have notes and want practical Markdown guidance | `engineering-paper-coach` |
| I want to audit a section before rewriting | `engineering-paper-auditor` |
| I want to draft Abstract, Introduction, Methods, or Experiments | `engineering-writing` |
| I want to polish text without strengthening claims | `engineering-polishing` |
| I want to check figures, tables, captions, or result prose | `engineering-figure-table` |
| I need to respond to reviewer or advisor comments | `engineering-response` |
| I need readiness triage before submission | `engineering-validation` |

For more usage examples, see the [Demo Gallery](docs/demo.html). Repository QA
and behavior-evidence details are in the maintainer section below.

## Project Overview

Engineering Paper Skills is a Codex skill suite for experiment-heavy engineering
papers. It is designed for authors working on robotics, control, perception,
learning, systems, devices, benchmarks, and other technical manuscripts where
claims must stay tied to concrete evidence.

This project is useful for:

- drafting titles, abstracts, introductions, related work, methods, experiments,
  discussions, and conclusions
- turning notes, outlines, results, and figure plans into manuscript structure
- polishing English academic prose without changing factual content
- designing figures, tables, captions, and result narratives
- preparing point-by-point responses to advisor, editor, or reviewer comments
- checking manuscript readiness before submission

## Skill Set

| Use case | Skill |
|---|---|
| Quick conservative writing, audit, polishing, response planning, or readiness triage in Markdown | `engineering-paper-coach` |
| Unsure which workflow to use, or planning a mixed paper task | `engineering-paper-router` |
| Audit paper logic, claim-evidence gaps, section drift, and visual overclaims before rewriting | `engineering-paper-auditor` |
| Plan or draft paper sections from claims, notes, figures, or results | `engineering-writing` |
| Improve English prose, flow, hedging, terminology, and anti-generic wording | `engineering-polishing` |
| Design figure/table responsibilities, captions, and visual evidence flow | `engineering-figure-table` |
| Triage reviewer/advisor comments and draft evidence-linked responses | `engineering-response` |
| Check manuscript readiness, LaTeX build state, claim-evidence alignment, and submission risks | `engineering-validation` |

## Use Case Examples

### Draft-First Writing Examples

These golden examples define the intended WRITE-mode behavior: manuscript prose
comes first, followed by short notes on structure, evidence, and boundaries.
They are maintainer-written expected outputs, not recorded model-run artifacts.

| Writing task | Prompt fixture | Expected draft-first output |
|---|---|---|
| Abstract from minimal evidence | [writing_min.md](tests/prompts/writing_min.md) | [writing_min.md](tests/outputs/golden/writing_min.md) |
| Methods reader path from module notes | [writing_methods_reader_path.md](tests/prompts/writing_methods_reader_path.md) | [writing_methods_reader_path.md](tests/outputs/golden/writing_methods_reader_path.md) |
| Results paragraph from table-like evidence | [writing_results_interpretation.md](tests/prompts/writing_results_interpretation.md) | [writing_results_interpretation.md](tests/outputs/golden/writing_results_interpretation.md) |
| Ablation interpretation from component rows | [writing_ablation_interpretation.md](tests/prompts/writing_ablation_interpretation.md) | [writing_ablation_interpretation.md](tests/outputs/golden/writing_ablation_interpretation.md) |
| Two-paragraph Conclusion from results and limits | [writing_conclusion_two_paragraph.md](tests/prompts/writing_conclusion_two_paragraph.md) | [writing_conclusion_two_paragraph.md](tests/outputs/golden/writing_conclusion_two_paragraph.md) |
| Coach writing request with draft-first output | [coach_write_draft_first.md](tests/prompts/coach_write_draft_first.md) | [coach_write_draft_first.md](tests/outputs/golden/coach_write_draft_first.md) |

**Example excerpt: Methods reader path**

```text
The execution path begins with overhead and side RGB-D observations, which are
used to estimate the insertion pose and an associated confidence score. When
the confidence score is low, the system requests an additional view before
continuing the insertion attempt. The guarded insertion controller then
executes the motion while monitoring force and pose deviation...
```

**Example excerpt: Ablation interpretation**

```text
Directly querying action hints reaches only 17% success, indicating that raw
image-space reasoning is not sufficient for reliable manipulation in the
evaluated task family. Adding geometry-aware execution increases success to
23%, suggesting that better action realization helps...
```

### Recorded Local Demos

These use cases are backed by recorded local Codex outputs. The prompt fixtures
are useful copyable starting points; the outputs are raw local final messages
from Codex, not polished golden examples.

| Use case | Prompt fixture | Recorded local output |
|---|---|---|
| Notes to manuscript paragraph | [demo_notes_to_manuscript_paragraph.md](tests/prompts/demo_notes_to_manuscript_paragraph.md) | [demo_notes_to_manuscript_paragraph_2dc9571.md](tests/outputs/model_runs/demo/demo_notes_to_manuscript_paragraph_2dc9571.md) |
| Claim audit | [demo_claim_audit.md](tests/prompts/demo_claim_audit.md) | [demo_claim_audit_681d305.md](tests/outputs/model_runs/demo/demo_claim_audit_681d305.md) |
| Results paragraph | [demo_results_paragraph.md](tests/prompts/demo_results_paragraph.md) | [demo_results_paragraph_681d305.md](tests/outputs/model_runs/demo/demo_results_paragraph_681d305.md) |
| Conservative polishing | [demo_polishing_claim_inflation.md](tests/prompts/demo_polishing_claim_inflation.md) | [demo_polishing_claim_inflation_681d305.md](tests/outputs/model_runs/demo/demo_polishing_claim_inflation_681d305.md) |
| Figure/table source-data consistency | [demo_figure_source_data_consistency.md](tests/prompts/demo_figure_source_data_consistency.md) | [demo_figure_source_data_consistency_681d305.md](tests/outputs/model_runs/demo/demo_figure_source_data_consistency_681d305.md) |
| Reviewer response truthfulness | [demo_response_truthfulness.md](tests/prompts/demo_response_truthfulness.md) | [demo_response_truthfulness_681d305.md](tests/outputs/model_runs/demo/demo_response_truthfulness_681d305.md) |
| Validation readiness triage | [demo_validation_readiness.md](tests/prompts/demo_validation_readiness.md) | [demo_validation_readiness_681d305.md](tests/outputs/model_runs/demo/demo_validation_readiness_681d305.md) |
| Related Work nearest-neighbor distinction | [demo_related_work_nearest_neighbor.md](tests/prompts/demo_related_work_nearest_neighbor.md) | [demo_related_work_nearest_neighbor_681d305.md](tests/outputs/model_runs/demo/demo_related_work_nearest_neighbor_681d305.md) |
| Methods execution path | [demo_methods_execution_path.md](tests/prompts/demo_methods_execution_path.md) | [demo_methods_execution_path_681d305.md](tests/outputs/model_runs/demo/demo_methods_execution_path_681d305.md) |

Full provenance is recorded in
[tests/outputs/model_runs/demo/manifest.json](tests/outputs/model_runs/demo/manifest.json).

The notes-to-manuscript paragraph hero example is stored at
[tests/outputs/model_runs/demo/demo_notes_to_manuscript_paragraph_2dc9571.md](tests/outputs/model_runs/demo/demo_notes_to_manuscript_paragraph_2dc9571.md).
It is local single-run evidence, not CI-controlled behavior proof.

### Recorded Output Excerpts

Excerpted for readability; see the linked artifacts for the full raw outputs.

**Notes to manuscript paragraph**

```text
Contact-rich insertion can fail when visual occlusion hides peg-hole alignment
and the controller continues from a poor pose estimate. Fixed overhead or side
RGB-D cameras may lose task-relevant visibility during insertion, while
open-loop insertion does not react to pose uncertainty or contact deviations.
```

**Related Work nearest-neighbor distinction**

```text
The strongest novelty claim is not yet safe. The supplied notes support a
positioning hypothesis, not a fully verified literature gap: the paper appears
to combine confidence-triggered additional RGB-D views with guarded
contact-rich insertion, but the author has not yet shown that prior work lacks
this exact combination.
```

**Results paragraph**

```text
These results support a bounded system-level claim that combining multi-view
perception with guarded execution improves insertion success in the tested
single-arm, single-fixture, cylindrical-peg setting. However, the experiment
does not isolate the individual effects of view selection and guarded execution.
```

**Figure/table audit**

```text
Figure 3 and Table 1 support only a limited claim: the full system reports a
higher success rate than the listed baselines under the tested protocol.
They do not support claims of statistical significance, causal validation,
robust generalization, industrial deployment readiness, or solving insertion
under occlusion.
```

**Reviewer response truthfulness**

```text
Package status: Revision plan only, not a final reviewer response.
Main risk: The draft falsely claims added stress tests, Table 3, final line
numbers, and broad generalization.
```

## Installation

### Prerequisites

- Codex with local skills support enabled.
- A writable Codex skills directory, usually `~/.codex/skills/`.
- Python 3 is only needed for repository QA scripts, not for normal skill use.
- Optional: LaTeX tools if you want `engineering-validation` to compile paper
  projects.

### Method 1: Clone and Copy Skills

Clone this repository:

```bash
git clone https://github.com/169884902hzl/engineering-paper-skills.git
cd engineering-paper-skills
```

Copy the skill folders and shared references into your Codex skills directory:

```bash
cp -a skills/_shared skills/engineering-* ~/.codex/skills/
```

Restart Codex so the new skills are loaded.

### Install One Skill

```bash
cp -a skills/_shared skills/engineering-writing ~/.codex/skills/
```

Use the same pattern for any other skill directory.

### Update

```bash
cd engineering-paper-skills
git pull
cp -a skills/_shared skills/engineering-* ~/.codex/skills/
```

Restart Codex after updating.

### Uninstall

Remove the installed skill directories:

```bash
rm -rf ~/.codex/skills/engineering-writing \
       ~/.codex/skills/engineering-polishing \
       ~/.codex/skills/engineering-figure-table \
       ~/.codex/skills/engineering-response \
       ~/.codex/skills/engineering-validation \
       ~/.codex/skills/engineering-paper-auditor \
       ~/.codex/skills/engineering-paper-coach \
       ~/.codex/skills/engineering-paper-router \
       ~/.codex/skills/_shared
```

### Troubleshooting

- Copy the whole skill directory, not only `SKILL.md`.
- Restart Codex after install or update.
- If a skill does not trigger, call it explicitly with `$skill-name`.
- If validation claims are needed, provide the manuscript root and let the agent
  report exactly which commands were run.

### Method 2: Manual Install

1. Download this repository as a ZIP file or clone it locally.
2. Copy each folder under `skills/` into your Codex skills directory.
3. Make sure the installed structure looks like this:

```text
~/.codex/skills/
├── _shared/
├── engineering-writing/
│   ├── SKILL.md
│   ├── agents/
│   └── references/
├── engineering-polishing/
├── engineering-figure-table/
├── engineering-response/
├── engineering-validation/
├── engineering-paper-auditor/
├── engineering-paper-coach/
└── engineering-paper-router/
```

## Verify Installation

After restarting Codex, try:

```text
Use $engineering-writing to draft an abstract from the following contribution,
method, results, and limitation notes:
[paste your notes]
```

For local structure validation, run:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  ~/.codex/skills/engineering-writing
```

Repeat the command for the other installed skill directories when needed.

## Maintainer Validation

Normal users do not need this section. Before publishing changes to this
repository, maintainers should run the repository QA checks. A skill is not
considered publish-ready only because `quick_validate.py` passes. At minimum,
validate every skill directory, check relative links, scan for private paths
and stale wording, and review adversarial prompts that try to induce
unsupported claims.

```bash
python scripts/validate_repo.py
python scripts/check_expected_behavior.py --spec-dir tests/expected
python scripts/check_quality_assets.py
python scripts/check_response_diff.py
python scripts/check_venue_profiles.py
for s in skills/engineering-*; do
  python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$s"
done
```

`tests/outputs/golden/` contains expected snapshots. `tests/outputs/model_runs/`
contains recorded local model-run artifacts when available. Treat both as review
evidence, not as automatic certification of top-tier paper quality.

## Basic Usage

### Draft a Section

```text
Use $engineering-writing to write an Introduction section from this outline:

[paste problem, gap, method, evidence, and contribution notes]
```

### Audit Before Rewriting

```text
Use $engineering-paper-auditor to audit this manuscript section before I revise
it:

[paste section, claims, figures/tables, and evidence notes]
```

### Polish Existing Text

```text
Use $engineering-polishing to polish the following paragraph while preserving
all facts, numbers, and claim strength:

[paste paragraph]
```

### Plan Figures and Tables

```text
Use $engineering-figure-table to audit whether these figures and tables support
the paper's main claims:

[paste figure list, table list, and claims]
```

### Respond to Reviews

```text
Use $engineering-response to classify these reviewer comments and draft a
point-by-point response plan:

[paste comments]
```

### Validate Before Submission

```text
Use $engineering-validation to check whether this LaTeX manuscript is ready for
submission:

[paste project path and target venue constraints]
```

## Example

**Input**

```text
Target section: Abstract
Problem: Contact-rich robotic insertion is sensitive to pose error and visual
occlusion.
Method: A perception-guided policy uses multi-view RGB-D observations and a
guarded execution stage.
Evidence: 92% success rate over 50 real-robot trials; ablation without guarded
execution drops to 74%.
Boundary: Tested on one object family and one fixture geometry.
```

**Expected behavior**

The skill should produce a concise English abstract that states the problem,
method, evidence, and limitation. It should not invent new baselines, additional
objects, unseen environments, or broader deployment claims.

## Core Rules

The skills are organized around five writing constraints:

1. **Evidence boundary**: use only the facts, results, mechanisms, and
   limitations provided by the author or visible in the project files.
2. **Section responsibility**: each section should do its own job instead of
   repeating the same claims in different wording.
3. **Argument before language**: fix claim structure before polishing sentences.
4. **Figure/table accountability**: every major visual should support a specific
   manuscript claim.
5. **Validation before readiness**: do not call a paper ready without fresh
   checks of the live draft, evidence, citations, figures, tables, and build
   state.

## For Maintainers and Reviewers

Normal skill users do not need the `scripts/`, `tests/`, or `evals/`
directories. They are review evidence for maintainers, external reviewers, and
contributors, but they are not required for a first-time user to understand how
to use the skills.

- [Demo gallery](https://169884902hzl.github.io/engineering-paper-skills/demo.html)
- [Quality gates](https://169884902hzl.github.io/engineering-paper-skills/quality-gates.html)
- [Discovery checklist](https://169884902hzl.github.io/engineering-paper-skills/discovery.html)
- [Full-paper realistic audit](tests/outputs/golden/full_paper_realistic_audit.md)
- [Structured JSON audit](tests/outputs/golden/full_paper_realistic_structured_audit.json)
- [Sentence-level claim and evidence audit](tests/outputs/golden/full_paper_realistic_sentence_audit.md)
- [AI-smell polishing example](tests/outputs/golden/polishing_ai_smell.md)
- [Figure/table panel-claim audit](tests/outputs/golden/figure_table_panel_claim.md)
- [Recorded local model-run artifact](tests/outputs/model_runs/full_paper_realistic_audit_8da3ceb.md)
- [Known-good commit matrix](KNOWN_GOOD.md)
- [No-release beta changelog](CHANGELOG.md)
- [Maintainer-only QA scripts](scripts/README.md)

## Files

### Runtime Skill Files

- `skills/_shared/`: shared evidence-bound, citation-boundary, claim-strength,
  sentence-role, story-spine, AI-writing, list-to-argument,
  terminology-ledger, source-note, and output-mode rules
- `skills/engineering-paper-router/`: routing skill for ambiguous or mixed paper
  tasks
- `skills/engineering-paper-coach/`: lightweight conservative Markdown entry
  skill for quick writing, audit, polishing, response planning, and readiness
  triage
- `skills/engineering-paper-auditor/`: reviewer-like paper audit skill for
  claim-evidence, section-boundary, visual, and readiness risks
- `skills/engineering-writing/`: drafting and manuscript-structure skill
- `skills/engineering-polishing/`: English polishing and claim-boundary skill
- `skills/engineering-figure-table/`: figure, table, caption, and visual
  evidence skill
- `skills/engineering-response/`: reviewer/advisor response skill
- `skills/engineering-validation/`: final manuscript validation skill

### Maintainer and Reviewer Files

- `scripts/validate_repo.py`: repository structure, link, wording, and prompt
  coverage checks
- `scripts/check_expected_behavior.py`: structured expected-behavior validation
- `scripts/run_prompt_regression.py`: optional prompt regression runner
- `scripts/check_quality_assets.py`: long-fixture, rubric, and quality-asset
  validation
- `scripts/check_response_diff.py`: response old/new manuscript fixture sanity
  check
- `tests/prompts/`: minimal, realistic, and adversarial prompt specs for each
  skill
- `tests/fixtures/long/`: longer flawed manuscript fixtures for story,
  sentence, AI-smell, and validation review
- `tests/fixtures/full_paper/`: full-paper flawed manuscript fixture for
  story, paragraph-transition, section-dependency, response, and validation
  review
- `tests/outputs/golden/`: golden output snapshots for expected-behavior checks
- `tests/expected/`: structured expected-behavior specs for prompt checks,
  including forbidden regexes, forbidden claim patterns, and required output
  sections
- `evals/`: manual top-tier paper quality rubric and recorded gold-fixture
  review results, plus a draft-first writing quality rubric
- `NOTICE.md`: third-party license notices
- `OPEN_SOURCE_QA.md`: validation commands and quality checks

## Roadmap

- Expand CI-controlled behavior-regression artifacts and human-scored eval
  records beyond local single-run evidence.
- Promote draft-first writing demos from golden expected outputs to recorded
  local model-run artifacts once the writing prompts are stable.
- Move structured JSON checks toward span-grounded claim/evidence and response
  verification contracts.
- Add more full before/after examples for each skill.
- Add LaTeX project QA helpers for labels, citations, page count, and warnings.
- Consider optional packaging once the manual installation path is stable.

## Manual Use Without Installing

You can also use the instructions manually:

1. Open the relevant `SKILL.md`.
2. Provide the manuscript section, target venue, available evidence, and known
   limitations.
3. Ask the model to follow the skill rules while preserving all facts.
4. Check whether any unsupported fact, metric, mechanism, reference, or claim was
   added.
5. If unsupported content appears, remove it or rerun the task with stricter
   evidence boundaries.

## Notes

- Better input evidence produces better manuscript text.
- These skills do not verify whether experimental results are true.
- These skills do not automatically create or validate references.
- For submission work, pair writing and polishing with `engineering-validation`.
- Keep private manuscripts, reviewer letters, and unpublished data out of public
  issues and pull requests.

## Contributing

Contributions are welcome, especially improvements that make the skills more
precise, conservative, and useful for real engineering papers.

Good contribution areas include:

- more section-specific writing checks
- stronger figure/table QA examples
- reviewer-response patterns for different venues
- validation checklists for LaTeX and submission workflows
- clearer anti-overclaim rules

Before opening a pull request, run `python scripts/validate_repo.py` and
`python scripts/check_expected_behavior.py --spec-dir tests/expected`. Do not
add private manuscripts, reviewer letters, unpublished data, local paths, or
unsupported paper claims to public examples.

## License and Notices

This project is released under the MIT License. Third-party license notices are
preserved in `NOTICE.md`.

## Acknowledgements

Thanks to Yuqi Cheng (`hustCYQ`) for publishing
[`phd-writing`](https://github.com/hustCYQ/phd-writing) under the MIT License.
The required third-party notice is preserved in `NOTICE.md`.

The goal is not to make papers sound longer or more impressive. The goal is to
make technical claims clear, bounded, and supported.
