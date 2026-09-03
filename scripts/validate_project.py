#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
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
EXAM_DOCS = [
    "docs/tsinghua-822/1995-1999.md",
    "docs/tsinghua-822/2000-2004.md",
    "docs/tsinghua-822/2005-2009.md",
    "docs/tsinghua-822/2010-2014.md",
    "docs/tsinghua-822/2015-2019.md",
    "docs/tsinghua-822/2020-2024.md",
]
KEY_DOCS = [
    "docs/key-problems/01-source-examples.md",
    "docs/key-problems/02-lecture-examples.md",
    "docs/key-problems/03-slide-variants.md",
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
    "docs/27-tsinghua-822-insights.md",
    "docs/28-recurring-problem-families.md",
    "docs/javascripts/mathjax.js",
    "docs/assets/stylesheets/extra.css",
    "docs/tsinghua-822/index.md",
    "docs/tsinghua-822/2024-deep-solutions.md",
    "docs/key-problems/index.md",
    "data/progress.csv",
    "data/problems.csv",
    "data/errors.csv",
    "data/models.csv",
    "data/formula_reviews.csv",
    "data/experiments.csv",
    "data/design_cases.csv",
    "data/exercise_progress.csv",
    "data/tsinghua_822_progress.csv",
    "data/key_problem_progress.csv",
    "data/exercise_catalog.json",
    "data/tsinghua_822_exam_catalog.json",
    "data/key_problem_catalog.json",
    "releases/v1.1/README.md",
    "releases/v1.2/README.md",
    *EXERCISE_DOCS,
    *EXAM_DOCS,
    *KEY_DOCS,
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
    "exams": 190,
    "key_problems": 40,
}
CHAPTER_COUNTS = {1: 6, 2: 26, 3: 33, 4: 21, 5: 26, 6: 16, 7: 20, 8: 10, 9: 18, 10: 17}
YEAR_COUNTS = {
    1995: 2,
    1996: 5,
    1997: 7,
    1998: 24,
    1999: 2,
    2000: 5,
    2001: 5,
    2002: 6,
    2003: 4,
    2004: 6,
    2005: 5,
    2006: 3,
    2007: 6,
    2008: 4,
    2009: 5,
    2010: 3,
    2011: 3,
    2012: 6,
    2013: 6,
    2014: 12,
    2015: 3,
    2016: 5,
    2017: 6,
    2018: 7,
    2019: 6,
    2020: 8,
    2021: 9,
    2022: 9,
    2023: 9,
    2024: 9,
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def repository_files() -> list[Path]:
    """Return tracked and non-ignored candidate files, including uncommitted additions."""
    if not (ROOT / ".git").exists():
        excluded_parts = {".cache", ".venv", "__pycache__", "private", "site"}
        return sorted(
            path
            for path in ROOT.rglob("*")
            if path.is_file()
            and not excluded_parts.intersection(path.relative_to(ROOT).parts)
            and not path.relative_to(ROOT).as_posix().startswith("data/private-")
        )

    try:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        fail(f"cannot enumerate repository files with Git: {error}")

    relative_paths = result.stdout.decode("utf-8").split("\0")
    return [
        ROOT / relative
        for relative in relative_paths
        if relative and (ROOT / relative).is_file()
    ]


project_files = repository_files()

for rel in REQUIRED:
    p = ROOT / rel
    if not p.exists() or p.stat().st_size == 0:
        fail(f"missing or empty: {rel}")
version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
if not re.fullmatch(r"\d+\.\d+\.\d+", version):
    fail(f"invalid VERSION: {version}")
manifest = json.loads((ROOT / "PROJECT_MANIFEST.json").read_text(encoding="utf-8"))
for key, value in [
    ("version", version),
    ("exercise_analyses", 193),
    ("tsinghua_822_exam_units", 190),
    ("key_problem_source_cards", 40),
    ("source_linked_analysis_cards", 423),
    ("data_templates", 10),
    ("machine_catalogs", 3),
    ("source_pdfs_included", False),
]:
    if manifest.get(key) != value:
        fail(f"manifest {key} mismatch: {manifest.get(key)}")
with (ROOT / "zensical.toml").open("rb") as f:
    cfg = tomllib.load(f)
project = cfg.get("project", {})
if project.get("site_name") != "控制工程基础知识体系":
    fail("unexpected site_name")
extra_js = project.get("extra_javascript", [])
if "javascripts/mathjax.js" not in extra_js or not any(
    "mathjax" in x.lower() and x.startswith("https://") for x in extra_js
):
    fail("MathJax not fully configured")
raw = (ROOT / "zensical.toml").read_text(encoding="utf-8")
if "pymdownx.arithmatex.generic = true" not in raw:
    fail("Arithmatex generic missing")

mathjax_js = (DOCS / "javascripts/mathjax.js").read_text(encoding="utf-8")
for token in ("window.MathJax", "document$.subscribe", "typesetPromise"):
    if token not in mathjax_js:
        fail(f"MathJax configuration missing token: {token}")


def flatten(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, list):
        for x in v:
            yield from flatten(x)
    elif isinstance(v, dict):
        for x in v.values():
            yield from flatten(x)


for rel in flatten(project.get("nav", [])):
    if rel.startswith(("http://", "https://")):
        continue
    if not (DOCS / rel).exists():
        fail(f"missing nav target: {rel}")

all_md = list(DOCS.rglob("*.md"))
all_text = "\n".join(p.read_text(encoding="utf-8") for p in all_md)
if "sandbox:/" in all_text or "/mnt/data/" in all_text:
    fail("container-only link leaked")
if any(ord(character) < 32 and character not in "\n\t" for character in all_text):
    fail("unexpected control character in Markdown")
prohibited_document_suffixes = {".pdf", ".doc", ".docx"}
prohibited_documents = [
    path.relative_to(ROOT)
    for path in project_files
    if path.suffix.lower() in prohibited_document_suffixes
]
if prohibited_documents:
    fail(f"source documents included: {prohibited_documents[:8]}")
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
    "exams": r"(?m)^## (TH-\d{4}-(?:MC)?\d{2})｜",
    "key_problems": r"(?m)^## (KP-(?:A|B|S)[A-Z0-9]+)｜",
}
unique = {}
for name, pat in patterns.items():
    matches = re.findall(pat, all_text)
    unique[name] = set(matches)
    if len(unique[name]) != EXPECTED[name]:
        fail(f"{name} count expected {EXPECTED[name]}, got {len(unique[name])}")
    if name != "checks":
        dup = [k for k, v in Counter(matches).items() if v > 1]
        if dup:
            fail(f"duplicate {name} ids: {dup[:8]}")
