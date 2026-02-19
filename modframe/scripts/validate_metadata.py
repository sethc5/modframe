"""Validate module README metadata fields.

Checks metadata readiness for machine-index and graph builds.

Usage:
  python scripts/validate_metadata.py
  python scripts/validate_metadata.py --warn-only
  python scripts/validate_metadata.py --status sourced
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / "topics"
SCHEMAS = ROOT / "docs" / "schemas"

TOPIC_RE = re.compile(r"^(\d{3})_(.+)$")
STATUS_RE = re.compile(r"^Status:\s*(.+)$", re.MULTILINE)
FIELD_RE = re.compile(r"^(Related modules|Last reviewed):\s*(.*)$", re.MULTILINE)
YM_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
ID_RE = re.compile(r"^\d{3}$")


def load_schema() -> dict:
    return json.loads((SCHEMAS / "readme_schema.json").read_text())


def parse_status(text: str, valid_statuses: list[str]) -> str:
    m = STATUS_RE.search(text)
    if not m:
        return "unknown"
    value = m.group(1).strip().lower()
    return value if value in valid_statuses else "unknown"


def parse_simple_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for m in FIELD_RE.finditer(text):
        fields[m.group(1)] = m.group(2).strip()
    return fields


def has_list_block(text: str, key: str) -> bool:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == f"{key}:":
            for nxt in lines[i + 1 : i + 8]:
                if not nxt.strip():
                    continue
                return nxt.lstrip().startswith("-")
    return False


def validate_readme(path: Path, schema: dict, status_filter: str | None) -> tuple[str, list[str]]:
    text = path.read_text(encoding="utf-8")
    valid_statuses = schema["valid_statuses"]
    meta_cfg = schema.get("metadata_fields", {})
    required_for = set(meta_cfg.get("required_for_statuses", []))

    status = parse_status(text, valid_statuses)
    if status_filter and status != status_filter:
        return status, []

    issues: list[str] = []
    if status in required_for:
        fields = parse_simple_fields(text)

        related = fields.get("Related modules", "")
        if not related:
            issues.append("missing 'Related modules' field")
        else:
            tokens = [x.strip() for x in related.split(",") if x.strip()]
            if not tokens or not all(ID_RE.match(t) for t in tokens):
                issues.append("invalid 'Related modules' format (expected: 001, 013, 017)")

        reviewed = fields.get("Last reviewed", "")
        if not reviewed:
            issues.append("missing 'Last reviewed' field")
        elif not YM_RE.match(reviewed):
            issues.append("invalid 'Last reviewed' format (expected YYYY-MM)")

        for key in ("Actors", "Statutes", "Cases"):
            if not has_list_block(text, key):
                issues.append(f"missing or invalid '{key}' list block")

    return status, issues


def main(argv: list[str]) -> int:
    warn_only = "--warn-only" in argv
    status_filter = None
    if "--status" in argv:
        i = argv.index("--status")
        if i + 1 < len(argv):
            status_filter = argv[i + 1]

    schema = load_schema()
    failures: list[tuple[str, str, list[str]]] = []
    checked = 0

    for section in sorted(TOPICS.iterdir()):
        if not section.is_dir():
            continue
        for topic in sorted(section.iterdir()):
            if not topic.is_dir() or not TOPIC_RE.match(topic.name):
                continue
            readme = topic / "README.md"
            if not readme.exists():
                continue

            status, issues = validate_readme(readme, schema, status_filter)
            if status_filter and status != status_filter:
                continue

            checked += 1
            if issues:
                failures.append((f"{section.name}/{topic.name}", status, issues))

    print(f"Metadata validation: {checked} topics checked")
    print(f"  Clean:      {checked - len(failures)}")
    print(f"  With issues:{len(failures)}")

    if failures:
        limit = 50
        print(f"\nIssues (showing up to {limit} of {len(failures)}):")
        for path, status, issues in failures[:limit]:
            print(f"\n  {path} (status={status})")
            for issue in issues:
                print(f"    - {issue}")
        if len(failures) > limit:
            print(f"  ... and {len(failures) - limit} more")

    if failures and not warn_only:
        print("\nFAILED")
        return 1
    if failures and warn_only:
        print("\nWARNING: issues found (--warn-only, not failing build)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
