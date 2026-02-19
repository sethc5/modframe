"""Build machine-readable indexes from topic README metadata.

Outputs:
  docs/indexes/actors.json
  docs/indexes/legal_citations.json
  docs/indexes/case_studies.json
  docs/indexes/data_sources.json
  docs/indexes/related_modules.json

Usage:
  python scripts/build_indexes.py
  python scripts/build_indexes.py --status sourced
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / "topics"
INDEX_DIR = ROOT / "docs" / "indexes"
TOPIC_RE = re.compile(r"^(\d{3})_(.+)$")
STATUS_RE = re.compile(r"^Status:\s*(.+)$", re.MULTILINE)

INCLUDE_STATUSES = {"sourced", "reviewed", "published"}


def parse_status(text: str) -> str:
    m = STATUS_RE.search(text)
    return m.group(1).strip().lower() if m else "unknown"


def extract_simple_field(text: str, key: str) -> str:
    m = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def extract_block(text: str, key: str) -> list[str]:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == f"{key}:":
            block: list[str] = []
            for nxt in lines[i + 1 :]:
                if not nxt.strip():
                    block.append(nxt)
                    continue
                if re.match(r"^[A-Za-z][A-Za-z ]+:\s*$", nxt.strip()) and not nxt.startswith((" ", "\t")):
                    break
                block.append(nxt)
            return block
    return []


def parse_list_values(block_lines: list[str]) -> list[str]:
    vals: list[str] = []
    for line in block_lines:
        s = line.strip()
        if s.startswith("-"):
            vals.append(s[1:].strip())
    return [v for v in vals if v]


def parse_list_objects(block_lines: list[str]) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for raw in block_lines:
        line = raw.strip()
        if not line:
            continue
        if line.startswith("-"):
            if current:
                items.append(current)
            current = {}
            payload = line[1:].strip()
            if ":" in payload:
                key, val = payload.split(":", 1)
                current[key.strip()] = val.strip()
        elif current is not None and ":" in line:
            key, val = line.split(":", 1)
            current[key.strip()] = val.strip()

    if current:
        items.append(current)
    return items


def parse_case_study(block_lines: list[str]) -> dict:
    out: dict = {}
    if not block_lines:
        return out

    in_actors = False
    actors: list[str] = []
    for raw in block_lines:
        line = raw.strip()
        if not line:
            continue
        if line == "actors:":
            in_actors = True
            continue
        if in_actors:
            if line.startswith("-"):
                actors.append(line[1:].strip())
                continue
            in_actors = False
        if ":" in line:
            key, val = line.split(":", 1)
            out[key.strip()] = val.strip()

    if actors:
        out["actors"] = actors
    return out


def collect_modules(status_filter: str | None) -> list[dict]:
    rows: list[dict] = []
    for section in sorted(TOPICS.iterdir()):
        if not section.is_dir():
            continue
        for topic in sorted(section.iterdir()):
            if not topic.is_dir():
                continue
            m = TOPIC_RE.match(topic.name)
            if not m:
                continue

            readme = topic / "README.md"
            if not readme.exists():
                continue
            text = readme.read_text(encoding="utf-8")
            status = parse_status(text)

            if status_filter and status != status_filter:
                continue
            if not status_filter and status not in INCLUDE_STATUSES:
                continue

            topic_id = m.group(1)
            rows.append(
                {
                    "topic_id": topic_id,
                    "topic": topic.name,
                    "section": section.name,
                    "path": f"topics/{section.name}/{topic.name}",
                    "status": status,
                    "related_modules": [x.strip() for x in extract_simple_field(text, "Related modules").split(",") if x.strip()],
                    "actors": parse_list_objects(extract_block(text, "Actors")),
                    "statutes": parse_list_values(extract_block(text, "Statutes")),
                    "cases": parse_list_values(extract_block(text, "Cases")),
                    "case_study": parse_case_study(extract_block(text, "Case study")),
                    "reform_proposals": parse_list_objects(extract_block(text, "Reform proposals")),
                    "data_sources": parse_list_objects(extract_block(text, "Data sources")),
                }
            )
    return rows


def build_indexes(rows: list[dict]) -> dict[str, list[dict]]:
    actors: dict[str, dict] = {}
    legal: dict[str, dict] = {}
    case_studies: list[dict] = []
    data_sources: dict[str, dict] = {}
    related_edges: list[dict] = []

    for row in rows:
        tid = row["topic_id"]
        path = row["path"]

        for actor in row["actors"]:
            name = actor.get("name", "").strip()
            if not name:
                continue
            rec = actors.setdefault(name, {"name": name, "types": set(), "topics": []})
            actor_type = actor.get("type", "").strip()
            if actor_type:
                rec["types"].add(actor_type)
            rec["topics"].append(tid)

        for statute in row["statutes"]:
            rec = legal.setdefault(statute, {"citation": statute, "kind": "statute", "topics": []})
            rec["topics"].append(tid)

        for case in row["cases"]:
            rec = legal.setdefault(case, {"citation": case, "kind": "case", "topics": []})
            rec["topics"].append(tid)

        if row["case_study"]:
            case_studies.append({"topic_id": tid, "path": path, **row["case_study"]})

        for ds in row["data_sources"]:
            name = ds.get("source", "").strip()
            if not name:
                continue
            rec = data_sources.setdefault(name, {"source": name, "topics": [], "details": []})
            rec["topics"].append(tid)
            rec["details"].append({"topic_id": tid, **ds})

        for target in row["related_modules"]:
            related_edges.append({"from": tid, "to": target})

    def uniq_sorted(values: list[str]) -> list[str]:
        return sorted(set(values))

    actors_out = []
    for item in actors.values():
        actors_out.append(
            {
                "name": item["name"],
                "types": sorted(item["types"]),
                "topics": uniq_sorted(item["topics"]),
            }
        )
    actors_out.sort(key=lambda x: x["name"].lower())

    legal_out = []
    for item in legal.values():
        legal_out.append(
            {
                "citation": item["citation"],
                "kind": item["kind"],
                "topics": uniq_sorted(item["topics"]),
            }
        )
    legal_out.sort(key=lambda x: x["citation"].lower())

    case_studies.sort(key=lambda x: (x.get("date", ""), x["topic_id"]))

    data_out = []
    for item in data_sources.values():
        data_out.append(
            {
                "source": item["source"],
                "topics": uniq_sorted(item["topics"]),
                "details": item["details"],
            }
        )
    data_out.sort(key=lambda x: x["source"].lower())

    related_edges.sort(key=lambda x: (x["from"], x["to"]))

    return {
        "actors": actors_out,
        "legal_citations": legal_out,
        "case_studies": case_studies,
        "data_sources": data_out,
        "related_modules": related_edges,
    }


def write_indexes(indexes: dict[str, list[dict]]) -> None:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    file_map = {
        "actors": "actors.json",
        "legal_citations": "legal_citations.json",
        "case_studies": "case_studies.json",
        "data_sources": "data_sources.json",
        "related_modules": "related_modules.json",
    }
    for key, filename in file_map.items():
        (INDEX_DIR / filename).write_text(json.dumps(indexes[key], indent=2) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    status_filter = None
    if "--status" in argv:
        i = argv.index("--status")
        if i + 1 < len(argv):
            status_filter = argv[i + 1].strip().lower()

    rows = collect_modules(status_filter)
    indexes = build_indexes(rows)
    write_indexes(indexes)

    print(f"Index build complete: {len(rows)} module(s) processed")
    print(f"  actors:          {len(indexes['actors'])}")
    print(f"  legal_citations: {len(indexes['legal_citations'])}")
    print(f"  case_studies:    {len(indexes['case_studies'])}")
    print(f"  data_sources:    {len(indexes['data_sources'])}")
    print(f"  related_edges:   {len(indexes['related_modules'])}")
    print(f"  output_dir:      {INDEX_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
