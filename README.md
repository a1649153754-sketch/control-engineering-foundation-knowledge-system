# 控制工程基础知识体系

> 基于《控制工程基础（第4版）》与配套《控制工程基础习题解（第4版）》整理的可持续知识库：保留教材章节、术语和分析主线，同时加入稳定编号、LaTeX 公式、193 道逐题解析、母题、边界卡、决策树、实验与复盘系统。

<p align="center">
  <img src="docs/assets/images/social-preview.svg" alt="控制工程基础知识体系封面" width="900">
</p>

## 当前版本

**v1.1.0 · 2026-08-25**

| 模块 | 当前规模 |
| --- | ---: |
| 教材章节 | 11 |
| 稳定知识节点 | 77 |
| 三级检查项 | 385 |
| 核心规则与公式卡 | 231 |
| LaTeX 显示公式图鉴 | 1 套 |
| 配套习题逐题解析 | 193 / 193 |
| 典型母题 | 78 |
| 错误命题与边界卡 | 44 |
| 任务决策树 | 16 |
| 实验 / MATLAB / LabVIEW 任务 | 20 |
| 个人高频疑问挂接 | 12 |

## v1.1.0 完善内容

- **真正启用公式渲染**：加入 MathJax 配置与加载脚本，修复只有 Arithmatex、没有浏览器渲染器而显示原始公式的问题。
- **独立公式图鉴**：把高频关系从宽表格抽出，使用 `\[...\]` 显示公式；移动端长公式可横向滚动。
- **193 道逐题解析**：覆盖习题解第 1—10 章全部题目，每题均有题意摘要、节点、母题、来源页、解析路线、关键公式、结果校验和易错点。
- **由题反哺知识库**：每题增加“由本题补入知识库”，并把跨题结论汇总为补充库。
- **机器可维护**：增加 `data/exercise_catalog.json`、逐题进度 CSV 与覆盖校验，防止以后漏题或重复编号。

## 项目特点

- **忠于教材结构**：`C1—C11` 与教材 11 章、77 个小节对应。
- **教材—题解双索引**：记录原书印刷页、PDF 页和题号。
- **条件优先**：公式同时记录触发信号、主路线、复核方式和失效边界。
- **逐题闭环**：`C` 节点 → `Q` 母题 → `EX` 逐题解析 → 错误标签 → 复测。
- **跨域连接**：统一时域、频域、稳定性、误差、校正与根轨迹。
- **软件与实验**：内置 MATLAB/LabVIEW 任务、数值可信性检查和实验报告模板。
- **可持续维护**：固定 ID、自动校验、单文件打包和 GitHub Pages 部署。

## 快速阅读

- [在线知识库](https://a1649153754-sketch.github.io/control-engineering-foundation-knowledge-system/)
- [体系总览](docs/00-overview.md)
- [习题解逐题解析](docs/exercises/index.md)
- [教材—习题解逐题索引](docs/18-exercise-index.md)
- [LaTeX 公式图鉴](docs/25-formula-atlas.md)
- [规则与公式卡](docs/14-formula-cards.md)
- [习题反哺补充库](docs/26-exercise-supplements.md)
- [动态数学模型](docs/02-dynamic-models.md)
- [时域瞬态响应](docs/03-time-response.md)
- [频率特性](docs/04-frequency-response.md)
- [稳定性分析](docs/05-stability.md)
- [误差分析](docs/06-error-analysis.md)
- [综合与校正](docs/07-design-compensation.md)
- [根轨迹法](docs/08-root-locus.md)
- [非线性问题](docs/09-nonlinear.md)
- [计算机控制系统](docs/10-digital-control.md)

## 在线网站与单文件版

- GitHub Pages：[https://a1649153754-sketch.github.io/control-engineering-foundation-knowledge-system/](https://a1649153754-sketch.github.io/control-engineering-foundation-knowledge-system/)
- 单文件 Markdown：[dist/控制工程基础知识体系_v1.1.0.md](dist/控制工程基础知识体系_v1.1.0.md)
- 部署后下载：[控制工程基础知识体系 v1.1.0](https://a1649153754-sketch.github.io/control-engineering-foundation-knowledge-system/downloads/控制工程基础知识体系_v1.1.0.md)

## 本地使用

需要 Python 3.11 或更高版本：

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
python scripts/validate_project.py
python scripts/build_bundle.py
zensical serve
```

浏览器打开 `http://127.0.0.1:8000`。静态构建：

```bash
zensical build --clean
```

## 推荐学习闭环

1. 读章节节点，先完成 `a/b` 检查项。
2. 在公式图鉴中看清结构，再回规则卡核对条件。
3. 独立做题，先记录 `C / Q / EX` 编号与第一动作。
4. 只在断点处查逐题解析和原习题解。
5. 把错误标为 `MODEL / STRUCT / COND / ALG / INTERP / VERIFY`。
6. 3/7/14 天重做，并用另一判据、MATLAB 或极限检查交叉验证。

## 仓库结构

```text
.
├─ docs/
│  ├─ exercises/             # 第1—10章共193道逐题解析
│  ├─ javascripts/mathjax.js # 公式渲染配置
│  ├─ 25-formula-atlas.md    # 独立显示公式
│  └─ 26-exercise-supplements.md
├─ data/
│  ├─ exercise_catalog.json  # 逐题机器可读目录
│  └─ exercise_progress.csv  # 逐题复测模板
├─ scripts/                  # 校验与单文件打包
├─ releases/                 # 版本说明
├─ .github/                  # Actions、Issue 与 PR 模板
├─ zensical.toml
├─ PROJECT_MANIFEST.json
├─ CHANGELOG.md
└─ ROADMAP.md
```

## 来源与版权边界

本仓库不包含两本来源 PDF、扫描页、整套题面或逐字答案。逐题页面发布的是原创题意概括、方法解析、知识映射和简短结果校验；具体图形、参数与完整题面请回到合法取得的原书核对。详见 [来源、页码与版本边界](docs/22-source-map.md)。

## 许可

- 原创知识体系、文字和表格：`CC BY-NC-SA 4.0`，见 `LICENSE`。
- 脚本、配置和工作流：`MIT`，见 `LICENSE-CODE`。
