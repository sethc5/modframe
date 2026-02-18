"""Validate module completeness across all topic folders.

Reads rules from docs/schemas/outline_schema.json and docs/schemas/readme_schema.json.
Edit those files to change what counts as complete — no Python edits needed.

Checks each topic for:
  - README.md: required fields present, Status is a known value
  - outline.md: all required headings present
  - outline.md: fewer than N placeholder strings (not a template stub)

Exit codes:
  0  all modules pass (or --warn-only mode)
  1  one or more failures

Usage:
  python scripts/validate_completeness.py
  python scripts/validate_completeness.py --warn-only    # exit 0 even on failures
  python scripts/validate_completeness.py --stats-only   # print summary, no per-module detail
  python scripts/validate_completeness.py --status draft # filter to one lifecycle state
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / "topics"
SCHEMAS = ROOT / "docs" / "schemas"

TOPIC_RE = re.compile(r"^\d{3}_")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+)$", re.MULTILINE)


def load_schemas() -> tuple[dict, dict]:
    outline = json.loads((SCHEMAS / "outline_schema.json").read_text())
    readme = json.loads((SCHEMAS / "readme_schema.json").read_text())
    return outline, readme


def check_readme(path: Path, schema: dict) -> list[str]:
    issues = []
    text = path.read_text()

    for field in schema["required_fields"]:
        pattern = re.compile(rf"^{re.escape(field)}:\s*(.+)$", re.MULTILINE)
        m = pattern.search(text)
        if not m:
            issues.append(f"README.md: missing '{field}' field")
        elif field == "Status":
            value = m.group(1).strip().lower()
            if value not in schema["valid_statuses"]:
                valid = ", ".join(schema["valid_statuses"])
                issues.append(f"README.md: Status '{value}' not in [{valid}]")

    return issues


def check_outline(path: Path, schema: dict) -> list[str]:
    issues = []
    text = path.read_text()

    # Required headings
    headings = [m.group(1).strip() for m in HEADING_RE.finditer(text)]
    for required in schema["required_headings"]:
        if not any(required.lower() in h.lower() for h in headings):
            issues.append(f"outline.md: missing heading matching '{required}'")

    # Placeholder detection
    hits = [s for s in schema["template_placeholders"] if s in text]
    threshold = schema.get("placeholder_hit_threshold", 3)
    if len(hits) >= threshold:
        issues.append(
            f"outline.md: {len(hits)} template placeholder(s) still present "
            f"(threshold: {threshold})"
        )

    return issues


def get_status(readme_path: Path, schema: dict) -> str:
    if not readme_path.exists():
        return "unknown"
    text = readme_path.read_text()
    m = re.search(r"^Status:\s*(.+)$", text, re.MULTILINE)
    if not m:
        return "unknown"
    value = m.group(1).strip().lower()
    return value if value in schema["valid_statuses"] else "unknown"


def main(argv: list[str]) -> int:
    warn_only = "--warn-only" in argv
    stats_only = "--stats-only" in argv
    status_filter = None
    if "--status" in argv:
        idx = argv.index("--status")
        if idx + 1 < len(argv):
            status_filter = argv[idx + 1]

    try:
        outline_schema, readme_schema = load_schemas()
    except FileNotFoundError as e:
        print(f"ERROR: schema file not found: {e}")
        return 1

    results = []
    failures = []

    for section in sorted(TOPICS.iterdir()):
        if not section.is_dir():
            continue
        for topic in sorted(section.iterdir()):
            if not topic.is_dir() or not TOPIC_RE.match(topic.name):
                continue

            readme = topic / "README.md"
            outline = topic / "outline.md"
            status = get_status(readme, readme_schema)

            if status_filter and status != status_filter:
                continue

            issues = []
            if not readme.exists():
                issues.append("README.md: file missing")
            else:
                issues.extend(check_readme(readme, readme_schema))

            if not outline.exists():
                issues.append("outline.md: file missing")
            else:
                issues.extend(check_outline(outline, outline_schema))

            record = {
                "path": f"{section.name}/{topic.name}",
                "status": status,
                "issues": issues,
            }
            results.append(record)
            if issues:
                failures.append(record)

    # Summary
    total = len(results)
    clean = total - len(failures)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1

    print(f"Module completeness: {total} topics checked")
    print(f"  Clean:      {clean}")
    print(f"  With issues:{len(failures)}")
    print("Status breakdown:")
    for s in readme_schema["valid_statuses"] + ["unknown"]:
        count = by_status.get(s, 0)
        if count:
            print(f"  {s:<12} {count}")

    if not stats_only and failures:
        limit = 50
        print(f"\nIssues (showing up to {limit} of {len(failures)}):")
        for rec in failures[:limit]:
            print(f"\n  {rec['path']}")
            for issue in rec["issues"]:
                print(f"    - {issue}")
        if len(failures) > limit:
            print(f"  ... and {len(failures) - limit} more")

    if failures and not warn_only and not stats_only:
        print("\nFAILED — use --warn-only to treat as warning during rollout")
        return 1

    if warn_only and failures:
        print("\nWARNING: issues found (--warn-only, not failing build)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
