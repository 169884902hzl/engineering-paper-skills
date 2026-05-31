# Section Boundaries

Use this when a paragraph feels misplaced or a section is drifting.

## Boundary Table

| Section | Main question | Should contain | Should not contain |
|---|---|---|---|
| Abstract | What is the problem, method, evidence, and boundary? | task, gap, method, result, boundary | derivation, long related work |
| Introduction | Why is this problem worth solving and what gap remains? | task, gap, positioning, formulation, contributions | formulas, setup details, result narration |
| Related Work | What prior axes exist and what combination remains uncovered? | taxonomy, nearest neighbor, distinction | paper-by-paper list |
| Methods | How does the system work? | reader path, core object, mechanism, execution, safety | baselines, result claims |
| Experiments | What evidence supports the contribution? | setup, baselines, metrics, results, ablation, failure | parameter dump, unsupported interpretation |
| Discussion | What does the evidence mean and where does it stop? | interpretation, relation to prior work, limitations | new results |
| Conclusion | What finally stands? | method, strongest evidence, boundary, future work | new claims, new terms |

## Diagnosis

Ask:

1. Is the sentence about gap, mechanism, evidence, or boundary?
2. If removed, what becomes missing: positioning, implementation, evidence, or
   closure?
3. Does the paragraph try to do more than one job?

Map missing function to section:

- positioning -> Introduction or Related Work
- implementation -> Methods
- evidence -> Experiments
- interpretation -> Discussion
- closure -> Conclusion

## Drift Symptoms

- Setup is longer than Results: Experiments is losing evidence focus.
- Methods overview is half a page: Methods is becoming a directory or background
  section.
- Introduction contains formulas, platform constants, or result numbers:
  positioning has drifted into Methods or Experiments.
- Related Work has many citations but no nearest-neighbor distinction:
  taxonomy has replaced positioning.
- Conclusion needs a third paragraph: earlier sections did not close their
  claims cleanly.
