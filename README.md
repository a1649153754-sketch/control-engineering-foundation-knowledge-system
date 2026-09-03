# 控制工程基础知识体系

> 基于《控制工程基础（第4版）》、配套《习题解（第4版）》、1995—2024 清华大学 822 真题与重点题资料建立的可持续知识库。教材结构、逐题解析、真题迁移和模型思考在同一编号体系中联通。

<p align="center">
  <img src="docs/assets/images/social-preview.svg" alt="控制工程基础知识体系封面" width="900">
</p>

## 当前版本

**v1.2.0 · 2026-08-31**

| 模块 | 当前规模 |
| --- | ---: |
| 教材章节 / 稳定节点 | 11 / 77 |
| 三级检查项 | 385 |
| 核心规则与公式卡 | 231 |
| 配套习题逐题解析 | 193 / 193 |
| 清华 822 真题题目单元 | 190 / 190 |
| 重点题与讲义来源卡 | 40 / 40 |
| 来源挂接解析卡总数 | 423 |
| 典型母题 / 边界卡 / 决策树 | 78 / 44 / 16 |
| 实验 / MATLAB / LabVIEW 任务 | 20 |

## v1.2.0 新增

- **1995—2024 真题全量建卡**：30 年共 190 个题目单元；1998 年20道选择题逐项加入答案判断与条件说明。
- **重点题资料全量索引**：40 张来源卡，保留重复/幻灯变体关系，不把第三方答案冒充官方结论。
- **每题加入“我的思考”**：写第一动作、结构不变量、替代路线、核验方法和失效边界；明确这是模型补充而非官方答案。
- **2024 九题深度解析**：对电路、Routh、Nyquist、频域设计、扰动灵敏度、二阶最优和离散极点作完整独立推导。
- **重复题族地图**：把多年换皮题压缩成12个迁移家族。
- **章节反哺**：C1—C10 章节末尾自动挂接相关真题，不再让真题成为孤立年份文件。
- **机器目录与进度表**：新增真题、重点题 JSON 目录与两个复测 CSV，并强化覆盖校验。

## 四层学习结构

```text
教材节点 C / 规则 K / 母题 Q
        ↓
配套习题 EX（193题）
        ↓
清华真题 TH（190题目单元）
        ↓
重点题 KP（40来源卡）+ 我的迁移思考
```

## 快速入口

- [在线知识库](https://a1649153754-sketch.github.io/control-engineering-foundation-knowledge-system/)
- [清华 822 真题全量索引](docs/tsinghua-822/index.md)
- [2024 年九题深度解析](docs/tsinghua-822/2024-deep-solutions.md)
- [重点题与答案全量索引](docs/key-problems/index.md)
- [重复题族与迁移地图](docs/28-recurring-problem-families.md)
- [真题驱动的知识补充与我的思考](docs/27-tsinghua-822-insights.md)
- [配套习题 193 题解析](docs/exercises/index.md)
- [LaTeX 公式图鉴](docs/25-formula-atlas.md)
- [规则与公式卡](docs/14-formula-cards.md)
- [习题反哺补充库](docs/26-exercise-supplements.md)

## 本地使用

```bash
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/validate_project.py
python scripts/build_bundle.py
zensical serve
```

## 推荐闭环

1. 先读章节节点和公式边界。
2. 做教材题 `EX`，证明基础方法可复现。
3. 做真题 `TH`，先识别题族和第一动作。
4. 对照重点题 `KP`，只吸收能独立复算的结论。
5. 错误标为 `MODEL / STRUCT / COND / ALG / INTERP / VERIFY / SOURCE`。
6. 3/7/14 天复测；图形或小字参数不清时记录证据状态，不猜数字。

## 仓库结构

```text
.
├─ docs/
│  ├─ exercises/          # 教材习题193题
│  ├─ tsinghua-822/       # 1995—2024真题190题目单元
│  ├─ key-problems/       # 重点题/讲义40来源卡
│  ├─ 25-formula-atlas.md
│  ├─ 27-tsinghua-822-insights.md
│  └─ 28-recurring-problem-families.md
├─ data/
│  ├─ exercise_catalog.json
│  ├─ tsinghua_822_exam_catalog.json
│  ├─ key_problem_catalog.json
│  └─ *_progress.csv
├─ scripts/
├─ releases/
└─ zensical.toml
```

## 来源与版权边界

仓库不包含来源 PDF、扫描图、整套逐字题面或大段第三方答案。公开页面保存的是题目摘要、页码定位、原创推导路线、简短可复核结论和模型思考。真题 PDF 只含题面时，项目明确标注“非官方答案”；重点题资料为第三方整理，数值结论必须独立复算。详见 [来源与证据边界](docs/22-source-map.md)。

## 许可

- 原创知识体系、文字和表格：`CC BY-NC-SA 4.0`。
- 脚本、配置和工作流：`MIT`。
