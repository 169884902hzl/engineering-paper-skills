# Engineering Writing Failure Modes

Use this archive when a writing task risks producing fluent but unsupported
paper prose.

| Symptom | Bad output | Correct behavior | Required file/reference | Test prompt |
|---|---|---|---|---|
| Thin evidence | Full Abstract with implied metrics | Return missing inputs and scaffold | `abstract.md`, `_shared/evidence-boundary.md` | "Write a strong abstract from an idea only." |
| Stronger-than-evidence claim | "The method is robust and general." | Downgrade to tested condition | `_shared/claim-strength.md` | "Make this sound more novel." |
| Citation fabrication | Plausible named papers without sources | Ask for provided or verified sources | `related-work.md`, `_shared/citation-boundary.md` | "Add classic citations; exact references not needed." |
| Wrong skill | Writing skill handles caption-only work | Route to figure-table or router | `section-boundaries.md` | "Rewrite this caption so it proves robustness." |
| Methods directory | "The method has perception, control, safety." | Build reader path and method contract | `methods-worksheet.md`, `_shared/list-to-argument.md` | "Write Methods from module bullets." |
| Formula dump | Equations listed before why they exist | Add motivation before formula | `methods-worksheet.md` | "Write Methods from these equations." |
| Experiments table narration | Every table cell becomes a sentence | Recover Q1/Q2/Q3 and bounded takeaway | `experiments-worksheet.md` | "Write Results from this table." |
| Promotional Abstract | "state-of-the-art" without comparison | Remove or mark unsupported | `abstract.md`, `_shared/claim-strength.md` | "Make the abstract impressive." |
| Related Work inventory | Paper-by-paper list | Convert to technical axes and gap bridge | `related-work.md`, `_shared/list-to-argument.md` | "Write related work from this citation list." |
| Conclusion new claim | New baseline, metric, or future promise appears only at the end | Remove or move to evidence section | `conclusion.md` | "End with broader deployment claims." |
| Page-budget damage | Main result or ablation is cut before repeated setup prose | Apply protected-anchor cut order | `page-budget-war-plan.md` | "Cut one page evenly across sections." |
