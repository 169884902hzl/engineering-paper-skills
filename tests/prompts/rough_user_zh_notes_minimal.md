# Rough User Chinese Notes Minimal Prompt

Use $engineering-writing to write an English manuscript paragraph from these
rough Chinese notes.

笔记：

- peg-hole 插入，遮挡是主要麻烦，尤其快接触的时候孔被 peg 挡住
- overhead 一开始好，后面容易看不到孔
- side 能看横向，但深度不稳
- open-loop 早期位姿错了就直接带进接触
- 我们用 overhead + side RGB-D 估计 pose/confidence；低 confidence 再看一次，然后更新 pose
- guarded insertion 有 force 和 pose deviation stop
- 结果：full 84%，overhead 69%，side 72%，open-loop 61%，180 trials
- 边界：一个 7-DoF arm，一个 fixture，一个圆柱 peg family；没有显著性、跨机器人、部署

不要逐句翻译。先给英文论文段落。