check_counts = Counter(re.findall(patterns["checks"], all_text))
if any(v != 2 for v in check_counts.values()):
    fail("check IDs must appear exactly twice")

# Every source-linked card owns a short, stable explicit anchor.  The visible
# title may evolve, but published EX / TH / KP links must not follow a generated
# slug that changes with the title text.
stable_ids = unique["exercises"] | unique["exams"] | unique["key_problems"]
stable_heading_pattern = re.compile(
    r"(?m)^## (EX-C(?:[1-9]|10)-\d{2}|TH-\d{4}-(?:MC)?\d{2}|KP-(?:A|B|S)[A-Z0-9]+)｜[^\r\n]*\{\s*#([a-z0-9-]+)\s*\}\s*$"
)
stable_heading_anchors = dict(stable_heading_pattern.findall(all_text))
if set(stable_heading_anchors) != stable_ids:
    missing = sorted(stable_ids - set(stable_heading_anchors))
    extra = sorted(set(stable_heading_anchors) - stable_ids)
    fail(
        f"stable explicit anchor coverage mismatch: missing={missing[:8]} extra={extra[:8]}"
    )
bad_anchors = [
    sid for sid, anchor in stable_heading_anchors.items() if anchor != sid.lower()
]
if bad_anchors:
    fail(f"stable explicit anchor mismatch: {bad_anchors[:8]}")

# Existing textbook exercise coverage.
expected_exercise_ids = {
    f"EX-C{chapter}-{number:02d}"
    for chapter, count in CHAPTER_COUNTS.items()
    for number in range(1, count + 1)
}
if unique["exercises"] != expected_exercise_ids:
    missing = sorted(expected_exercise_ids - unique["exercises"])
    extra = sorted(unique["exercises"] - expected_exercise_ids)
    fail(f"exercise ID coverage mismatch; missing={missing[:8]}, extra={extra[:8]}")

chapter_exercise_counts = Counter(
    int(item.split("-")[1][1:]) for item in unique["exercises"]
)
if dict(sorted(chapter_exercise_counts.items())) != CHAPTER_COUNTS:
    fail(
        f"exercise chapter counts mismatch: {dict(sorted(chapter_exercise_counts.items()))}"
    )

exercise_catalog = json.loads(
    (ROOT / "data/exercise_catalog.json").read_text(encoding="utf-8-sig")
)
if (
    not isinstance(exercise_catalog, list)
    or len(exercise_catalog) != EXPECTED["exercises"]
):
    fail("exercise_catalog.json must contain 193 entries")
