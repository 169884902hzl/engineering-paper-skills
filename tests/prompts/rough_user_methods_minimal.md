# Rough User Methods Minimal Prompt

Use $engineering-writing to make a Methods overview paragraph from these notes.

overhead rgbd + side rgbd. We estimate insertion pose and confidence. If low
confidence, ask for one more view and update pose. Then guarded controller
does insertion. Stops on force or pose deviation. We did not provide formulas,
threshold values, latency, calibration, or pseudocode. Main point is the path
from visual evidence to pose then to guarded execution.
