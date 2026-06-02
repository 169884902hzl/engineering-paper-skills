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

The examples below are raw recorded Codex outputs from public writing prompt
fixtures. They show the intended user experience: rough notes, result tables,
ablation rows, Chinese source notes, or Methods notes become manuscript prose
first. These are local artifacts, not CI-controlled behavior proof and not
top-tier-ready proof.

Examples are recorded local Codex outputs; detailed provenance is in Evidence
Archive.

### Results table + diagnostic axes -> Results paragraph

```text
Input skeleton:
Full system 84% over 180 trials; fixed overhead 69%; fixed side 72%;
open-loop 61%. Diagnostic axes: overhead loses the hole near final approach,
side view preserves lateral visibility but leaves depth uncertainty, and
open-loop carries pose error into contact.
```

```text
Short excerpt from recorded output:
In contact-rich peg insertion, the best-performing policy is the one that
prevents visual ambiguity from becoming unrecovered contact error. The
confidence-triggered multi-view system achieved 84% success over 180 trials,
outperforming fixed side viewing by 12 percentage points...
```

Full artifact:
[writing_results_showcase_v2_ad6d5b4.md](tests/outputs/model_runs/writing/writing_results_showcase_v2_ad6d5b4.md).

### Ablation rows -> contribution-level ablation paragraph

```text
Input skeleton:
Naive direct hint 17%; + geometry-aware execution 23%; + target-focused
perception 44%; + overlay self-verification 76%; full mask-constrained
grounding 88%. Interpret each delta as a contribution role, not causal proof.
```

```text
Short excerpt from recorded output:
The ablation indicates that the main bottleneck in contact-rich action
grounding is not merely executing a hinted motion, but verifying that a
visually plausible hint is grounded to the intended insertion target.
```

Full artifact:
[writing_ablation_showcase_v2_ad6d5b4.md](tests/outputs/model_runs/writing/writing_ablation_showcase_v2_ad6d5b4.md).

### Chinese notes -> English manuscript paragraph

```text
Input skeleton:
遮挡下 peg-hole 插入；overhead early context but final occlusion; side lateral
view but unstable depth; open-loop carries pose error; full system 84% vs
69%/72%/61%; no significance, cross-robot, or deployment test.
```

```text
Short excerpt from recorded output:
Occlusion during the final approach, rather than initial visual recognition,
is the central failure mode in peg-hole insertion under fixed camera views.
Overhead sensing captures the global scene early but loses usable hole
visibility as the peg approaches contact...
```

Full artifact:
[writing_zh_to_en_showcase_v2_rerun_e99ca81.md](tests/outputs/model_runs/writing/writing_zh_to_en_showcase_v2_rerun_e99ca81.md).

### Methods notes -> reader-path Methods paragraph

```text
Input skeleton:
Overhead RGB-D, side RGB-D, candidate insertion pose, confidence estimate,
optional additional view, refined pose, guarded insertion controller, force
and pose-deviation stops. Explain the reader path, not a module list.
```

```text
Short excerpt from recorded output:
Because pose uncertainty that survives into contact is difficult to correct
safely, the method first resolves the insertion pose in perception and only
then commits to guarded execution.
```

Full artifact:
[writing_methods_showcase_v2_e99ca81.md](tests/outputs/model_runs/writing/writing_methods_showcase_v2_e99ca81.md).

Better input evidence produces better manuscript prose. If evidence is missing,
the skill should downgrade the claim, write a scaffold, or mark the gap instead
of inventing results.

## How To Get Strong Prose

Give the skill a concrete section target, the task bottleneck, the method
object, a result table or measured evidence, diagnostic axes or failure modes,
and the boundary of what was not tested. Ask for manuscript prose first. State
forbidden claims explicitly, especially unsupported mechanisms, deployment
readiness, broad robustness, missing statistics, and unverified citations.

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

For stronger section drafting, call `engineering-writing` directly:

