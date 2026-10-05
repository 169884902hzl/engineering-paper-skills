# Experiment Plan Pre-mortem

Use this when an experiment plan, a proposal, or a results-table skeleton
exists but the experiments are not finished. It runs the reviewer objections
in [reviewer-attack-patterns.md](reviewer-attack-patterns.md) against the plan
while a missing control still costs one more condition instead of a rebuttal.
The objections reviewers raise most often (handicapped baseline, unmeasured
internal component, missing time or cost, unstated operating assumption) are
cheap to fix at this stage and expensive or impossible after the setup is
taken down. P7 and P9 concern layout and are checked after writing.

## Inputs

- The claim or claims the experiments must support, one sentence each.
- Planned method and baselines, with what each one has: capability, prior or
  pretrained model, training data, tuning effort, compute.
- Conditions: scenes, objects, disturbances, difficulty levels, and which of
  them are meant to test generalization.
- Metrics, with how each is computed and from which logged signal.
- Planned trial counts per cell and what one trial is.
- Hardware and compute budget, including setup time per trial.

If an input is missing, list it under `Needs author input`; do not invent
baselines, conditions, or budgets.

## Procedure

1. Map claims to comparisons. For each claim, write the comparison that would
   support it and say whether the claim is system-level or mechanism-level
   (see P1). A claim with no comparison in the plan goes to "Claims to drop or
   narrow now" unless a cell is added for it.
2. P1. For every mechanism-level claim, plan a matched control: the same
   capability or prior without the proposed mechanism (the same pretrained
   model used directly, or the baseline with the simplest form of the
   capability). Give learned baselines a defensible data and tuning budget,
   or write down now why it is limited, so the paper can state it.
3. P2. List the operating assumptions the method needs (a visible target, a
   reachable pose, a valid intermediate estimate). For each, plan to log how
   often it holds, how a violation is detected, and what the system does
   then. Include trials where an assumption is expected to fail, or narrow
   the claim to the envelope that is tested.
4. P3. List the internal components the method relies on (verifier, mask,
   estimator, confidence score). Plan an independent measurement of each
   against ground truth: accuracy, false accept and false reject rates, and
   how often it changes the outcome for better and for worse.
5. P4. Plan to log wall-clock time, model calls or iterations, and hardware or
   compute cost per action for every method, not only the proposed one.
   Decide now whether to test the simplest alternative configuration (fewer
   sensors, one call instead of a loop, a better-placed fixed sensor). If it
   will not be tested, write down the number that argues it is insufficient.
6. P5. Write every decision rule as inputs, rule, output before running:
   thresholds, weights, selection rules, stopping criteria. Mark heuristics,
   freeze their values, and record how they were chosen. A threshold tuned on
   the evaluation trials makes the result optimistic.
7. P6. If calibration error or timing between subsystems can change the
   outcome, plan to measure it: calibration residuals at the start of each
   session, per-subsystem latency, and the delay between subsystems.
8. P8. Design results per category (object, condition, difficulty, failure
   type), not only pooled means. Fix the categories before running so they
   are not chosen after seeing which ones look good. Balance trials across
   categories, or plan to report n per category.
9. Choose trial counts and held-out conditions (sections below).
10. Fix the logging schema (section below) and do one dry run that fills every
    field before the first counted trial.

## Choosing Trial Counts

Choose n from three things, not from the table layout:

- The evaluation unit: what is actually independent. Repeated trials on the
  same object and start pose are not independent evidence for a claim about
  objects; count objects or scenes. For learned methods, training seeds are a
  separate unit from evaluation episodes: many episodes from one trained model
  say nothing about variation across training runs.
- Expected variability: run a short pilot and look at the spread across units.
- The uncertainty the claim needs: decide how wide an interval the claim can
  tolerate before choosing n.

For a single success rate counted over n independent trials (k successes out
of n), only multiples of 100/n percent are possible: 10 trials give 10-point
steps and 20 trials give 5-point steps, so 87% from one cell of 10 trials is
an error. Averages over seeds, objects, or conditions, and metrics that are
not success counts, do not follow this rule; say how a reported value was
aggregated.

95% Wilson score intervals for a single success rate:

| n | Observed | 95% Wilson interval |
|---|---|---|
| 10 | 5/10 (50%) | 23.7-76.3% |
| 10 | 8/10 (80%) | 49.0-94.3% |
| 10 | 9/10 (90%) | 59.6-98.2% |
| 10 | 10/10 (100%) | 72.2-100% |
| 20 | 10/20 (50%) | 29.9-70.1% |
| 20 | 16/20 (80%) | 58.4-91.9% |
| 20 | 18/20 (90%) | 69.9-97.2% |
| 20 | 20/20 (100%) | 83.9-100% |
| 50 | 45/50 (90%) | 78.6-95.7% |

These intervals describe one proportion. Ten successes in ten trials still
leave the true rate plausibly as low as about 72%. For a claim that method A
beats method B, plan the comparison test before running: run both methods on
the same initial conditions, use a paired test (for example an exact McNemar
test on matched success and failure), and check with the pilot spread whether
n can resolve the expected difference. Comparing the two intervals by eye is
not that test; overlapping intervals do not show that the methods are equal.

## Held-out Conditions

A generalization claim needs conditions (objects, scenes, disturbances) that
are chosen before running and never used to design the method or tune a
threshold (P5). Write the held-out list down with the plan. If nothing is held
out, narrow the claim to the conditions tested.

## What To Log

Log during the experiments so the writing stage has evidence rather than
recollection:

- Every failure, with the stage where it occurred and a suspected cause,
  marked as suspected until checked. Keep failed trials; do not rerun them
  away.
- Time per action and per trial, and calls or iterations per action (P4).
- Each operating-assumption violation: when, how it was detected, and what the
  system did (P2).
- Internal component outputs next to ground truth where available (P3).
- Calibration residuals and subsystem timestamps when they matter (P6).
- Seeds, configuration files, code version, and hardware per trial, so every
  number in a table can be traced to its runs.
- Every deviation from the plan (a changed threshold, a dropped condition),
  with the date and the reason.

## Output Shape

```text
Experiment plan pre-mortem
| Claim | Comparison | Matched control | Metric | n | Logged fields | Pattern addressed |

Cheapest additions, ranked:
1. [addition] - [objection it prevents] - [cost: trials, hours, hardware]

Claims to drop or narrow now:
- [claim] - [why the plan cannot support it] - [narrower wording, or the cell to add]

Not triggered: [pattern ids]
Needs author input: [facts the plan does not state]
```

In "Pattern addressed", use the ids from
[reviewer-attack-patterns.md](reviewer-attack-patterns.md); write `n` or
`held-out` for rows about trial counts or generalization. Rank additions by
the objection they prevent per unit of cost. A matched control or a logged
field usually costs less than a new baseline; prefer one matched control over
several weak baselines.
