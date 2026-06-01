# Engineering Paper Skills

Evidence-bound Codex skills for engineering paper writing, manuscript audit,
polishing, figure/table claim checks, reviewer response, and validation.

Start with **`$engineering-paper-coach`** if you want practical Markdown
guidance. Use the specialized skills when you need a deeper audit, section
drafting, figure/table review, reviewer-response planning, or
submission-readiness triage.

This beta skill suite is designed for robotics, machine learning, control,
systems, and other experiment-heavy engineering papers where claims must stay
tied to supplied methods, results, figures, tables, citations, and limitations.

## What It Does

- Turns rough research notes into conservative paper outlines or bounded
  manuscript paragraphs.
- Audits whether claims are stronger than the supplied evidence.
- Polishes academic prose without adding facts or increasing claim strength.
- Checks whether figures, tables, captions, and result narratives support the
  stated claims.
- Helps draft reviewer or advisor responses without pretending that experiments,
  tables, citations, line numbers, or manuscript edits already exist.
- Reports readiness with explicit states such as `PASS`, `FAIL`, `PARTIAL`,
  `NOT_RUN`, `UNKNOWN`, and `CANNOT_DETERMINE`.

> **Statement**
>
> - This is a beta engineering-paper skill suite, not a guarantee of
>   top-tier-paper readiness. It provides strict writing and validation
>   workflows, but final claims, experiments, citations, venue compliance, and
>   AI-use disclosure remain the author's responsibility.
> - This project provides a lightweight coaching skill, six task skills, and a
>   routing skill for English
>   engineering paper auditing, writing, polishing, figures and tables,
>   revision responses, and validation.
> - The skills help organize and express author-provided research content. They
>   do not replace real experiments, citation checking, advisor review, or venue
>   requirements.
> - The skills are conservative by default: they should not invent mechanisms,
>   data, references, metrics, limitations, or conclusions.
> - If the input evidence is thin, the skills should expose the gap instead of
>   producing overconfident manuscript prose.

---

## What This Does Not Do

These skills do not replace real experiments, citation verification, advisor
review, venue instructions, or author judgment. They cannot certify that a
result is true, a citation exists, a figure proves a mechanism, or a manuscript
is submission-ready unless the relevant source files, evidence, tools, and
official venue policies are provided and checked.

If evidence is thin, the skills should expose the gap, downgrade the claim, or
produce a scaffold instead of confident manuscript prose.

## Example Provenance

The examples in this README are split into two types:

- **Illustrative examples** are hand-written for readability. They show the
  expected interaction style, but they are not recorded model-run outputs.
- **Recorded local Codex outputs** are raw final messages generated from prompt
  fixtures and stored under `tests/outputs/model_runs/demo/`. They are local
  single-run evidence, not CI-controlled proof or top-tier-readiness proof.

## Quick Illustrative Examples

### Example 1: Audit An Overclaim

Illustrative example, not a recorded model-run output.

**Input**

```text
Use $engineering-paper-coach to audit this paper claim and give a safe rewrite.

Evidence:
- 84% success over 180 trials.
- One robot arm.
- One tabletop fixture.
- One object family.
- No cross-robot test.
- No industrial deployment test.
- No statistical significance test.

Draft claim:
"The system is deployment-ready and proven robust for industrial insertion."
```

**Illustrative output**

```text
Verdict: the claim is too strong for the supplied evidence.

Claim-strength audit:
- deployment readiness: unsupported; no deployment protocol or deployment log is supplied.
- robustness: unsupported beyond the tested setup; only one robot, one fixture, and one object family are supplied.
- industrial suitability: unsupported; the evidence is tabletop-only.
- bounded empirical comparison: partially supported by the 84% result over 180 trials.

Safe rewrite:
"In the evaluated tabletop insertion setup, the system achieved 84% success
over 180 trials on one robot arm and one object family. Cross-robot robustness,
industrial deployment, and broader object variation remain untested."

Evidence needed for stronger wording:
- cross-robot or cross-fixture evaluation
- object-family variation
- occlusion or stress-test protocol
- uncertainty estimates or statistical analysis
- deployment protocol
```

### Example 2: Do Not Fake A Reviewer Response

Illustrative example, not a recorded model-run output.

**Input**

```text
Use $engineering-response to audit this draft response.

Reviewer comment:
"The paper overclaims robustness. Please add stress tests and clarify whether
the method generalizes beyond the tabletop setup."

Supplied materials:
- No revised manuscript diff.
- No new stress-test data.
- No Table 3.
- Final line numbers are unavailable.

Draft response:
"We added new stress tests in Table 3 and revised Lines 210-225 to show robust
generalization."
```

**Illustrative output**

```text
Response mode: plan, not final response.

| Reviewer concern | Draft response claim | Supplied evidence | Verdict | Safe action |
|---|---|---|---|---|
| Add stress tests | "We added new stress tests" | No stress-test data supplied | FAIL | Do not claim completed |
| Add Table 3 | "Table 3" | No Table 3 supplied | FAIL | Mark as missing evidence |
| Cite final location | "Lines 210-225" | Final line numbers unavailable | FAIL | Use placeholder until final build |
| Clarify generalization | "robust generalization" | One tabletop setup only | FAIL | Narrow to tested setup |

Safe response plan:
"We agree that the original robustness wording was too broad. Based on the
current evidence, we will narrow the claim to the evaluated tabletop setup.
Additional stress-test results and final line numbers cannot be claimed until
the revised manuscript and data are available."

Required before final response:
- revised manuscript diff
- stress-test protocol and results, if performed
- final compiled line numbers
```


## Quick Start

```bash
git clone https://github.com/169884902hzl/engineering-paper-skills.git
cd engineering-paper-skills
cp -a skills/_shared skills/engineering-* ~/.codex/skills/
```

Restart Codex, then run:

```text
Use $engineering-paper-coach to audit this claim and give a safe rewrite:
Evidence: 84% success over 180 trials on one robot, one tabletop fixture, and
one object family.
Draft: "The system is deployment-ready and proven robust for industrial insertion."
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

For structured JSON audits, regression artifacts, and quality gates, see the
[Demo Gallery](docs/demo.html) and [Quality Gates](docs/quality-gates.md).

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

These use cases are backed by recorded local Codex outputs. The prompt fixtures
are useful copyable starting points; the outputs are raw local final messages
from Codex, not polished golden examples.

| Use case | Prompt fixture | Recorded local output |
|---|---|---|
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

### Recorded Output Excerpts

Excerpted for readability; see the linked artifacts for the full raw outputs.

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
- Python 3 for repository QA scripts.
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

## Validation

Before publishing changes to this repository, run the repository QA checks. A
skill is not considered publish-ready only because `quick_validate.py` passes.
At minimum, validate every skill directory, check relative links, scan for
private paths and stale wording, and review adversarial prompts that try to
induce unsupported claims.

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

## Quality Evidence for Maintainers and Reviewers

These links are review evidence for the repository. They are useful for
maintainers, external reviewers, and contributors, but they are not required for
a first-time user to understand how to use the skills.

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

## Files

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
  review results
- `NOTICE.md`: third-party license notices
- `OPEN_SOURCE_QA.md`: validation commands and quality checks

## Roadmap

- Expand CI-controlled behavior-regression artifacts and human-scored eval
  records beyond local single-run evidence.
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
