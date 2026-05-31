# Abstract

Use this for English abstract drafting and revision.

## Timing

Write the abstract last. It should reflect stable Methods, stable Experiments,
and stable boundaries.

## Five-Sentence Contract

### Sentence 1: Task and Failure Mode

Job: state the control, perception, learning, or engineering problem and the
specific failure mode.

Use:

```text
[Task] remains challenging under [condition], where [specific failure] disrupts
[loop/measurement/decision].
```

Avoid:

- generic field importance
- vague statements that a problem is common
- method details in the first sentence

### Sentence 2: Why Existing Routes Are Insufficient

Job: compress the main prior routes into a contrast.

Use:

```text
[Route A] addresses [partial issue] but [limitation], while [route B] [different
limitation].
```

Avoid:

- criticizing a baseline before defining it
- reviewing many papers
- introducing the proposed method too early

### Sentence 3: Method Core

Job: state the formulation or system change and only the key mechanisms.

Use:

```text
We introduce [method/formulation], which [mechanism 1] and [mechanism 2] to
[intended effect].
```

Avoid:

- listing every module
- claiming a mechanism that only appears in derivation
- replacing a concrete mechanism with adjectives

### Sentence 4: Evaluation and Boundary

Job: state platform, dataset, supervision/data regime, and evaluation boundary.

Use:

```text
We evaluate [method] on [platform/task/dataset] under [condition], using
[data/supervision boundary].
```

Avoid:

- full setup details
- new method explanation
- broad generalization not tested

### Sentence 5: Strongest Stable Evidence

Job: end with the main result, baseline comparison, and a cost or boundary when
needed.

Use:

```text
Across [setting], [method] achieves [result] compared with [baselines], with
[cost/boundary/remaining limitation].
```

Avoid:

- only `significantly improves`
- results without baseline context
- subset-only metrics presented as global headline

## Abstract Gate

Before finalizing, check:

- Does every promise have Methods support?
- Does every result have Experiment support?
- Is the strongest claim still true under the stated boundary?
- Are task, method, evidence, and boundary all present?
