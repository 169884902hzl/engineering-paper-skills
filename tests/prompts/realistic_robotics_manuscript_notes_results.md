# Realistic Robotics Manuscript Notes Results Prompt

Use $engineering-writing to draft manuscript Results prose first from these
de-identified author notes.

Author notes, copied from a lab notebook and cleaned only for privacy:

- task name keeps changing in draft: "active view insertion", "confidence view
  update", maybe call it confidence-triggered multi-view insertion for now
- result table draft has 3 baselines and ours:
  - ours: 84% / 180 trials
  - fixed overhead: 69%
  - fixed wrist-side camera: 72%
  - open-loop pose execution: 61%
- reviewer will ask why side camera is better than overhead even though
  overhead sees whole scene early. Explanation: overhead loses hole near final
  approach, side keeps lateral relationship but depth is still uncertain.
- failures still happen when all views are ambiguous or when the peg shifts the
  pose after contact starts
- not sure whether to call this robust. Probably do not. No confidence
  intervals or significance yet.
- de-identified: one robot arm, one fixture, one peg family. Do not mention
  private project name.

Please write the Results paragraph first, then a short missing-evidence note if
needed.