```text
Use $engineering-writing to draft a showcase-grade [section name] paragraph.

Target:
[Abstract / Introduction opening / Methods overview / Results / Ablation /
Related Work / Conclusion]

Paper type:
[robotics / ML systems / control / engineering conference or journal]

Task:
[specific task, not a broad field]

Core bottleneck:
[the technical bottleneck that carries the paper contribution]

Existing routes and limitations:
- [route A]: [what it solves] but [what it misses]
- [route B]: [what it solves] but [what it misses]
- [route C]: [what it solves] but [what it misses]

Method:
[method object, not only module names]
[information flow / decision rule / intermediate representation / execution path]

Evidence:
- [main result, with numbers]
- [baseline]
- [ablation]
- [failure modes or diagnostic axes]

Boundary:
- [dataset / robot / platform / scenario scope]
- [statistical tests not performed]
- [deployment or generalization tests not performed]
- [causal mechanisms not proven]

Writing requirements:
- Produce manuscript prose first.
- Do not output an outline before the draft.
- Write like a strong engineering conference paper, but stay evidence-bound.
- Use mechanism or failure-mode interpretation, not table reading.
- Integrate boundary as scientific scope, not as apology.
- Avoid generic frames such as "X remains challenging", "To address this
  limitation", and "These results indicate" unless the sentence names a
  concrete mechanism.
- Do not invent citations, experiments, baselines, statistics, line numbers,
  deployment, novelty proof, or broad robustness.
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

### Recorded Showcase Writing Outputs

The outputs below are raw local Codex final answers. Results and Ablation from
showcase v2 remain strong hero candidates. The Abstract, Related Work,
Chinese-to-English, and Conclusion public-demo blockers were rerun at base
commit `e99ca8120a6174a9cdba7083bd71f739908c822c`, and Methods showcase v2 was
added in the same pass. Commit `8865acf6469b0dae32d16807c341c04bf249e2a3`
adds stricter public-demo checks, a boundary-first Conclusion rerun, and
three-paragraph full-section demos. These are local artifacts, not
CI-controlled behavior proof and not top-tier-ready proof.

| Writing task | Prompt fixture | Recorded local output | Review placement |
|---|---|---|---|
| Results paragraph from diagnostic axes | [writing_results_showcase_v2.md](tests/prompts/writing_results_showcase_v2.md) | [writing_results_showcase_v2_ad6d5b4.md](tests/outputs/model_runs/writing/writing_results_showcase_v2_ad6d5b4.md) | hero |
| Ablation paragraph with contribution roles | [writing_ablation_showcase_v2.md](tests/prompts/writing_ablation_showcase_v2.md) | [writing_ablation_showcase_v2_ad6d5b4.md](tests/outputs/model_runs/writing/writing_ablation_showcase_v2_ad6d5b4.md) | hero |
| Chinese notes to English manuscript argument | [writing_zh_to_en_showcase_v2_rerun.md](tests/prompts/writing_zh_to_en_showcase_v2_rerun.md) | [writing_zh_to_en_showcase_v2_rerun_e99ca81.md](tests/outputs/model_runs/writing/writing_zh_to_en_showcase_v2_rerun_e99ca81.md) | hero |
| Methods overview with reader path | [writing_methods_showcase_v2.md](tests/prompts/writing_methods_showcase_v2.md) | [writing_methods_showcase_v2_e99ca81.md](tests/outputs/model_runs/writing/writing_methods_showcase_v2_e99ca81.md) | hero |
| Six-sentence Abstract rerun | [writing_abstract_showcase_v2_rerun.md](tests/prompts/writing_abstract_showcase_v2_rerun.md) | [writing_abstract_showcase_v2_rerun_e99ca81.md](tests/outputs/model_runs/writing/writing_abstract_showcase_v2_rerun_e99ca81.md) | gallery |
| Related Work positioning rerun | [writing_related_work_showcase_v2_rerun.md](tests/prompts/writing_related_work_showcase_v2_rerun.md) | [writing_related_work_showcase_v2_rerun_e99ca81.md](tests/outputs/model_runs/writing/writing_related_work_showcase_v2_rerun_e99ca81.md) | gallery |
| Two-paragraph Conclusion rerun2 | [writing_conclusion_showcase_v2_rerun2.md](tests/prompts/writing_conclusion_showcase_v2_rerun2.md) | [writing_conclusion_showcase_v2_rerun2_8865acf.md](tests/outputs/model_runs/writing/writing_conclusion_showcase_v2_rerun2_8865acf.md) | gallery |
| Full-section Results demo v2 | [full_section_results_demo_v2.md](tests/prompts/full_section_results_demo_v2.md) | [full_section_results_demo_v2_8865acf.md](tests/outputs/model_runs/writing/full_section_results_demo_v2_8865acf.md) | gallery |
| Full-section Methods demo | [full_section_methods_demo.md](tests/prompts/full_section_methods_demo.md) | [full_section_methods_demo_8865acf.md](tests/outputs/model_runs/writing/full_section_methods_demo_8865acf.md) | gallery |
| Realistic manuscript-note Results | [realistic_robotics_manuscript_notes_results.md](tests/prompts/realistic_robotics_manuscript_notes_results.md) | [realistic_robotics_manuscript_notes_results_8865acf.md](tests/outputs/model_runs/writing/realistic_robotics_manuscript_notes_results_8865acf.md) | gallery |
| Chinese notes to Methods | [zh_notes_to_methods_showcase.md](tests/prompts/zh_notes_to_methods_showcase.md) | [zh_notes_to_methods_showcase_8865acf.md](tests/outputs/model_runs/writing/zh_notes_to_methods_showcase_8865acf.md) | gallery |
| Chinese notes to Discussion | [zh_notes_to_discussion_showcase.md](tests/prompts/zh_notes_to_discussion_showcase.md) | [zh_notes_to_discussion_showcase_8865acf.md](tests/outputs/model_runs/writing/zh_notes_to_discussion_showcase_8865acf.md) | gallery |
| Related Work verified-citation mode | [related_work_verified_citation_mode.md](tests/prompts/related_work_verified_citation_mode.md) | [related_work_verified_citation_mode_8865acf.md](tests/outputs/model_runs/writing/related_work_verified_citation_mode_8865acf.md) | evidence-only |

Full provenance is recorded in
[tests/outputs/model_runs/writing/manifest_showcase_v2.json](tests/outputs/model_runs/writing/manifest_showcase_v2.json),
[tests/outputs/model_runs/writing/manifest_showcase_v2_rerun.json](tests/outputs/model_runs/writing/manifest_showcase_v2_rerun.json),
[tests/outputs/model_runs/writing/manifest_showcase_v2_rerun2.json](tests/outputs/model_runs/writing/manifest_showcase_v2_rerun2.json),
[tests/outputs/model_runs/writing/manifest_realistic_sections.json](tests/outputs/model_runs/writing/manifest_realistic_sections.json),
and
[tests/outputs/model_runs/writing/manifest_stability.json](tests/outputs/model_runs/writing/manifest_stability.json).
The local review records are
[evals/results/e99ca81_showcase_v2_rerun_human_review.md](evals/results/e99ca81_showcase_v2_rerun_human_review.md)
and
[evals/results/8865acf_showcase_v2_rerun2_human_review.md](evals/results/8865acf_showcase_v2_rerun2_human_review.md).

### Rough Notes And Benchmark Evidence

The messy-note and de-identified benchmark prompts test ordinary rough input,
not only rich showcase prompts.

| Evidence set | Manifest | Human review |
|---|---|---|
| Messy notes: intro, results table, incomplete Related Work, mixed zh/en Methods, contradictory boundary notes | [manifest_messy_notes.json](tests/outputs/model_runs/writing/manifest_messy_notes.json) | [e99ca81_messy_notes_human_review.md](evals/results/e99ca81_messy_notes_human_review.md) |
| Three-run stability: Results, Ablation, Chinese-to-English rerun | [manifest_stability.json](tests/outputs/model_runs/writing/manifest_stability.json) | [e99ca81_stability_human_review.md](evals/results/e99ca81_stability_human_review.md) |
| De-identified benchmark and full-section Results demo | [manifest_benchmark.json](tests/outputs/model_runs/writing/manifest_benchmark.json) | [e99ca81_benchmark_human_review.md](evals/results/e99ca81_benchmark_human_review.md) |
| Minimal rough-user prompts: intro, results, Methods, Chinese notes, Related Work scaffold | [manifest_rough_user.json](tests/outputs/model_runs/writing/manifest_rough_user.json) | [8865acf_rough_user_human_review.md](evals/results/8865acf_rough_user_human_review.md) |
| Stability on rough-user and benchmark prompts | [manifest_stability_rough_benchmark.json](tests/outputs/model_runs/writing/manifest_stability_rough_benchmark.json) | [8865acf_stability_rough_benchmark_human_review.md](evals/results/8865acf_stability_rough_benchmark_human_review.md) |
| Realistic manuscript-note, citation-mode, full-section, and Chinese-note cases | [manifest_realistic_sections.json](tests/outputs/model_runs/writing/manifest_realistic_sections.json) | [8865acf_realistic_sections_human_review.md](evals/results/8865acf_realistic_sections_human_review.md) |

### Draft-First Writing Examples

These golden examples define the intended WRITE-mode behavior: manuscript prose
comes first, followed by short notes on structure, evidence, and boundaries.
They are maintainer-written expected outputs, not recorded model-run artifacts.

| Writing task | Prompt fixture | Expected draft-first output |
|---|---|---|
| Methods reader path from module notes | [writing_methods_reader_path.md](tests/prompts/writing_methods_reader_path.md) | [writing_methods_reader_path.md](tests/outputs/golden/writing_methods_reader_path.md) |
| Results paragraph from table-like evidence | [writing_results_interpretation.md](tests/prompts/writing_results_interpretation.md) | [writing_results_interpretation.md](tests/outputs/golden/writing_results_interpretation.md) |
| Ablation interpretation from component rows | [writing_ablation_interpretation.md](tests/prompts/writing_ablation_interpretation.md) | [writing_ablation_interpretation.md](tests/outputs/golden/writing_ablation_interpretation.md) |
| Two-paragraph Conclusion from results and limits | [writing_conclusion_two_paragraph.md](tests/prompts/writing_conclusion_two_paragraph.md) | [writing_conclusion_two_paragraph.md](tests/outputs/golden/writing_conclusion_two_paragraph.md) |
| Coach writing request with draft-first output | [coach_write_draft_first.md](tests/prompts/coach_write_draft_first.md) | [coach_write_draft_first.md](tests/outputs/golden/coach_write_draft_first.md) |
| Minimal abstract smoke check | [writing_min.md](tests/prompts/writing_min.md) | [writing_min.md](tests/outputs/golden/writing_min.md) |

## Evidence Archive

The remaining recorded writing outputs are retained for provenance, regression
review, and previous behavior comparison. Some are useful evidence, but they
are not public hero cards.

### Superseded Or Evidence-only Showcase Outputs

| Output | Reason |
|---|---|
| [writing_conclusion_showcase_v2_rerun_e99ca81.md](tests/outputs/model_runs/writing/writing_conclusion_showcase_v2_rerun_e99ca81.md) | Superseded by boundary-first rerun2 at `8865acf`; retained for provenance only. |
| [full_section_results_demo_e99ca81.md](tests/outputs/model_runs/writing/full_section_results_demo_e99ca81.md) | Superseded by the exactly-three-paragraph v2 output at `8865acf`; retained for provenance only. |
| [writing_abstract_showcase_v2_ad6d5b4.md](tests/outputs/model_runs/writing/writing_abstract_showcase_v2_ad6d5b4.md) | Rejected original Abstract showcase output; retained for comparison only. |
| [writing_related_work_showcase_v2_ad6d5b4.md](tests/outputs/model_runs/writing/writing_related_work_showcase_v2_ad6d5b4.md) | Evidence-only original Related Work showcase output. |
| [writing_zh_to_en_showcase_v2_ad6d5b4.md](tests/outputs/model_runs/writing/writing_zh_to_en_showcase_v2_ad6d5b4.md) | Evidence-only original Chinese-to-English showcase output. |
| [writing_conclusion_showcase_v2_ad6d5b4.md](tests/outputs/model_runs/writing/writing_conclusion_showcase_v2_ad6d5b4.md) | Evidence-only original Conclusion showcase output. |

### Recorded Rich Writing Outputs

The outputs below are raw local Codex final answers generated from rich writing
prompt fixtures at base commit `078d53e7b5925cf7c56b3b4696c8a35b9ac8d475`.
They are recorded local single-run artifacts, not CI-controlled behavior proof,
not multi-run stability proof, and not top-tier-ready proof.

| Writing task | Prompt fixture | Recorded local output |
|---|---|---|
| Introduction opening for contact-rich insertion | [writing_intro_opening_rich.md](tests/prompts/writing_intro_opening_rich.md) | [writing_intro_opening_rich_078d53e.md](tests/outputs/model_runs/writing/writing_intro_opening_rich_078d53e.md) |
| Methods overview from method notes | [writing_methods_overview_rich.md](tests/prompts/writing_methods_overview_rich.md) | [writing_methods_overview_rich_078d53e.md](tests/outputs/model_runs/writing/writing_methods_overview_rich_078d53e.md) |
| Results paragraph from diagnostic axes | [writing_results_with_diagnostic_axes.md](tests/prompts/writing_results_with_diagnostic_axes.md) | [writing_results_with_diagnostic_axes_078d53e.md](tests/outputs/model_runs/writing/writing_results_with_diagnostic_axes_078d53e.md) |
| Ablation paragraph from failure modes | [writing_ablation_with_failure_modes.md](tests/prompts/writing_ablation_with_failure_modes.md) | [writing_ablation_with_failure_modes_078d53e.md](tests/outputs/model_runs/writing/writing_ablation_with_failure_modes_078d53e.md) |
| Related Work positioning with placeholders | [writing_related_work_positioning_rich.md](tests/prompts/writing_related_work_positioning_rich.md) | [writing_related_work_positioning_rich_078d53e.md](tests/outputs/model_runs/writing/writing_related_work_positioning_rich_078d53e.md) |
| Chinese notes to English manuscript prose | [writing_zh_notes_to_en_manuscript_rich.md](tests/prompts/writing_zh_notes_to_en_manuscript_rich.md) | [writing_zh_notes_to_en_manuscript_rich_078d53e.md](tests/outputs/model_runs/writing/writing_zh_notes_to_en_manuscript_rich_078d53e.md) |
| Six-sentence Abstract from rich evidence | [writing_abstract_from_rich_evidence.md](tests/prompts/writing_abstract_from_rich_evidence.md) | [writing_abstract_from_rich_evidence_078d53e.md](tests/outputs/model_runs/writing/writing_abstract_from_rich_evidence_078d53e.md) |
| Bounded two-paragraph Conclusion | [writing_conclusion_bounded_takeaway_rich.md](tests/prompts/writing_conclusion_bounded_takeaway_rich.md) | [writing_conclusion_bounded_takeaway_rich_078d53e.md](tests/outputs/model_runs/writing/writing_conclusion_bounded_takeaway_rich_078d53e.md) |

Full provenance is recorded in
[tests/outputs/model_runs/writing/manifest_rich.json](tests/outputs/model_runs/writing/manifest_rich.json).
The local eval record is
[evals/results/078d53e_rich_writing_model_eval.jsonl](evals/results/078d53e_rich_writing_model_eval.jsonl).

**Hero candidates from recorded local Codex outputs**

```text
The largest improvement enters at the overlay self-verification stage: success
increases from 44% to 76%, a 32 percentage point gain, consistent with its role
in rejecting visually plausible but poorly grounded action hints before they
reach execution.
```

```text
The diagnostic pattern explains why the ranking is not simply a
camera-placement effect: overhead viewing tends to fail when the peg hides the
hole during final approach, side viewing improves lateral visibility but can
still leave depth uncertainty unresolved...
```

```text
This ordering is used because visual uncertainty that is left unresolved before
contact can propagate into the peg-hole interaction and become difficult to
correct once the peg begins entering the hole.
```

### Previous Behavior Evidence: Draft-First Writing Outputs

The outputs below are raw local Codex final answers generated from the same
draft-first writing prompt fixtures at base commit `ce1478f`. They are recorded
model-run artifacts, not illustrative examples and not polished golden
snapshots.

| Writing task | Prompt fixture | Recorded local output |
|---|---|---|
| Coach writing request with draft-first output | [coach_write_draft_first.md](tests/prompts/coach_write_draft_first.md) | [coach_write_draft_first_ce1478f.md](tests/outputs/model_runs/writing/coach_write_draft_first_ce1478f.md) |
| Ablation interpretation from component rows | [writing_ablation_interpretation.md](tests/prompts/writing_ablation_interpretation.md) | [writing_ablation_interpretation_ce1478f.md](tests/outputs/model_runs/writing/writing_ablation_interpretation_ce1478f.md) |
| Results paragraph from table-like evidence | [writing_results_interpretation.md](tests/prompts/writing_results_interpretation.md) | [writing_results_interpretation_ce1478f.md](tests/outputs/model_runs/writing/writing_results_interpretation_ce1478f.md) |
| Methods reader path from module notes | [writing_methods_reader_path.md](tests/prompts/writing_methods_reader_path.md) | [writing_methods_reader_path_ce1478f.md](tests/outputs/model_runs/writing/writing_methods_reader_path_ce1478f.md) |
| Two-paragraph Conclusion from results and limits | [writing_conclusion_two_paragraph.md](tests/prompts/writing_conclusion_two_paragraph.md) | [writing_conclusion_two_paragraph_ce1478f.md](tests/outputs/model_runs/writing/writing_conclusion_two_paragraph_ce1478f.md) |
| Minimal abstract smoke/provenance check | [writing_min.md](tests/prompts/writing_min.md) | [writing_min_ce1478f.md](tests/outputs/model_runs/writing/writing_min_ce1478f.md) |

Full provenance is recorded in
[tests/outputs/model_runs/writing/manifest.json](tests/outputs/model_runs/writing/manifest.json).
The local eval record is
[evals/results/ce1478f_writing_model_eval.jsonl](evals/results/ce1478f_writing_model_eval.jsonl).
These outputs are local single-run evidence, not CI-controlled behavior proof
or top-tier-ready proof.

**Golden expected excerpt: Methods reader path**

```text
The execution path begins with overhead and side RGB-D observations, which are
used to estimate the insertion pose and an associated confidence score. When
the confidence score is low, the system requests an additional view before
continuing the insertion attempt. The guarded insertion controller then
executes the motion while monitoring force and pose deviation...
```

**Golden expected excerpt: Ablation interpretation**

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
