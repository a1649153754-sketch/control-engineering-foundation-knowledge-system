#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DIST = ROOT / "dist"

ORDER = [
    "00-overview.md",
    "01-introduction.md",
    "02-dynamic-models.md",
    "03-time-response.md",
    "04-frequency-response.md",
    "05-stability.md",
    "06-error-analysis.md",
    "07-design-compensation.md",
    "08-root-locus.md",
    "09-nonlinear.md",
    "10-digital-control.md",
    "11-labview.md",
    "12-method-library.md",
    "13-checklists.md",
    "14-formula-cards.md",
    "25-formula-atlas.md",
    "15-problem-archetypes.md",
    "16-decision-trees.md",
    "17-counterexamples.md",
    "18-exercise-index.md",
    "26-exercise-supplements.md",
    "exercises/index.md",
    "exercises/01-introduction.md",
    "exercises/02-dynamic-models.md",
    "exercises/03-time-response.md",
    "exercises/04-frequency-response.md",
    "exercises/05-stability.md",
    "exercises/06-error-analysis.md",
    "exercises/07-design-compensation.md",
    "exercises/08-root-locus.md",
    "exercises/09-nonlinear.md",
    "exercises/10-digital-control.md",
    "19-experiments-matlab.md",
    "20-review-templates.md",
    "21-project-maintenance.md",
    "22-source-map.md",
    "23-appendices.md",
    "24-personal-links.md",
]

version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
parts = []
for name in ORDER:
    path = DOCS / name
    if not path.exists():
        raise FileNotFoundError(f"Missing bundle source: {path}")
    parts.append(path.read_text(encoding="utf-8").strip())

DIST.mkdir(exist_ok=True)
out = DIST / f"控制工程基础知识体系_v{version}.md"
out.write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8", newline="\n")
print(f"Wrote {out.relative_to(ROOT)} ({out.stat().st_size:,} bytes, {len(ORDER)} source pages)")
