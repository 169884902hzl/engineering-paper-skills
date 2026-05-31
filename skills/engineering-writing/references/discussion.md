# Discussion

Use this for English Discussion, implications, and limitations.

## Job

Discussion explains what the evidence means and where it stops. It should not
repeat Results figure by figure.

## Structure

Use:

```text
central advance -> evidence meaning -> relation to prior work -> constraints ->
future use
```

## Paragraph Types

- Interpretation: what the main result changes about the problem.
- Comparison: how the result relates to prior assumptions or methods.
- Limitation: which assumptions, regimes, datasets, or platforms remain
  untested.
- Implication: what the method enables within the proven boundary.

## Limitations

Limitations must be anchored in the paper:

- observed failure regime
- untested condition
- method assumption
- platform or dataset boundary
- metric limitation

Avoid adding generic limitations that do not follow from the paper.

## Do Not

- introduce new experimental results
- introduce new method components
- repeat the introduction
- write future work that is unrelated to the shown limitation

## Section Boundary Table

| Content | Results | Discussion | Conclusion |
|---|---|---|---|
| Measured numbers | primary location | only interpret or connect | only summarize strongest evidence |
| Mechanism interpretation | only if directly supported | explain bounded meaning | do not introduce new mechanism |
| Limitation | state if tied to result | explain why it matters | summarize boundary and future work |
| Future work | avoid unless needed for boundary | optional if tied to limitation | brief, directly based on boundary |

If Discussion starts repeating table cells, move the content back to Results. If
it introduces new claims, downgrade or remove them.