required_exercise_fields = {
    "id",
    "number",
    "chapter",
    "title",
    "pages",
    "nodes",
    "archetype",
    "summary",
    "steps",
    "formulas",
    "checkpoint",
    "pitfalls",
    "supplement",
}
exercise_catalog_ids: list[str] = []
for item in exercise_catalog:
    if not isinstance(item, dict) or not required_exercise_fields.issubset(item):
        item_id = item.get("id") if isinstance(item, dict) else item
        fail(f"exercise catalog entry missing fields: {item_id}")
    exercise_catalog_ids.append(item["id"])
    chapter = item["chapter"]
    number = int(item["number"].split("-")[1])
    expected_id = f"EX-C{chapter}-{number:02d}"
    if item["id"] != expected_id:
        fail(f"exercise catalog ID/number mismatch: {item['id']} vs {item['number']}")
    if not item["nodes"] or not all(node in unique["nodes"] for node in item["nodes"]):
        fail(f"exercise catalog node mapping invalid: {item['id']} -> {item['nodes']}")
    if item["archetype"] not in unique["archetypes"]:
        fail(
            f"exercise catalog archetype mapping invalid: {item['id']} -> {item['archetype']}"
        )
    if (
        not item["summary"].strip()
        or not item["checkpoint"].strip()
        or not item["supplement"].strip()
    ):
        fail(f"exercise catalog explanation field empty: {item['id']}")
    if len(item["steps"]) < 2 or not item["pitfalls"]:
        fail(f"exercise catalog route/pitfall too thin: {item['id']}")

if set(exercise_catalog_ids) != expected_exercise_ids or len(
    exercise_catalog_ids
) != len(set(exercise_catalog_ids)):
    fail("exercise catalog IDs do not exactly match Markdown cards")
if Counter(item["chapter"] for item in exercise_catalog) != Counter(CHAPTER_COUNTS):
    fail("exercise catalog chapter counts are wrong")

exercise_body = "\n".join(
    (ROOT / relative_path).read_text(encoding="utf-8")
    for relative_path in EXERCISE_DOCS[1:]
)
exercise_chunks = [
    chunk
    for chunk in re.split(r"(?m)(?=^## EX-C(?:[1-9]|10)-\d{2}｜)", exercise_body)
    if chunk.startswith("## EX-")
]
if len(exercise_chunks) != EXPECTED["exercises"]:
    fail(f"could not split 193 exercise cards; got {len(exercise_chunks)}")
for chunk in exercise_chunks:
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

# Tsinghua exam catalogue.
exam = json.loads(
    (ROOT / "data/tsinghua_822_exam_catalog.json").read_text(encoding="utf-8")
)
if not isinstance(exam, list) or len(exam) != EXPECTED["exams"]:
    fail("exam catalogue must have 190 entries")
if any(not isinstance(item, dict) for item in exam):
    fail("exam catalogue entries must be objects")
exam_ids = [item.get("id") for item in exam]
if set(exam_ids) != unique["exams"] or len(exam_ids) != len(set(exam_ids)):
    fail("exam ID mismatch")
if dict(sorted(Counter(item["year"] for item in exam).items())) != YEAR_COUNTS:
    fail("exam year counts mismatch")
required_exam_fields = {
    "id",
    "year",
    "number",
    "title",
    "source_pages",
    "profile",
    "nodes",
    "archetype",
    "summary",
    "route",
    "formulas",
    "result_status",
    "pitfalls",
    "model_insight",
    "evidence_status",
}
for item in exam:
    if not required_exam_fields.issubset(item):
        fail(f"exam entry missing fields: {item.get('id')}")
    if not item["id"].startswith(f"TH-{item['year']}-"):
        fail(f"exam ID/year mismatch: {item['id']} vs {item['year']}")
    if (
        not isinstance(item["source_pages"], list)
        or not item["source_pages"]
        or not all(isinstance(page, int) and page > 0 for page in item["source_pages"])
        or not isinstance(item["nodes"], list)
        or not item["nodes"]
        or not isinstance(item["route"], list)
        or len(item["route"]) < 3
        or not isinstance(item["formulas"], list)
        or not isinstance(item["pitfalls"], list)
        or not item["pitfalls"]
        or not item["model_insight"].strip()
        or not item["summary"].strip()
        or not item["evidence_status"].strip()
    ):
        fail(f"exam entry too thin or malformed: {item['id']}")
    if not all(node in unique["nodes"] for node in item["nodes"]):
        fail(f"bad exam nodes: {item['id']}")
    if item["archetype"] not in unique["archetypes"]:
        fail(f"bad exam archetype: {item['id']}")

