# Redactions

Content derived from an unpublished manuscript was redacted on 2026-10-05.

Each redacted span was replaced with the literal marker
`[redacted: unpublished source data]`. All other text in these files is the
original recorded output, kept verbatim. The outputs were not re-run.

Recorded outputs in `tests/outputs/model_runs/writing/`:

- `writing_ablation_interpretation_ce1478f.md`
- `writing_conclusion_two_paragraph_ce1478f.md`
- `writing_ablation_with_failure_modes_078d53e.md`
- `writing_ablation_showcase_v2_ad6d5b4.md`
- `stability_ablation_run1_e99ca81.md`
- `stability_ablation_run2_e99ca81.md`
- `stability_ablation_run3_e99ca81.md`
- `full_section_results_demo_e99ca81.md`
- `full_section_results_demo_v2_8865acf.md`

Eval records in `evals/results/`:

- `078d53e_rich_writing_model_eval.jsonl` (inline `model_output` for
  `writing_ablation_with_failure_modes`)
- `ce1478f_writing_model_eval.jsonl` (review notes for
  `writing_ablation_interpretation` and `writing_conclusion_two_paragraph`)
- `ad6d5b4_showcase_v2_human_review.md` (quoted sentence for
  `writing_ablation_showcase_v2`)

Notes:

- The `sha256` and `output_sha256` values in the writing manifests and eval
  records were left unchanged. They describe the outputs as originally
  recorded and do not match the redacted files.
- These outputs were generated from the prompt fixtures as they existed at the
  recorded base commits. The matching prompt fixtures
  (`writing_ablation_interpretation.md`, `writing_ablation_showcase_v2.md`,
  `writing_ablation_with_failure_modes.md`,
  `writing_conclusion_two_paragraph.md`, `full_section_results_demo.md`,
  `full_section_results_demo_v2.md`) were replaced afterwards with an invented
  scenario, so the current prompt files no longer correspond to these
  recordings. In `related_work_verified_citation_mode.md` one synthetic
  snippet was reworded; its recorded output needed no redaction.
