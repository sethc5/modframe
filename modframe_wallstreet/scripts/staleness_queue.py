"""Generate staleness-priority queue using README metadata recency and legal volatility.

Usage:
  python scripts/staleness_queue.py
  python scripts/staleness_queue.py --next 20
  python scripts/staleness_queue.py --format json
"""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / "topics"
TOPIC_RE = re.compile(r"^(\d{3})_(.+)$")
STATUS_RE = re.compile(r"^Status:\s*(.+)$", re.MULTILINE)
YM_RE = re.compile(r"^(\d{4})-(0[1-9]|1[0-2])$")


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
            out: list[str] = []
            for nxt in lines[i + 1 :]:
                if not nxt.strip():
                    out.append(nxt)
                    continue
                if re.match(r"^[A-Za-z][A-Za-z ]+:\s*$", nxt.strip()) and not nxt.startswith((" ", "\t")):
                    break
                out.append(nxt)
            return out
    return []


def parse_list_values(lines: list[str]) -> list[str]:
    return [ln.strip()[1:].strip() for ln in lines if ln.strip().startswith("-")]


def months_since(ym: str) -> int:
    m = YM_RE.match(ym)
    if not m:
        return 999
    year = int(m.group(1))
    month = int(m.group(2))
    today = dt.date.today()
    return max(0, (today.year - year) * 12 + (today.month - month))


def priority_score(last_reviewed: str, statutes: int, cases: int, status: str) -> float:
    age = months_since(last_reviewed)
    legal_volatility = min(12, statutes + cases)
    status_weight = {
        "sourced": 10,
        "reviewed": 6,
        "published": 4,
    }.get(status, 0)
    missing_penalty = 20 if age >= 999 else 0
    return round((age * 2.0) + legal_volatility + status_weight + missing_penalty, 3)


def scan() -> list[dict]:
    rows: list[dict] = []
    for section in sorted(TOPICS.iterdir()):
        if not section.is_dir():
            continue
        for topic in sorted(section.iterdir()):
            if not topic.is_dir() or not TOPIC_RE.match(topic.name):
                continue

            readme = topic / "README.md"
            if not readme.exists():
                continue
            text = readme.read_text(encoding="utf-8")
            status = parse_status(text)
            if status not in {"sourced", "reviewed", "published"}:
                continue

            last = extract_simple_field(text, "Last reviewed")
            statutes = parse_list_values(extract_block(text, "Statutes"))
            cases = parse_list_values(extract_block(text, "Cases"))

            score = priority_score(last, len(statutes), len(cases), status)
            rows.append(
                {
                    "topic": topic.name,
                    "section": section.name,
                    "path": f"topics/{section.name}/{topic.name}",
                    "status": status,
                    "last_reviewed": last or "(missing)",
                    "statute_count": len(statutes),
                    "case_count": len(cases),
                    "priority_score": score,
                }
            )

    rows.sort(key=lambda x: (-x["priority_score"], x["path"]))
    return rows


def main(argv: list[str]) -> int:
    fmt = "text"
    next_n = 20

    if "--format" in argv:
        i = argv.index("--format")
        if i + 1 < len(argv):
            fmt = argv[i + 1]

    if "--next" in argv:
        i = argv.index("--next")
        if i + 1 < len(argv):
            next_n = int(argv[i + 1])

    rows = scan()
    output = rows[:next_n]

    if fmt == "json":
        print(json.dumps(output, indent=2))
        return 0

    print(f"Staleness queue: showing {len(output)} of {len(rows)}")
    for row in output:
        print(
            f"  {row['path']:<90} score={row['priority_score']:6.2f} "
            f"status={row['status']:<9} last={row['last_reviewed']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
