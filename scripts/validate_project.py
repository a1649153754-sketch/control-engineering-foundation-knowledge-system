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

EXERCISE_DOCS = [
    "docs/exercises/index.md",
    "docs/exercises/01-introduction.md",
    "docs/exercises/02-dynamic-models.md",
    "docs/exercises/03-time-response.md",
    "docs/exercises/04-frequency-response.md",
    "docs/exercises/05-stability.md",
    "docs/exercises/06-error-analysis.md",
    "docs/exercises/07-design-compensation.md",
    "docs/exercises/08-root-locus.md",
    "docs/exercises/09-nonlinear.md",
    "docs/exercises/10-digital-control.md",
]

REQUIRED = [
    "README.md",
    "VERSION",
    "CHANGELOG.md",
    "ROADMAP.md",
    "PROJECT_MANIFEST.json",
    "CITATION.cff",
    "zensical.toml",
    "docs/index.md",
    "docs/00-overview.md",
    "docs/01-introduction.md",
    "docs/02-dynamic-models.md",
    "docs/03-time-response.md",
    "docs/04-frequency-response.md",
    "docs/05-stability.md",
    "docs/06-error-analysis.md",
    "docs/07-design-compensation.md",
    "docs/08-root-locus.md",
    "docs/09-nonlinear.md",
    "docs/10-digital-control.md",
    "docs/11-labview.md",
    "docs/12-method-library.md",
    "docs/13-checklists.md",
    "docs/14-formula-cards.md",
    "docs/15-problem-archetypes.md",
    "docs/16-decision-trees.md",
    "docs/17-counterexamples.md",
    "docs/18-exercise-index.md",
    "docs/19-experiments-matlab.md",
    "docs/20-review-templates.md",
    "docs/21-project-maintenance.md",
    "docs/22-source-map.md",
    "docs/23-appendices.md",
    "docs/24-personal-links.md",
    "docs/25-formula-atlas.md",
    "docs/26-exercise-supplements.md",
    "docs/javascripts/mathjax.js",
    "docs/assets/stylesheets/extra.css",
    "data/progress.csv",
    "data/problems.csv",
    "data/errors.csv",
    "data/models.csv",
    "data/formula_reviews.csv",
    "data/experiments.csv",
    "data/design_cases.csv",
    "data/exercise_progress.csv",
    "data/exercise_catalog.json",
    "releases/v1.1/README.md",
    *EXERCISE_DOCS,
]

EXPECTED = {
    "nodes": 77,
    "checks": 385,
    "cards": 231,
    "archetypes": 78,
    "boundaries": 44,
    "decisions": 16,
    "experiments": 20,
    "personal": 12,
    "exercises": 193,
}

CHAPTER_COUNTS = {1: 6, 2: 26, 3: 33, 4: 21, 5: 26, 6: 16, 7: 20, 8: 10, 9: 18, 10: 17}


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
if manifest.get("exercise_analyses") != EXPECTED["exercises"]:
    fail("manifest exercise count is wrong")
if manifest.get("data_templates") != 8:
    fail("manifest data template count is wrong")

with (ROOT / "zensical.toml").open("rb") as file:
    config = tomllib.load(file)
project = config.get("project", {})
if project.get("site_name") != "控制工程基础知识体系":
    fail("unexpected site_name")

extra_js = project.get("extra_javascript", [])
if "javascripts/mathjax.js" not in extra_js:
    fail("local MathJax configuration is not loaded")
if not any("mathjax" in item.lower() and item.startswith("https://") for item in extra_js):
    fail("MathJax browser renderer CDN is not loaded")
raw_toml = (ROOT / "zensical.toml").read_text(encoding="utf-8")
if "pymdownx.arithmatex.generic = true" not in raw_toml:
    fail("Arithmatex generic mode is not enabled")

mathjax_js = (DOCS / "javascripts/mathjax.js").read_text(encoding="utf-8")
for token in ("window.MathJax", "document$.subscribe", "typesetPromise"):
    if token not in mathjax_js:
        fail(f"MathJax configuration missing token: {token}")


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
    "exercises": r"(?m)^## (EX-C(?:[1-9]|10)-\d{2})｜",
}

unique_by_name: dict[str, set[str]] = {}
for name, pattern in patterns.items():
    matches = re.findall(pattern, all_text)
    unique = set(matches)
    unique_by_name[name] = unique
    if len(unique) != EXPECTED[name]:
        fail(f"{name} unique count expected {EXPECTED[name]}, got {len(unique)}")
    if name != "checks":
        duplicates = [key for key, count in Counter(matches).items() if count > 1]
        if duplicates:
            fail(f"duplicate {name} ids: {duplicates[:10]}")

# Every checklist ID is intentionally mirrored once in its chapter page and once in the aggregate checklist.
check_matches = re.findall(patterns["checks"], all_text)
check_counts = Counter(check_matches)
bad_check_counts = [key for key, count in check_counts.items() if count != 2]
if bad_check_counts:
    fail(f"check IDs must appear exactly twice: {bad_check_counts[:10]}")

# Verify all expected exercise IDs and chapter counts.
expected_exercise_ids = {
    f"EX-C{chapter}-{number:02d}"
    for chapter, count in CHAPTER_COUNTS.items()
    for number in range(1, count + 1)
}
if unique_by_name["exercises"] != expected_exercise_ids:
    missing = sorted(expected_exercise_ids - unique_by_name["exercises"])
    extra = sorted(unique_by_name["exercises"] - expected_exercise_ids)
    fail(f"exercise ID coverage mismatch; missing={missing[:8]}, extra={extra[:8]}")