# Key problem catalogue and duplicate graph.
key = json.loads((ROOT / "data/key_problem_catalog.json").read_text(encoding="utf-8"))
if not isinstance(key, list) or len(key) != EXPECTED["key_problems"]:
    fail("key problem catalog must have 40 entries")
if any(not isinstance(item, dict) for item in key):
    fail("key problem catalog entries must be objects")
key_ids = [item.get("id") for item in key]
if set(key_ids) != unique["key_problems"] or len(key_ids) != len(set(key_ids)):
    fail("key problem ID mismatch")
key_id_set = set(key_ids)
for item in key:
    if not {
        "id",
        "label",
        "title",
        "source_pages",
        "profile",
        "nodes",
        "archetype",
        "duplicate_of",
        "route",
        "pitfalls",
        "model_insight",
        "summary",
    }.issubset(item):
        fail(f"key entry missing fields: {item.get('id')}")
    if (
        not isinstance(item["source_pages"], list)
        or not item["source_pages"]
        or not all(isinstance(page, int) and page > 0 for page in item["source_pages"])
        or not isinstance(item["nodes"], list)
        or not item["nodes"]
        or not isinstance(item["route"], list)
        or len(item["route"]) < 2
        or not isinstance(item["pitfalls"], list)
        or not item["pitfalls"]
        or not item["model_insight"].strip()
        or not item["summary"].strip()
    ):
        fail(f"key entry too thin or malformed: {item['id']}")
    if not all(node in unique["nodes"] for node in item["nodes"]):
        fail(f"bad key-problem nodes: {item['id']}")
    if item["archetype"] not in unique["archetypes"]:
        fail(f"bad key-problem archetype: {item['id']}")
    if item["duplicate_of"] == item["id"] or (
        item["duplicate_of"] and item["duplicate_of"] not in key_id_set
    ):
        fail(f"invalid duplicate_of: {item['id']}")

key_by_id = {item["id"]: item for item in key}
for item in key:
    seen: set[str] = set()
    current_id = item["id"]
    while current_id:
        if current_id in seen:
            fail(f"duplicate_of cycle detected at: {item['id']}")
        seen.add(current_id)
        current_id = key_by_id[current_id]["duplicate_of"]

# Card field completeness.
exam_text = "\n".join((ROOT / p).read_text(encoding="utf-8") for p in EXAM_DOCS)
chunks = [
    x
    for x in re.split(r"(?m)(?=^## TH-\d{4}-(?:MC)?\d{2}｜)", exam_text)
    if x.startswith("## TH-")
]
if len(chunks) != 190:
    fail(f"exam card split got {len(chunks)}")
for ch in chunks:
    eid = re.match(r"## (TH-[^｜]+)", ch).group(1)
    for token in [
        "**题源摘要（非逐字转录）**",
        "**来源定位**",
        "**对应知识点**",
        "### 我的独立推导路线（非官方答案）",
        "### 关键公式与判据",
        "### 结论/核验状态",
        "### 易错点",
        "我的思考：为什么这题值得收进体系",
        "证据边界",
    ]:
        if token not in ch:
            fail(f"exam card missing {token}: {eid}")
key_text = "\n".join((ROOT / p).read_text(encoding="utf-8") for p in KEY_DOCS)
chunks = [x for x in re.split(r"(?m)(?=^## KP-)", key_text) if x.startswith("## KP-")]
if len(chunks) != 40:
    fail(f"key card split got {len(chunks)}")
for ch in chunks:
    kid = re.match(r"## (KP-[^｜]+)", ch).group(1)
    for token in [
        "**题面要素（摘要）**",
        "**来源定位**",
        "**对应知识点**",
        "### 参考资料给出的路线",
        "### 我的重构解法",
        "### 复核清单",
        "我的思考",
    ]:
        if token not in ch:
            fail(f"key card missing {token}: {kid}")

# Deep solution anchors and chapter reverse links.
deep = (DOCS / "tsinghua-822/2024-deep-solutions.md").read_text(encoding="utf-8")
for n in range(1, 10):
    if f"## 深解 TH-2024-{n:02d}" not in deep:
        fail(f"2024 deep solution missing {n}")
