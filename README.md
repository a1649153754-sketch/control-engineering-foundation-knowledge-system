# 控制工程基础知识体系

> 基于《控制工程基础（第4版）》与配套《控制工程基础习题解（第4版）》整理的可持续知识库：保留教材的章节、术语和分析主线，同时加入稳定编号、公式卡、母题、边界卡、决策树、实验与复盘系统。

<p align="center">
  <img src="docs/assets/images/social-preview.svg" alt="控制工程基础知识体系封面" width="900">
</p>

## 当前版本

**v1.0.0 · 2026-08-25**

| 模块 | 当前规模 |
| --- | ---: |
| 教材章节 | 11 |
| 稳定知识节点 | 77 |
| 三级检查项 | 385 |
| 核心规则与公式卡 | 231 |
| 典型母题 | 78 |
| 错误命题与边界卡 | 44 |
| 任务决策树 | 16 |
| 实验 / MATLAB / LabVIEW 任务 | 20 |
| 个人高频疑问挂接 | 12 |

## 项目特点

- **忠于教材结构**：`C1—C11` 与教材 11 章、77 个小节一一对应。
- **教材—题解双索引**：记录原书印刷页、PDF 页和配套题号范围。
- **条件优先**：公式同时记录触发信号、主路线、复核方式和失效边界。
- **题型驱动**：把配套题解抽象成 `Q` 母题，不复制题目和答案全文。
- **跨域连接**：统一时域、频域、稳定性、误差、校正与根轨迹。
- **软件与实验**：内置 MATLAB/LabVIEW 任务、数值可信性检查和实验报告模板。
- **可持续维护**：固定 ID、自动校验、单文件打包和 GitHub Pages 部署。

## 快速阅读

- [体系总览](docs/00-overview.md)
- [动态数学模型](docs/02-dynamic-models.md)
- [时域瞬态响应](docs/03-time-response.md)
- [频率特性](docs/04-frequency-response.md)
- [稳定性分析](docs/05-stability.md)
- [误差分析](docs/06-error-analysis.md)
- [综合与校正](docs/07-design-compensation.md)
- [根轨迹法](docs/08-root-locus.md)
- [非线性问题](docs/09-nonlinear.md)
- [计算机控制系统](docs/10-digital-control.md)
- [规则与公式卡](docs/14-formula-cards.md)
- [母题索引](docs/15-problem-archetypes.md)
- [来源与页码](docs/22-source-map.md)

## 在线网站与单文件版

- GitHub Pages：[https://a1649153754-sketch.github.io/control-engineering-foundation-knowledge-system/](https://a1649153754-sketch.github.io/control-engineering-foundation-knowledge-system/)
- 单文件 Markdown：[dist/控制工程基础知识体系_v1.0.0.md](dist/控制工程基础知识体系_v1.0.0.md)
- 部署后下载地址：[https://a1649153754-sketch.github.io/control-engineering-foundation-knowledge-system/downloads/控制工程基础知识体系_v1.0.0.md](https://a1649153754-sketch.github.io/control-engineering-foundation-knowledge-system/downloads/控制工程基础知识体系_v1.0.0.md)

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
2. 遮住规则卡结论，只看触发信号主动提取。
3. 做教材/配套题，记录 `Q` 母题与错误标签。
4. 把重复错误挂到 `B` 边界卡或 `J-C` 个人问题。
5. 3/7/14 天重做变式，并用 MATLAB、另一判据或实验交叉验证。

## 仓库结构

```text
.
├─ docs/                    # 章节正文、公式卡、母题、边界、实验与模板
├─ data/                    # 掌握度、题目、错题、模型、实验与设计空白表
├─ scripts/                 # 项目校验与单文件打包
├─ releases/                # 版本说明
├─ .github/                 # Actions、Issue 与 PR 模板
├─ zensical.toml            # 文档站配置
├─ PROJECT_MANIFEST.json
├─ CHANGELOG.md
└─ ROADMAP.md
```

## 来源与版权边界

本仓库不包含两本来源 PDF、扫描页、整套题目或逐题答案。项目发布的是原创总结、索引、公式条件说明和学习工具；具体符号、图形和题目细节请回到合法取得的原书核对。详见 [来源、页码与版本边界](docs/22-source-map.md)。

## 许可

- 原创知识体系、文字和表格：`CC BY-NC-SA 4.0`，见 `LICENSE`。
- 脚本、配置和工作流：`MIT`，见 `LICENSE-CODE`。
