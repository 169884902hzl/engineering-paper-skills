# Benchmark Robotics System Results Prompt

Use $engineering-writing to draft a manuscript Results paragraph first.

Paper type:
Robotics system paper.

Task:
Mobile manipulator retrieves small tools from cluttered workbench trays.

Method:
The system combines tray-level object proposal, wrist-camera verification, and
a guarded lift check before placing the object in a return bin.

Imperfect notes:

- table has three rows: full system 73% over 150 trials, proposal-only 52%,
  proposal plus wrist verification 64%
- failure modes: reflective tool handles confuse the proposal stage; thin tools
  sometimes pass verification but slip during lift
- only two tray layouts and six tool categories
- no significance test; no factory deployment; no multi-robot evaluation
- author wants the paragraph to explain why wrist verification helps but does
  not solve lift failures

Requirements:

- Write manuscript prose first.
- Include the boundary.
- Do not invent extra categories, sensors, thresholds, or statistics.
