# Engineering Paper Skills

> **Statement**
>
> - This project provides five Codex skills for English engineering paper
>   writing, polishing, figures and tables, revision responses, and validation.
> - The skills help organize and express author-provided research content. They
>   do not replace real experiments, citation checking, advisor review, or venue
>   requirements.
> - The skills are conservative by default: they should not invent mechanisms,
>   data, references, metrics, limitations, or conclusions.
> - If the input evidence is thin, the skills should expose the gap instead of
>   producing overconfident manuscript prose.

---

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

| Skill | Use it for |
|---|---|
| `engineering-writing` | Paper structure, section drafting, contribution-evidence maps, and full manuscript argument |
| `engineering-polishing` | English prose polishing, paragraph flow, claim strength, terminology, and anti-generic wording checks |
| `engineering-figure-table` | Figure/table planning, captions, table notes, visual responsibility, and consistency checks |
| `engineering-response` | Comment classification, revision planning, and point-by-point response drafting |
| `engineering-validation` | Live-draft checks, LaTeX build checks, evidence audits, citation/figure/table checks, and final submission QA |

## Installation

### Method 1: Clone and Copy Skills

Clone this repository:

```bash
git clone https://github.com/169884902hzl/engineering-paper-skills.git
cd engineering-paper-skills
```

Copy the five skill folders into your Codex skills directory:

```bash
cp -a skills/engineering-* ~/.codex/skills/
```

Restart Codex so the new skills are loaded.

### Method 2: Manual Install

1. Download this repository as a ZIP file or clone it locally.
2. Copy each folder under `skills/` into your Codex skills directory.
3. Make sure the installed structure looks like this:

```text
~/.codex/skills/
├── engineering-writing/
│   ├── SKILL.md
│   ├── agents/
│   └── references/
├── engineering-polishing/
├── engineering-figure-table/
├── engineering-response/
└── engineering-validation/
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

Repeat the command for the other four installed skill directories when needed.

## Basic Usage

### Draft a Section

```text
Use $engineering-writing to write an Introduction section from this outline:

[paste problem, gap, method, evidence, and contribution notes]
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

- `skills/engineering-writing/`: drafting and manuscript-structure skill
- `skills/engineering-polishing/`: English polishing and claim-boundary skill
- `skills/engineering-figure-table/`: figure, table, caption, and visual
  evidence skill
- `skills/engineering-response/`: reviewer/advisor response skill
- `skills/engineering-validation/`: final manuscript validation skill
- `NOTICE.md`: third-party license notices
- `OPEN_SOURCE_QA.md`: validation commands and release checks

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

The goal is not to make papers sound longer or more impressive. The goal is to
make technical claims clear, bounded, and supported.
