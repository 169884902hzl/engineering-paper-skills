# Chinese Notes To English Manuscript Rich Prompt

Use $engineering-writing to turn the following Chinese research notes into one
English manuscript paragraph.

This is a showcase-grade WRITE request. Do not translate sentence by sentence.
Extract the task, bottleneck, method, evidence, and boundary, then write native
English engineering-paper prose.

Target section:
Introduction-to-method bridge paragraph.

中文笔记：
任务是接触丰富的机器人插入。困难不是单纯看不清，而是接近接触以后，孔和 peg 的相对位姿线索会被遮挡或变得不可靠。固定相机有时能看到整体，但最后阶段可能看不到真正有用的对齐线索。开环插入快，但如果初始位姿有偏差，接触以后很难恢复。我们的方法用 overhead 和 side RGB-D 估计插入位姿和置信度；置信度低时请求额外视角；执行阶段用力阈值和位姿偏差阈值保护。实验是 180 次真实机器人试验，成功率 84%，fixed overhead 69%，fixed side 72%，open-loop 61%。边界是单机械臂、单 fixture、圆柱 peg family，没有显著性检验，没有跨机器人或部署实验。

Requirements:

- Final output must be English manuscript prose.
- Do not preserve Chinese phrasing.
- Avoid broad claims.
- Integrate the boundary as scientific scope, not as an apology.
