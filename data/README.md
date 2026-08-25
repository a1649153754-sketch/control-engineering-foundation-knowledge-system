# 数据与复测模板

公开仓库中的 CSV 只保留表头；真实成绩和私人题目记录建议复制到 `private/` 或 `data/private-*.csv`。

| 文件 | 用途 |
| --- | --- |
| `progress.csv` | 知识节点掌握等级与复测日期 |
| `problems.csv` | 自录题目、母题、用时、错因与修复 |
| `errors.csv` | 重复错误和迁移验证 |
| `models.csv` | 物理对象、模型、参数、假设与验证 |
| `formula_reviews.csv` | 规则卡与公式主动提取结果 |
| `experiments.csv` | 理论—软件—实验对比 |
| `design_cases.csv` | 校正/PID/数字控制综合设计记录 |
| `exercise_progress.csv` | 193 道配套题的逐题完成与 3/7/14 天复测 |
| `exercise_catalog.json` | 193 道题的 ID、题号、章节、来源页、节点、母题和解析字段目录 |

## 逐题记录建议

`exercise_progress.csv` 的推荐流程：

1. `exercise_id` 填 `EX-Cx-yy`；
2. `error_tags` 使用 `MODEL/STRUCT/COND/ALG/INTERP/VERIFY`；
3. `breakpoint` 只写真正卡住的位置；
4. `repair` 写一个可执行动作，不写“下次认真”；
5. `review_3d/7d/14d` 记录脱离答案后的结果。

日期使用 ISO `YYYY-MM-DD`；多个节点用 `/` 分隔。`exercise_catalog.json` 是公开索引，不保存个人成绩。
