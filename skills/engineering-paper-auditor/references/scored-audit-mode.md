# Scored Audit Mode

Opt-in protocol for users who ask for scores, a review panel, or reviewer
simulation. The default audit output stays unscored; scored mode adds a
triage layer on top of the same findings.

## Calibration Boundary

- Bands are heuristic triage derived only from findings listed in this audit
  run. They are not acceptance predictions and are not calibrated against any
  venue decision data.
- Every band must be traceable to anchored findings; a band without findings
  is not allowed.
- Material that was not actually inspected is `CANNOT_DETERMINE`, not a low
  band.
- No weighted total is produced. A single weighted number reads like a venue
  prediction, which this suite does not make.

## Reviewer Lenses

Run each lens as an independent pass before synthesis.

| Lens | Reads for | Typical blockers |
|---|---|---|
| Method rigor | formulation, assumptions, notation, decision rules | undefined objects, hidden assumptions, mechanism claims without support |
| Experimental evidence | baselines, ablations, protocol, statistics | missing obvious baseline, single-setup generality claims, selective axes |
| Contribution and positioning | novelty framing, nearest neighbors, impact wording | incremental delta framed as a breakthrough, limitation claims about unverified prior work |

## Procedure

1. Each lens reads the manuscript independently and reports: a two-sentence
   summary, its top findings with anchors, and its open questions.
2. Synthesis marks consensus blockers: findings raised by two or more lenses.
3. Build the critical path: the top three repairs ordered by blocking power,
   each routed to the owning skill.
4. Assign per-lens bands using the anchors below.

## Band Anchors

- 5: no blockers found in this lens on the inspected material.
- 4: minor repairs found; none blocking.
- 3: at least one blocking finding with a known repair route.
- 2: multiple blocking findings, or one structural break in the argument.
- 1: the lens cannot treat the inspected material as sound.

## Output Block

```text
Scored audit (heuristic triage, not an acceptance prediction)
| Lens | Band (1-5) | Anchored findings |

Consensus blockers
- ...

Critical path
1. ...
2. ...
3. ...

Not inspected
- ...
```
