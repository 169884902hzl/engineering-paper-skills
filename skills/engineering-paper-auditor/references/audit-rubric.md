# Audit Rubric

Use this rubric for full manuscripts, sections, and paper-quality reviews.

## Severity

| Severity | Meaning | Example |
|---|---|---|
| Critical | Output would be false, fabricated, or misleading | claiming an experiment was run when it was not |
| High | Main paper logic or evidence chain fails | contribution has no Methods or Experiments anchor |
| Medium | Reader trust or clarity is damaged | Results narrates table cells without a takeaway |
| Low | Style or presentation issue | repeated transition or local wording problem |

## Audit Axes

| Axis | Pass condition | Fail symptom |
|---|---|---|
| Thesis | One sentence names task, gap, method, evidence, boundary | thesis is promotional or absent |
| Contribution-evidence | Every contribution has method and evidence anchors | contribution appears only in Abstract/Conclusion |
| Section responsibility | Each section has a distinct job | Introduction contains Methods details; Results repeats table |
| Sentence role | Every sentence has function, necessity, placement, connection, and evidence boundary | decorative, redundant, misplaced, or disconnected sentence |
| Methods reader path | Inputs, state, mechanism, gate, and execution order are clear | module directory or formula dump |
| Experiments proof | Q1/Q2/Q3 are answered with bounded evidence | table narration or missing ablation role |
| Visual accountability | Each figure/table has responsibility and must-not-claim boundary | caption claims invisible mechanism |
| Claim strength | verbs match evidence class | "proves", "fully robust", or "generalizes" without evidence |
| Terminology | method, metric, category names are stable | same object has multiple names |
| Validation status | readiness claims are backed by checks | dry read presented as READY |

## Repair Routing

| Finding type | Route |
|---|---|
| section architecture | `engineering-writing` |
| sentence-level clarity after stable logic | `engineering-polishing` |
| caption, table, figure role, visual consistency | `engineering-figure-table` |
| reviewer/advisor comment handling | `engineering-response` |
| build, references, final status, submission safety | `engineering-validation` |
