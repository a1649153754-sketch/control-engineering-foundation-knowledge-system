#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
import tomllib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REQUIRED = ['README.md', 'VERSION', 'PROJECT_MANIFEST.json', 'zensical.toml', 'docs/index.md', 'docs/00-overview.md', 'docs/01-introduction.md', 'docs/02-dynamic-models.md', 'docs/03-time-response.md', 'docs/04-frequency-response.md', 'docs/05-stability.md', 'docs/06-error-analysis.md', 'docs/07-design-compensation.md', 'docs/08-root-locus.md', 'docs/09-nonlinear.md', 'docs/10-digital-control.md', 'docs/11-labview.md', 'docs/12-method-library.md', 'docs/13-checklists.md', 'docs/14-formula-cards.md', 'docs/15-problem-archetypes.md', 'docs/16-decision-trees.md', 'docs/17-counterexamples.md', 'docs/18-exercise-index.md', 'docs/19-experiments-matlab.md', 'docs/20-review-templates.md', 'docs/21-project-maintenance.md', 'docs/22-source-map.md', 'docs/23-appendices.md', 'docs/24-personal-links.md', 'data/progress.csv', 'data/problems.csv', 'data/errors.csv', 'data/models.csv', 'data/formula_reviews.csv', 'data/experiments.csv', 'data/design_cases.csv']
EXPECTED = {
    "nodes": 77,
    "checks": 385,
    "cards": 231,
    "archetypes": 78,
    "boundaries": 44,
    "decisions": 16,
    "experiments": 20,
    "personal": 12,
}

def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)

for rel in REQUIRED:
    path = ROOT / rel
    if not path.exists() or path.stat().st_size == 0:
        fail(f"missing or empty: {rel}")

version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
if not re.fullmatch(r"\d+\.\d+\.\d+", version):
    fail("invalid VERSION")

manifest = json.loads((ROOT / "PROJECT_MANIFEST.json").read_text(encoding="utf-8"))
if manifest.get("version") != version:
    fail("manifest version does not match VERSION")
if manifest.get("source_pdfs_included") is not False:
    fail("manifest must state that source PDFs are excluded")

with (ROOT / "zensical.toml").open("rb") as file:
    config = tomllib.load(file)
project = config.get("project", {})
if project.get("site_name") != "控制工程基础知识体系":
    fail("unexpected site_name")

def flatten(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from flatten(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from flatten(item)

for rel in flatten(project.get("nav", [])):
    if rel.startswith(("http://", "https://")):
        continue
    if not (DOCS / rel).exists():
        fail(f"missing nav target: {rel}")

doc_md_files = list(DOCS.rglob("*.md"))
link_md_files = [
    p for p in ROOT.rglob("*.md")
    if ".git" not in p.parts and "dist" not in p.parts and "releases" not in p.parts
]
all_text = "\n".join(p.read_text(encoding="utf-8") for p in doc_md_files)

if "sandbox:/" in all_text or "/mnt/data/" in all_text:
    fail("container-only link leaked")
if any(ord(ch) < 32 and ch not in "\n\t" for ch in all_text):
    fail("unexpected control character in Markdown")
if any(p.suffix.lower() == ".pdf" for p in ROOT.rglob("*")):
    fail("source PDF accidentally included")

patterns = {
    "nodes": r"(?m)^## (C(?:[1-9]|10|11)\.\d+) ",
    "checks": r"\*\*(C(?:[1-9]|10|11)\.\d+-[a-e])\*\*",
    "cards": r"(?m)^\| (K-C(?:[1-9]|10|11)\.\d+-\d{2}) \|",
    "archetypes": r"(?m)^\| (Q-C(?:[1-9]|10|11)-\d{2}) \|",
    "boundaries": r"(?m)^\| (B-C(?:[1-9]|10|11)-\d{2}) \|",
    "decisions": r"(?m)^## (D-\d{2}) ",
    "experiments": r"(?m)^\| (E-\d{2}) \|",
    "personal": r"(?m)^\| (J-C-\d{2}) \|",
}

for name, pattern in patterns.items():
    matches = re.findall(pattern, all_text)
    unique = sorted(set(matches))
    if len(unique) != EXPECTED[name]:
        fail(f"{name} unique count expected {EXPECTED[name]}, got {len(unique)}")
    if name not in {"checks"}:
        duplicates = [key for key, count in Counter(matches).items() if count > 1]
        if duplicates:
            fail(f"duplicate {name} ids: {duplicates[:10]}")

# Every checklist ID is intentionally mirrored once in its chapter page and once in the aggregate checklist.
check_matches = re.findall(patterns["checks"], all_text)
check_counts = Counter(check_matches)
bad_check_counts = [key for key, count in check_counts.items() if count != 2]
if bad_check_counts:
    fail(f"check IDs must appear exactly twice: {bad_check_counts[:10]}")

# Validate relative Markdown links; anchors are ignored.
link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for md in link_md_files:
    body = md.read_text(encoding="utf-8")
    for target in link_pattern.findall(body):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (md.parent / target).resolve().exists():
            fail(f"broken local link in {md.relative_to(ROOT)}: {target}")

# Ensure public CSVs are templates only.
for csv_path in (ROOT / "data").glob("*.csv"):
    rows = csv_path.read_text(encoding="utf-8-sig").splitlines()
    if len(rows) != 1:
        fail(f"public CSV must contain header only: {csv_path.name}")

print("Project validation passed")
for key, value in EXPECTED.items():
    print(f"  {key:12s}: {value}")
print(f"  version     : {version}")
