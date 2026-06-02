# Chinese Notes To English Showcase V2 Rerun Prompt

Use $engineering-writing to draft a showcase-grade English manuscript paragraph
from Chinese notes.

Target section:
Results-oriented manuscript paragraph.

Paper type:
Robotics / engineering conference paper.

中文笔记:

- 我们做的是遮挡下的 peg-hole 插入，不是普通的视觉识别任务。
- 真正的问题是快接触的时候，孔会被 peg 挡住，固定相机看到的信息变少。
- overhead 相机一开始能看到整体，但最后阶段容易被遮挡。
- side 相机能看到横向关系，但深度还是不稳定。
- open-loop 会把早期的位姿误差直接带进接触。
- 我们的方法先用 overhead 和 side RGB-D 估计插入位姿和 confidence。
- 如果 confidence 低，就再请求一个视角，然后更新位姿。
- 最后用 force 和 pose deviation 的 guard 执行插入。
- 180 次真机实验，full system 是 84%，fixed overhead 是 69%，fixed side
  是 72%，open-loop 是 61%。
- 没有做显著性检验，也没有跨机器人、部署和工业场景测试。

Core bottleneck:
Do not translate sentence by sentence. Reconstruct the English paper argument
around visibility loss, pose update, guarded execution, and bounded Results
evidence.

Evidence:

- 84% success over 180 real-robot trials.
- Fixed overhead: 69%.
- Fixed side: 72%.
- Open-loop: 61%.
- Failure interpretation is present in the Chinese notes.

Boundary:

- One 7-DoF robot arm.
- One tabletop fixture.
- One cylindrical peg family.
- No statistical significance test.
- No cross-robot evaluation.
- No deployment or industrial evaluation.

Forbidden wording and claims:

- Do not translate sentence by sentence.
- Do not write `supplied failure modes`.
- Do not say `dominant failure source` unless a failure distribution is
  supplied.
- Use `central failure mode` or similarly bounded wording when the bottleneck
  needs a name.
- Do not invent citations.
- Do not invent additional baselines.
- Do not claim broad robustness.
- Do not claim deployment readiness.
- Do not claim statistical significance.

Style requirements:

- Produce manuscript prose first.
- Reconstruct a native English argument.
- Do not preserve Chinese sentence order.
- Use mechanism or failure-mode interpretation, not literal translation.
- Integrate boundary as scientific scope.
- The final output should sound like native English engineering manuscript
  prose, not audit prose.
