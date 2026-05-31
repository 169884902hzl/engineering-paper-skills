# Introduction

Use this for English Introduction drafting and revision.

## Core Rule

Introduction establishes positioning. It should not become Methods, setup, or a
long related-work taxonomy.

## Seven-Block Structure

### Block 1: Task Context

Job: define the task and why feedback, reliability, or capability matters.

Do not start by attacking baselines or describing your system.

### Block 2: Central Challenge

Job: make the failure mode concrete.

Use a chain:

```text
[Method family] is useful because [role]. However, it depends on [assumption].
In [setting], [failure] breaks [loop/measurement/decision].
```

### Block 3: Classical Routes and Their Shared Gap

Job: explain why dominant configurations or standard formulations fail under
the challenge.

Do not write a citation list. Group by technical behavior and limitation.

### Block 4: Partial Repair Routes

Job: show what related directions improve and why each still misses the target
setting.

Each route should follow:

```text
[Route] improves [partial issue], but [specific remaining gap].
```

### Block 5: Second Gap

Job: introduce the additional gap that motivates the paper's formulation:
signal, supervision, data, calibration, deployment, speed, or evaluation.

Do not jump to experiments here.

### Block 6: Formulation Bridge

Job: convert the gaps into this paper's formulation.

Use:

```text
These gaps motivate [formulation/system], in which [role/change] enables
[capability] under [boundary].
```

### Block 7: Contributions

Use concrete, testable verbs:

- `We propose ...`
- `We formulate ...`
- `We validate ...`

Each contribution must map to a Methods block and an Experiments/Results block.

## Introduction Failure Modes

- broad opening with no task
- gap paragraph contains formulas or setup details
- related work routes are mixed in one paragraph
- method introduced before the gap is established
- contribution list uses adjectives instead of claims
- result numbers appear before the reader knows what is being tested

## Check

Ask:

1. Does the first paragraph define the task?
2. Are the gaps split into layers rather than compressed into one vague claim?
3. Does the formulation sentence come after the gap is clear?
4. Can every contribution be traced to later evidence?
