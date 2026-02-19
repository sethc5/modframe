"""Generate a prioritized work queue of incomplete topic modules.

Scans all topics, determines completeness from README.md Status field and
outline.md placeholder detection, then outputs a sorted queue.

Output formats:
  text  — human-readable summary (default)
  csv   — spreadsheet-ready
  json  — machine-readable

Priority ordering: incomplete topics first, sorted by topic_id ascending
(front sections = highest priority).

Usage:
  python scripts/generate_queue.py
  python scripts/generate_queue.py --next 10
  python scripts/generate_queue.py --format csv > queue.csv
  python scripts/generate_queue.py --format json > queue.json
  python scripts/generate_queue.py --status draft    # only show one state
"""

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / "topics"
SCHEMAS = ROOT / "docs" / "schemas"

TOPIC_RE = re.compile(r"^(\d{3})_(.+)$")
STATUS_RE = re.compile(r"^Status:\s*(.+)$", re.MULTILINE)

STATUS_ORDER = ["unknown", "empty", "scaffolded", "draft", "sourced", "reviewed", "published"]
DONE_STATES = {"reviewed", "published"}


def load_placeholders() -> list[str]:
    schema = json.loads((SCHEMAS / "outline_schema.json").read_text())
    return schema.get("template_placeholders", [])


def load_valid_statuses() -> list[str]:
    schema = json.loads((SCHEMAS / "readme_schema.json").read_text())
    return schema.get("valid_statuses", [])


def is_stub(outline_path: Path, placeholders: list[str], threshold: int = 3) -> bool:
    """True if outline.md appears to be an unfilled template."""
    if not outline_path.exists():
        return True
    text = outline_path.read_text()
    hits = sum(1 for p in placeholders if p in text)
    return hits >= threshold


def get_status(readme_path: Path, valid: list[str]) -> str:
    if not readme_path.exists():
        return "unknown"
    text = readme_path.read_text()
    m = STATUS_RE.search(text)
    if not m:
        return "unknown"
    value = m.group(1).strip().lower()
    return value if value in valid else "unknown"


def metadata_penalty(readme_path: Path, status: str) -> int:
    """Small queue penalty for missing machine-readable metadata on sourced+ modules."""
    if status not in {"sourced", "reviewed", "published"}:
        return 0
    if not readme_path.exists():
        return 0
    text = readme_path.read_text()

    penalty = 0
    if not re.search(r"^Related modules:\s*.+$", text, re.MULTILINE):
        penalty += 8
    if not re.search(r"^Last reviewed:\s*\d{4}-(0[1-9]|1[0-2])$", text, re.MULTILINE):
        penalty += 8
    for key in ("Actors", "Statutes", "Cases"):
        if not re.search(rf"^{key}:\s*$", text, re.MULTILINE):
            penalty += 8
    return penalty


def status_rank(status: str) -> int:
    try:
        return STATUS_ORDER.index(status)
    except ValueError:
        return 0


def completeness_score(readme_path: Path, outline_path: Path, placeholders: list[str], status: str) -> int:
    """0–100 rough completion score used for sorting within same status."""
    score = 0
    if readme_path.exists():
        text = readme_path.read_text()
        if re.search(r"^Status:", text, re.MULTILINE):
            score += 10
        if re.search(r"^Tags:", text, re.MULTILINE):
            score += 5
    if not is_stub(outline_path, placeholders):
        score += 50
    if outline_path.exists():
        text = outline_path.read_text()
        if "**Summary:**" in text and "Briefly explain" not in text:
            score += 15
        if "**Mechanism in one sentence:**" in text and "Describe the operational" not in text:
            score += 10
        if "### Suggested sources" in text and "Statutes and regulations\n" not in text:
            score += 10
    score -= metadata_penalty(readme_path, status)
    return max(0, min(score, 100))


def scan_topics(placeholders: list[str], valid_statuses: list[str]) -> list[dict]:
    rows = []
    for section in sorted(TOPICS.iterdir()):
        if not section.is_dir():
            continue
        for topic in sorted(section.iterdir()):
            if not topic.is_dir():
                continue
            m = TOPIC_RE.match(topic.name)
            if not m:
                continue

            topic_id = int(m.group(1))
            topic_name = m.group(2).replace("_", " ")
            readme = topic / "README.md"
            outline = topic / "outline.md"

            status = get_status(readme, valid_statuses)
            stub = is_stub(outline, placeholders)
            score = completeness_score(readme, outline, placeholders, status)

            rows.append({
                "topic_id": topic_id,
                "section": section.name,
                "topic_name": topic_name,
                "path": f"topics/{section.name}/{topic.name}",
                "status": status,
                "is_stub": stub,
                "completeness_pct": score,
            })
    return rows


def main(argv: list[str]) -> int:
    next_n = None
    fmt = "text"
    status_filter = None

    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--next" and i + 1 < len(argv):
            next_n = int(argv[i + 1])
            i += 2
            continue
        if arg == "--format" and i + 1 < len(argv):
            fmt = argv[i + 1]
            i += 2
            continue
        if arg == "--status" and i + 1 < len(argv):
            status_filter = argv[i + 1]
            i += 2
            continue
        i += 1

    try:
        placeholders = load_placeholders()
        valid_statuses = load_valid_statuses()
    except FileNotFoundError as e:
        print(f"ERROR: schema file not found: {e}", file=sys.stderr)
        return 1

    rows = scan_topics(placeholders, valid_statuses)

    if status_filter:
        rows = [r for r in rows if r["status"] == status_filter]

    # Sort: done topics last, incomplete sorted by (completeness asc, topic_id asc)
    incomplete = [r for r in rows if r["status"] not in DONE_STATES]
    complete = [r for r in rows if r["status"] in DONE_STATES]
    incomplete.sort(key=lambda r: (r["completeness_pct"], r["topic_id"]))
    complete.sort(key=lambda r: r["topic_id"])
    queue = incomplete + complete

    if next_n is not None:
        queue = incomplete[:next_n]

    if fmt == "json":
        print(json.dumps(queue, indent=2))
        return 0

    if fmt == "csv":
        if not queue:
            return 0
        writer = csv.DictWriter(sys.stdout, fieldnames=list(queue[0].keys()))
        writer.writeheader()
        writer.writerows(queue)
        return 0

    # Text output
    all_rows = scan_topics(placeholders, valid_statuses)
    total = len(all_rows)
    stub_count = sum(1 for r in all_rows if r["is_stub"])
    done_count = sum(1 for r in all_rows if r["status"] in DONE_STATES)
    in_progress = total - stub_count - done_count

    print(f"Work queue: {total} total topics")
    print(f"  Stub/empty:  {stub_count}")
    print(f"  In progress: {in_progress}")
    print(f"  Done:        {done_count}")
    print()

    display_limit = next_n or 20
    label = f"Next {display_limit}" if next_n else f"Top {display_limit} to work on"
    print(f"{label}:")
    for r in queue[:display_limit]:
        name = r["topic_name"][:42]
        print(
            f"  [{r['topic_id']:03d}] {name:<42}  "
            f"status={r['status']:<12}  pct={r['completeness_pct']:3d}%"
        )

    if not next_n and len(incomplete) > display_limit:
        remaining = len(incomplete) - display_limit
        print(f"  ... and {remaining} more incomplete (use --format csv/json for full list)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
