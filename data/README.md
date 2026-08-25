# 数据模板

这些 CSV 是公开的空白模板；真实成绩和私人题目记录建议复制到 `private/` 或 `data/private-*.csv`。

| 文件 | 用途 |
| --- | --- |
| `progress.csv` | 节点掌握等级与复测日期 |
| `problems.csv` | 题号、母题、用时、错因与修复 |
| `errors.csv` | 重复错误和迁移验证 |
| `models.csv` | 物理对象、模型、参数、假设与验证 |
| `formula_reviews.csv` | 规则卡主动提取结果 |
| `experiments.csv` | 理论—软件—实验对比 |
| `design_cases.csv` | 校正/PID/数字控制综合设计记录 |

日期建议使用 ISO `YYYY-MM-DD`；多个节点用 `/` 分隔；错误标签使用项目定义的 `MOD/ALG/SIG/CON/FREQ/DYN/DES/NUM/EXP`。
