# Claim Strength

Use this to calibrate verbs and boundaries.

## Verb Ladder

From weaker to stronger:

- `is consistent with`
- `suggests`
- `indicates`
- `supports`
- `shows`
- `demonstrates`
- `confirms`

Default to weaker verbs unless the mechanism is directly measured.

## Strong Claim Triggers

Check these words:

- `robust`
- `generalizable`
- `guarantees`
- `fully`
- `eliminates`
- `proves`
- `confirms`
- `state-of-the-art`
- `training-free`
- `calibration-robust`

For each, ask what evidence defines the regime.

## Repair Patterns

Unsupported:

```text
These results prove that the method is robust to occlusion.
```

Bounded:

```text
These results indicate improved performance under the tested occlusion regimes.
```

Unsupported:

```text
The system requires no data.
```

Bounded:

```text
The system does not require task-specific training data in the reported
evaluation.
```