chapter_exercise_counts = Counter(int(item.split("-")[1][1:]) for item in unique_by_name["exercises"])
if dict(sorted(chapter_exercise_counts.items())) != CHAPTER_COUNTS:
    fail(f"exercise chapter counts mismatch: {dict(sorted(chapter_exercise_counts.items()))}")

# Validate the machine-readable catalogue and its references.
catalog = json.loads((ROOT / "data/exercise_catalog.json").read_text(encoding="utf-8-sig"))
if not isinstance(catalog, list) or len(catalog) != EXPECTED["exercises"]:
    fail("exercise_catalog.json must contain 193 entries")
required_catalog_fields = {
    "id", "number", "chapter", "title", "pages", "nodes", "archetype",
    "summary", "steps", "formulas", "checkpoint", "pitfalls", "supplement",
}
catalog_ids = []
for item in catalog:
    if not isinstance(item, dict) or not required_catalog_fields.issubset(item):
        fail(f"catalog entry missing fields: {item.get('id') if isinstance(item, dict) else item}")
    catalog_ids.append(item["id"])
    chapter = item["chapter"]
    number = int(item["number"].split("-")[1])
    expected_id = f"EX-C{chapter}-{number:02d}"
    if item["id"] != expected_id:
        fail(f"catalog ID/number mismatch: {item['id']} vs {item['number']}")
    if not item["nodes"] or not all(node in unique_by_name["nodes"] for node in item["nodes"]):
        fail(f"catalog node mapping invalid: {item['id']} -> {item['nodes']}")
    if item["archetype"] not in unique_by_name["archetypes"]:
        fail(f"catalog archetype mapping invalid: {item['id']} -> {item['archetype']}")
    if not item["summary"].strip() or not item["checkpoint"].strip() or not item["supplement"].strip():
        fail(f"catalog explanation field empty: {item['id']}")
    if len(item["steps"]) < 2 or not item["pitfalls"]:
        fail(f"catalog route/pitfall too thin: {item['id']}")
if set(catalog_ids) != expected_exercise_ids or len(catalog_ids) != len(set(catalog_ids)):
    fail("exercise catalogue IDs do not exactly match Markdown cards")
if Counter(item["chapter"] for item in catalog) != Counter(CHAPTER_COUNTS):
    fail("exercise catalogue chapter counts are wrong")

# Every exercise card must expose the same minimum fields.
exercise_body = "\n".join((ROOT / rel).read_text(encoding="utf-8") for rel in EXERCISE_DOCS[1:])
card_chunks = re.split(r"(?m)(?=^## EX-C(?:[1-9]|10)-\d{2}｜)", exercise_body)
card_chunks = [chunk for chunk in card_chunks if chunk.startswith("## EX-")]
if len(card_chunks) != EXPECTED["exercises"]:
    fail(f"could not split 193 exercise cards; got {len(card_chunks)}")
for chunk in card_chunks:
    exercise_id_match = re.match(r"## (EX-C(?:[1-9]|10)-\d{2})｜", chunk)
    exercise_id = exercise_id_match.group(1) if exercise_id_match else "unknown"
    required_phrases = [
        "**题意摘要**",
        "**对应知识点**",
        "**来源定位**",
        "### 解析路线",
        "### 结果校验",
        "### 易错点",
        "由本题补入知识库",
    ]
    missing_phrases = [phrase for phrase in required_phrases if phrase not in chunk]
    if missing_phrases:
        fail(f"exercise card missing fields: {exercise_id} -> {missing_phrases}")
    if not re.search(r"`C(?:[1-9]|10)\.\d+`", chunk):
        fail(f"exercise card lacks node mapping: {exercise_id}")
    if not re.search(r"`Q-C(?:[1-9]|10)-\d{2}`", chunk):
        fail(f"exercise card lacks archetype mapping: {exercise_id}")

# Formula atlas should contain substantial display math and known anchor formulas.
formula_atlas = (DOCS / "25-formula-atlas.md").read_text(encoding="utf-8")
if formula_atlas.count("\\[") < 30 or formula_atlas.count("\\]") != formula_atlas.count("\\["):
    fail("formula atlas display-math blocks are missing or unbalanced")
for token in ("F-C1-02", "F-C3-04", "F-C4-06", "F-C5-03", "F-C7-04", "F-C10-08"):
    if token not in formula_atlas:
        fail(f"formula atlas missing anchor: {token}")

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

# If the current-version bundle has been generated, it must contain the new layers.
bundle = ROOT / "dist" / f"控制工程基础知识体系_v{version}.md"
if bundle.exists():
    bundle_text = bundle.read_text(encoding="utf-8")
    for token in ("# LaTeX 公式图鉴", "# 习题反哺补充库", "# 习题解逐题解析", "EX-C10-17"):
        if token not in bundle_text:
            fail(f"current bundle missing token: {token}")

print("Project validation passed")
for key, value in EXPECTED.items():
    print(f"  {key:12s}: {value}")
print("  chapters     : " + ", ".join(f"C{k}={v}" for k, v in CHAPTER_COUNTS.items()))
print("  mathjax      : enabled")
print(f"  version      : {version}")
