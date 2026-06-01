# Paper-Level Narrative Map

Use this for full sections, multi-section rewrites, abstracts, introductions,
and conclusions. The map prevents fluent prose from hiding a broken story.

## Map

```text
Paper narrative map
| Story node | Manuscript location | Sentence/paragraph anchor | Evidence anchor | Reader question answered | Boundary |
```

## Required Checks

- The Abstract must not claim more than the Methods/Experiments can support.
- The Introduction must make the Methods necessary.
- The Methods must provide the mechanism needed to interpret Experiments.
- The Experiments must test each contribution, not just report performance.
- The Discussion must explain evidence meaning without adding new proof.
- The Conclusion must only restate what the paper has already supported.

## Failure Signs

| Symptom | Repair |
|---|---|
| contribution appears first in Abstract and last in Conclusion only | add Methods and Experiments anchors or downgrade |
| Introduction gap is not linked to a nearest-neighbor route | rebuild Related Work or positioning |
| Methods are a list of modules | introduce the state, signal, or mechanism connecting modules |
| Results table has no evaluation question | add question and bounded interpretation |
| Conclusion adds future capability | convert to limitation-derived future work |