deep_2024_09 = deep.split("## 深解 TH-2024-09", 1)[1]
for token in [
    r"| G | \(-0.6\pm j0.6\)",
    r"| H | \(-0.8\pm j0.8\)",
    "**非渐近稳定**：A、B、D、H",
    "**稳定组中阶跃有振荡/超调**：C、G",
    "**稳定组中调整时间最长**：C、G",
]:
    if token not in deep_2024_09:
        fail(f"TH-2024-09 deep solution inconsistent: {token}")
exam_2024_09 = next(x for x in exam if x["id"] == "TH-2024-09")
for token in ["-0.6±0.6j", "-0.8±0.8j"]:
    if token not in exam_2024_09["summary"]:
        fail(f"TH-2024-09 catalogue missing pole: {token}")
for c, file in {
    1: "01-introduction.md",
    2: "02-dynamic-models.md",
    3: "03-time-response.md",
    4: "04-frequency-response.md",
    5: "05-stability.md",
    6: "06-error-analysis.md",
    7: "07-design-compensation.md",
    8: "08-root-locus.md",
    9: "09-nonlinear.md",
    10: "10-digital-control.md",
}.items():
    t = (DOCS / file).read_text(encoding="utf-8")
    if "<!-- TSINGHUA822:START -->" not in t or "清华 822 真题挂接" not in t:
        fail(f"chapter C{c} lacks exam reverse links")

# Formula atlas and links.
formula_atlas = (DOCS / "25-formula-atlas.md").read_text(encoding="utf-8")
if formula_atlas.count(r"\[") < 30 or formula_atlas.count(r"\[") != formula_atlas.count(
    r"\]"
):
    fail("formula atlas math blocks bad")
for token in ("F-C1-02", "F-C3-04", "F-C4-06", "F-C5-03", "F-C7-04", "F-C10-08"):
    if token not in formula_atlas:
        fail(f"formula atlas missing anchor: {token}")

link_pat = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
link_markdown_files = [
    path
    for path in project_files
    if path.suffix.lower() == ".md"
    and "dist" not in path.relative_to(ROOT).parts
    and "releases" not in path.relative_to(ROOT).parts
]
for markdown_file in link_markdown_files:
    body = markdown_file.read_text(encoding="utf-8")
    for raw_target in link_pat.findall(body):
        raw_target = raw_target.strip()
        if raw_target.startswith(("http://", "https://", "mailto:")):
            continue
        target, separator, fragment = raw_target.partition("#")
        target_path = (
            markdown_file if not target else (markdown_file.parent / target).resolve()
        )
        if not target_path.exists():
            fail(f"broken local link in {markdown_file.relative_to(ROOT)}: {target}")
        if separator and fragment.lower().startswith(("ex-", "th-", "kp-")):
            target_body = target_path.read_text(encoding="utf-8")
            explicit_pattern = r"\{\s*#" + re.escape(fragment.lower()) + r"\s*\}"
            if not re.search(explicit_pattern, target_body, re.IGNORECASE):
                fail(
                    f"broken stable anchor in {markdown_file.relative_to(ROOT)}: {raw_target}"
                )

# CSVs remain templates.
public_csv_files = [
    path
    for path in project_files
    if path.parent == ROOT / "data" and path.suffix.lower() == ".csv"
]
for csv_path in public_csv_files:
    if len(csv_path.read_text(encoding="utf-8-sig").splitlines()) != 1:
        fail(f"public CSV must contain header only: {csv_path.name}")

bundle = ROOT / "dist" / f"控制工程基础知识体系_v{version}.md"
if bundle.exists():
    bt = bundle.read_text(encoding="utf-8")
    for token in [
        "# LaTeX 公式图鉴",
        "# 习题反哺补充库",
        "# 习题解逐题解析",
        "EX-C10-17",
        "# 清华大学 822 控制工程基础真题全量索引",
        "TH-1995-01",
        "TH-2024-09",
        "# 清华 822 重点题与答案",
        "KP-S12",
        "# 2024 年清华 822：九题深度解析",
    ]:
        if token not in bt:
            fail(f"bundle missing {token}")

# The manifest count includes tracked files plus non-ignored candidate additions.
# Ignored caches, generated sites, and private local data never affect the count.
if manifest.get("project_file_count") != len(project_files):
    fail(
        "manifest project_file_count expected "
        f"{len(project_files)}, got {manifest.get('project_file_count')}"
    )
print("Project validation passed")
for k, v in EXPECTED.items():
    print(f"  {k:14s}: {v}")
print("  year coverage  : " + ", ".join(f"{y}={c}" for y, c in YEAR_COUNTS.items()))
print("  source cards   : 423")
print("  mathjax        : enabled")
print(f"  version        : {version}")
