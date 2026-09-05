# 数据与复测模板

公开CSV只保留表头；个人成绩建议存入 `private/`。

| 文件 | 用途 |
|---|---|
| `progress.csv` | 知识节点掌握度 |
| `problems.csv` | 自录题目与母题 |
| `errors.csv` | 重复错误与迁移验证 |
| `models.csv` | 物理模型与假设 |
| `formula_reviews.csv` | 公式主动提取 |
| `experiments.csv` | 理论—软件—实验对比 |
| `design_cases.csv` | 控制器设计案例 |
| `exercise_progress.csv` | 教材193题复测 |
| `tsinghua_822_progress.csv` | 清华真题190题目单元复测 |
| `key_problem_progress.csv` | 重点题40来源卡复测 |
| `exercise_catalog.json` | 教材题机器目录 |
| `tsinghua_822_exam_catalog.json` | 真题机器目录 |
| `key_problem_catalog.json` | 重点题机器目录与重复关系 |

错误标签建议：`MODEL/STRUCT/COND/ALG/INTERP/VERIFY/SOURCE`。`SOURCE` 专门记录扫描模糊、参数歧义或答案来源未经独立复核。
