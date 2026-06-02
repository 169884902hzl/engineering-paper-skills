# Mixed Chinese-English Notes To Methods Prompt

Use $engineering-writing to draft one Methods overview paragraph.

Mixed notes:

- input: overhead RGB-D + wrist RGB-D
- 先估计 target pose and confidence，不是直接控制
- low confidence -> request side view
- new view updates target pose
- controller: guarded insertion, stop on force limit or pose deviation
- no formula for confidence; no latency; no calibration detail in notes
- paragraph should explain why this order exists: uncertainty before contact is
  cheaper to resolve than after contact

Write manuscript prose first. Do not translate sentence by sentence. Do not
invent formulas, thresholds, calibration, timing, or pseudocode.
