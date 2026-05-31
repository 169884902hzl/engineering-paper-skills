# Engineering Paper Skills

Evidence-bound Codex skills for English engineering research papers.

> **Statement**
>
> - This project provides six task skills plus a routing skill for English
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

These skills do not replace real experiments, citation checking, advisor review,
venue instructions, or author judgment. They cannot verify that an experiment is
true, that a citation exists, or that a result is valid unless the relevant
source material and verification tools are provided. When evidence is missing,
the skills should ask for the missing evidence, downgrade the claim, or mark the
output as unsupported.

## Quick Start

```bash
git clone https://github.com/169884902hzl/engineering-paper-skills.git
cd engineering-paper-skills
cp -a skills/_shared skills/engineering-* ~/.codex/skills/
```

Restart Codex, then run:

```text
Use $engineering-writing to draft a five-sentence abstract from this evidence:
- Method: perception-guided insertion with guarded execution.
- Evidence: 92% success over 50 real-robot trials.
- Boundary: one object family and one fixture geometry.
Do not add citations, baselines, objects, or extra numbers.
```

For repository QA:

```bash
python scripts/validate_repo.py
python scripts/check_expected_behavior.py --spec-dir tests/expected
for s in skills/engineering-*; do
  python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$s"
done
```

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
| Unsure which workflow to use, or planning a mixed paper task | `engineering-paper-router` |
| Audit paper logic, claim-evidence gaps, section drift, and visual overclaims before rewriting | `engineering-paper-auditor` |
| Plan or draft paper sections from claims, notes, figures, or results | `engineering-writing` |
| Improve English prose, flow, hedging, terminology, and anti-generic wording | `engineering-polishing` |
| Design figure/table responsibilities, captions, and visual evidence flow | `engineering-figure-table` |
| Triage reviewer/advisor comments and draft evidence-linked responses | `engineering-response` |
| Check manuscript readiness, LaTeX build state, claim-evidence alignment, and submission risks | `engineering-validation` |

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
skill is not considered release-ready only because `quick_validate.py` passes.
At minimum, validate every skill directory, check relative links, scan for
private paths and stale wording, and review adversarial prompts that try to
induce unsupported claims.

```bash
python scripts/validate_repo.py
python scripts/check_expected_behavior.py --spec-dir tests/expected
for s in skills/engineering-*; do
  python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$s"
done
```

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

## Files

- `skills/_shared/`: shared evidence-bound, citation-boundary, claim-strength,
  list-to-argument, terminology-ledger, source-note, and output-mode rules
- `skills/engineering-paper-router/`: routing skill for ambiguous or mixed paper
  tasks
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
- `tests/prompts/`: minimal, realistic, and adversarial prompt specs for each
  skill
- `tests/outputs/golden/`: golden output snapshots for expected-behavior checks
- `tests/expected/`: structured expected-behavior specs for prompt checks,
  including forbidden regexes, forbidden claim patterns, and required output
  sections
- `NOTICE.md`: third-party license notices
- `OPEN_SOURCE_QA.md`: validation commands and release checks

## Roadmap

- Add executable prompt regression runs once a stable non-interactive Codex CLI
  command is selected for this repository.
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

The goal is not to make papers sound longer or more impressive. The goal is to
make technical claims clear, bounded, and supported.
