# Experiments Table Narration

## Before

```text
Table II shows that the full method reaches 86%, the fixed camera baseline
reaches 71%, and the version without guarded execution reaches 74%.
```

## Problem

The paragraph reads table cells aloud. It does not state the evaluation question,
the ablation role, or the boundary of the result.

## After

```text
The experiment evaluates whether active observation and guarded execution
improve insertion success under the stated real-trial protocol. The full system
achieves 86% success over 120 trials, compared with 71% for the fixed-camera
baseline. Removing guarded execution reduces success to 74%, supporting the
role of the guarded stage under this protocol. These results do not establish
performance outside the tested visibility and task conditions.
```

## Skill Behavior

- Use `engineering-writing`.
- Convert rows into Q1/Q2 evidence.
- Avoid broader robustness or causality claims.
