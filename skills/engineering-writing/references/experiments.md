# Experiments and Results

Use this for English Experiments, Results, ablations, and failure analysis.

## Core Rule

Experiments prove the contribution. They are not table narration.

## Section Opening

State two to four evaluation questions:

- Q1: Does the method outperform relevant baselines?
- Q2: Which task/object/condition axis explains the gains?
- Q3: Which component supports which contribution?
- Q4: Where does the method fail or degrade?

If questions are not explicit, the section should still make them obvious.

## Setup

Setup should establish fairness, not consume the section.

Keep:

- platform or dataset
- shared protocol
- task/object split
- baseline fairness
- where detailed parameters live

Move parameter lists to tables or supplementary material when possible.

## Baselines

Define baselines before interpreting them:

```text
All methods share [common protocol]. [Baseline] differs only in [policy/model],
which tests [specific hypothesis].
```

Do not criticize a baseline before defining it.

## Metrics

Only include metrics used by claims. For each metric, define:

- what it measures
- direction of improvement
- success/failure criterion
- relation to contribution

## Main Results

Use:

```text
data -> interpretation -> bounded conclusion
```

Recommended paragraph sequence:

1. Overall result: ranking, strongest number, cost/time if relevant.
2. Axis 1: category or condition where the mechanism matters.
3. Axis 2: second category or diagnostic axis.
4. Hardest regime and remaining failures.

Avoid:

- pooled average only when categories explain the result
- prose that reads every table cell
- mechanism stories without evidence
- over-causal verbs when the mechanism is not directly measured

## Ablation

Each ablation paragraph should answer:

```text
What is removed?
Which metric changes most?
Which contribution does this support?
What boundary remains?
```

If the ablation only lists components, rewrite it around contribution support.

## Stress Tests and Sensitivity

Use stress tests to define boundaries, not to overstate robustness.

Safe phrasing:

```text
The stress test indicates reduced sensitivity within [tested range], but it does
not establish invariance to [untested condition].
```

## Failure Analysis

Place failure analysis in Results/Experiments or Discussion, not only in
Conclusion.

State:

- hardest regime
- why it is hard
- remaining failure types
- whether the result defines an operating envelope

## Minimum Experiments Card

| Block | Job | Must include | Must avoid |
|---|---|---|---|
| Setup | fairness and scope | platform, protocol, task split | parameter dump |
| Baselines | comparison meaning | what differs | unsupported criticism |
| Main results | contribution evidence | overall + axes | table narration |
| Ablation | mechanism evidence | removed part + metric + role | module list |
| Failure | boundary | hardest regime + failure types | hidden limitations |
