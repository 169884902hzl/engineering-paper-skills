# Introduction Opening Rich Prompt

Use $engineering-writing to draft the opening two paragraphs of an Introduction.

This is a showcase-grade WRITE request. Produce manuscript prose first. Do not
output a plan before the draft. Write in the style of a robotics / engineering
conference paper.

Target section:
Introduction opening, two paragraphs.

Task:
Contact-rich robotic insertion under partial visual occlusion.

Problem:
During insertion, the peg and hole may remain partially visible at the start,
but the alignment cue becomes unreliable as the robot approaches contact. A
fixed camera can lose task-relevant visibility, while open-loop execution
continues from an uncertain pose estimate.

Why existing routes are insufficient:

- Fixed overhead and fixed side RGB-D cameras improve coverage but cannot
  actively recover task-relevant visibility once the insertion geometry changes.
- Open-loop insertion is efficient but cannot react to pose uncertainty or
  contact deviation after contact begins.
- Force-guarded controllers can stop unsafe insertion but do not resolve the
  upstream perception ambiguity.

Method motivation:
A confidence-triggered multi-view insertion system estimates insertion pose and
confidence from overhead/side RGB-D observations, requests an additional view
when confidence is low, and uses a guarded insertion controller with force and
pose-deviation stops.

Evidence available:
84% success over 180 trials.
Baselines: fixed overhead 69%, fixed side 72%, open-loop 61%.

Boundary:
One 7-DoF arm, one tabletop fixture, one cylindrical peg family, no confidence
interval, no statistical significance test, no cross-robot or deployment test.

Requirements:

- Paragraph 1: task difficulty -> core bottleneck.
- Paragraph 2: existing-route gap -> method motivation.
- Do not list modules.
- Do not claim broad robustness, deployment readiness, novelty proof, or
  statistical significance.
- Avoid generic openings such as "X remains difficult" unless the sentence
  names the concrete failure mode.
