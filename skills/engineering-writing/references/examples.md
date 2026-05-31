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
