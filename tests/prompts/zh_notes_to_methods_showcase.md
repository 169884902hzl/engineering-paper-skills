# Chinese Notes To Methods Showcase Prompt

Use $engineering-writing to write an English Methods paragraph from these
Chinese notes.

目标：
写 Methods，不是 Results，也不是逐句翻译。

中文笔记：

- 我们的系统先不要急着执行插入，先判断视觉给的 pose 够不够可信。
- 输入有 overhead RGB-D、side RGB-D、候选 insertion pose 和 confidence。
- 中间量是 refined insertion pose + confidence，不是直接输出动作。
- 如果 confidence 低，再请求一个视角，更新 pose。
- 执行阶段是 guarded insertion，监测 force 和 pose deviation。
- 没有给公式、阈值、延迟、标定细节。

要求：
先输出英文论文 Methods prose。不要增加阈值、公式、延迟或实验结论。
