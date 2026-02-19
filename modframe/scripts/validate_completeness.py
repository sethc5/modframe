"""Validate module completeness across all topic folders.

Reads rules from docs/schemas/outline_schema.json and docs/schemas/readme_schema.json.
Edit those files to change what counts as complete — no Python edits needed.

Checks each topic for:
  - README.md: required fields present, Status is a known value
  - outline.md: all required headings present
  - outline.md: fewer than N placeholder strings (not a template stub)
  - outline.md: at least min_claim_labels labeled claims [Observed/Inferred/Hypothesis]
  - outline.md: at least sources_min_entries real source entries in Suggested sources
  - outline.md: actors section meets actors_min_words word count

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
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
CLAIM_LABEL_RE = re.compile(r"\[(Observed|Inferred|Hypothesis)")
YM_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")


def has_list_block(text: str, key: str) -> bool:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == f"{key}:":
            for nxt in lines[i + 1 : i + 8]:
                if not nxt.strip():
                    continue
                return nxt.lstrip().startswith("-")
    return False


def load_schemas() -> tuple[dict, dict]:
    outline = json.loads((SCHEMAS / "outline_schema.json").read_text())
    readme = json.loads((SCHEMAS / "readme_schema.json").read_text())
    return outline, readme


def extract_section(text: str, heading_keyword: str) -> str:
    """Return the body of the first heading matching keyword, up to the next heading
    at the same or higher level. Returns empty string if the heading is not found."""
    lines = text.split("\n")
    in_section = False
    section_level = 0
    collected: list[str] = []

    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            level = len(m.group(1))
            heading_text = m.group(2)
            if in_section and level <= section_level:
                break
            if heading_keyword.lower() in heading_text.lower():
                in_section = True
                section_level = level
        elif in_section:
            collected.append(line)

    return "\n".join(collected)


def check_readme(path: Path, schema: dict) -> list[str]:
    issues = []
    text = path.read_text()
    status_value = ""

    for field in schema["required_fields"]:
        pattern = re.compile(rf"^{re.escape(field)}:\s*(.+)$", re.MULTILINE)
        m = pattern.search(text)
        if not m:
            issues.append(f"README.md: missing '{field}' field")
        elif field == "Status":
            value = m.group(1).strip().lower()
            status_value = value
            if value not in schema["valid_statuses"]:
                valid = ", ".join(schema["valid_statuses"])
                issues.append(f"README.md: Status '{value}' not in [{valid}]")

    # Metadata checks for sourced+ states
    meta_cfg = schema.get("metadata_fields", {})
    required_for = set(meta_cfg.get("required_for_statuses", []))
    if status_value in required_for:
        rel_match = re.search(r"^Related modules:\s*(.+)$", text, re.MULTILINE)
        if not rel_match:
            issues.append("README.md: missing 'Related modules' field")
        else:
            ids = [x.strip() for x in rel_match.group(1).split(",") if x.strip()]
            if not ids or not all(re.fullmatch(r"\d{3}", x) for x in ids):
                issues.append("README.md: invalid 'Related modules' format (expected 001, 013, 017)")

        rev_match = re.search(r"^Last reviewed:\s*(.+)$", text, re.MULTILINE)
        if not rev_match:
            issues.append("README.md: missing 'Last reviewed' field")
        elif not YM_RE.match(rev_match.group(1).strip()):
            issues.append("README.md: invalid 'Last reviewed' format (expected YYYY-MM)")

        for key in ("Actors", "Statutes", "Cases"):
            if not has_list_block(text, key):
                issues.append(f"README.md: missing or invalid '{key}' list block")

    return issues


def check_outline(path: Path, schema: dict) -> list[str]:
    issues = []
    text = path.read_text()
    targets = schema.get("word_count_targets", {})

    # Required headings
    headings = [m.group(2).strip() for m in HEADING_RE.finditer(text)]
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

    # Claim label count
    min_labels = schema.get("min_claim_labels", 0)
    if min_labels:
        label_count = len(CLAIM_LABEL_RE.findall(text))
        if label_count < min_labels:
            issues.append(
                f"outline.md: {label_count} claim label(s) found "
                f"([Observed]/[Inferred]/[Hypothesis]), need \u2265 {min_labels}"
            )

    # Source entry count (non-placeholder bullets in Suggested sources)
    min_sources = targets.get("sources_min_entries", 0)
    if min_sources:
        sources_text = extract_section(text, "Suggested sources")
        real_sources = [
            ln.strip()
            for ln in sources_text.split("\n")
            if ln.strip().startswith("-")
            and not any(p in ln for p in schema["template_placeholders"])
        ]
        if len(real_sources) < min_sources:
            issues.append(
                f"outline.md: {len(real_sources)} source entry(ies) in "
                f"Suggested sources, need \u2265 {min_sources}"
            )

    # Actors section word count
    min_actor_words = targets.get("actors_min_words", 0)
    if min_actor_words:
        actors_text = extract_section(text, "Actors and roles")
        word_count = len(actors_text.split())
        if word_count < min_actor_words:
            issues.append(
                f"outline.md: Actors and roles section has {word_count} word(s), "
                f"need \u2265 {min_actor_words}"
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
