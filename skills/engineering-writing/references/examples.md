# Engineering Writing Examples

## Minimal Abstract

Input:

```text
Target section: Abstract
Problem: Contact-rich insertion is sensitive to pose error.
Method: A perception-guided policy with guarded execution.
Evidence: 92% success over 50 real-robot trials; removing guarded execution
drops success to 74%.
Boundary: One object family and one fixture geometry.
```

Expected behavior:

- Write concise English manuscript prose.
- State the task, method, evidence, and boundary.
- Do not add baselines, citations, object categories, datasets, or extra
  numbers.
- Include a claim-evidence map unless prose-only output was requested.

Possible output skeleton:

```text
One-sentence thesis
In contact-rich insertion, we address pose sensitivity by combining
perception-guided policy execution with a guarded stage, supported by 50
real-robot trials within one object family and fixture geometry.

Draft
[Five sentences: task failure, method, result, ablation, boundary.]

Claim-evidence map
| Claim | Evidence support | Boundary |
```

## Evidence-Thin Scaffold

Input:

```text
We have a better controller. Please write a strong Introduction.
```

Expected behavior:

- Do not write a confident final Introduction.
- Ask for problem, method, evidence, and boundary.
- Provide a scaffold with placeholders if useful.
- Mark unsupported claims explicitly.

Possible output skeleton:

```text
Unsupported or downgraded claims
| Requested claim | Status | Reason | Safe wording |
| "better controller" | Unsupported | no metric, task, or comparison | "candidate controller" |

Draft scaffold
Paragraph 1: task and failure mode [needs task evidence]
Paragraph 2: method idea [needs mechanism]
Paragraph 3: contribution [blocked until evidence exists]
```

## Section Routing

Input:

```text
Please rewrite this figure caption and say it proves robustness.
```

Expected behavior:

- Hand off to `engineering-figure-table`.
- Do not solve caption-only work inside this skill unless the user explicitly
  asks for combined section writing.

## Methods Module List Repair

Input:

```text
Methods notes:
- perception module detects target
- controller moves gripper
- safety module stops when confidence is low
```

Expected behavior:

- Do not write a directory-style Methods section.
- First build roles, inputs, outputs, loop order, gate, fallback, and boundary.
- Then draft a reader path.

Possible output skeleton:

```text
Methods reader path
| Block | Paragraph job | Source anchor | Missing input |
| Overview | Define closed-loop contract | module notes | sensor/state definition |
| Gate/fallback | Define low-confidence stop | safety note | threshold or trigger |
```

## Results Table Narration Repair

Input:

```text
Table: Full 92%, w/o guarded execution 74%, fixed camera baseline 68%.
Write Results.
```

Expected behavior:

- Define the evaluation question.
- Interpret the overall result and ablation role.
- Do not read each table cell mechanically.
- State the tested condition and boundary.

Possible output skeleton:

```text
Result paragraph plan
| Question | Evidence | Interpretation | Boundary |
| Does guarded execution matter? | Full 92%, w/o guarded execution 74% | guarded execution contributes to task success | tested table only |
```

## Source Notes To English Introduction

Input:

```text
Notes: target sometimes invisible; active observation helps; maybe because the
camera keeps the gripper and hole in view; success improves in our trials.
```

Expected behavior:

- Treat notes as source material.
- Separate facts from assumptions.
- Use English manuscript prose.
- Do not write the guessed mechanism as proven.

Possible output skeleton:

```text
Source-note triage
| Source item | Type | Can enter prose? | Handling |
| active observation helps | Fact if supported by trials | yes with evidence | tie to trial result |
| maybe because camera keeps view | Assumption | no as fact | mark as possible explanation |
```
