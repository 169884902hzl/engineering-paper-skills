# Chinese Notes To Discussion Showcase Prompt

Use $engineering-writing to write an English Discussion paragraph from these
Chinese notes.

目标：
写 Discussion。重点解释结果边界和下一步，不要写成 Results 重复。

中文笔记：

- full system 84%，fixed overhead 69%，fixed side 72%，open-loop 61%，180 trials。
- 这个结果说明更新视角有帮助，但现在不能说已经 robust 或 deployment-ready。
- 失败主要在两个情况：所有视角都看不清，或者接触后 pose deviation 超过 guarded recovery。
- 只做了一个 7-DoF 机械臂、一个 fixture、一个圆柱 peg family。
- 没有显著性检验、跨机器人、工业部署。
- 未来应该先补充更多 fixture / peg family，然后做统计检验和更强 failure breakdown。

要求：
先输出英文 Discussion prose。不要逐句翻译。不要编造新结果或引用。
