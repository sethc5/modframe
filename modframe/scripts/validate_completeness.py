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


# Regex substitutions applied before sentence splitting so that abbreviations
# like U.S.C., U.S., Pub., Inc., etc. and claim labels [Observed]/[Inferred]
# are not counted as sentence boundaries.
_ABBREV_SUBS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"U\.S\.C\."), "USC"),
    (re.compile(r"U\.S\."), "US"),
    (re.compile(r"(?<!\w)([A-Z])\.(?=[A-Z]\.)"), r"\1"),
    (
        re.compile(
            r"(?:Pub|Inc|Corp|Ltd|Jr|Sr|Dr|Mr|Mrs|Ms|Rev|Gen|Gov|Sen|Rep"
            r"|Vol|No|vs|etc|approx|est)\."
        ),
        lambda m: m.group()[:-1],
    ),
    (re.compile(r"\s*\[(Observed|Inferred|Hypothesis)(?:\s*—[^\]]+)?\]"), ""),
]


def _count_sentences(text: str) -> int:
    """Count real sentences, ignoring abbreviation dots and claim labels."""
    cleaned = text
    for pat, repl in _ABBREV_SUBS:
        cleaned = pat.sub(repl, cleaned)
    return len([s for s in re.split(r"(?<=[.!?])\s+", cleaned) if s.strip()])


def check_outline(path: Path, schema: dict, status: str = "unknown") -> list[str]:
    issues = []
    text = path.read_text()
    targets = schema.get("word_count_targets", {})
    citation_rules = schema.get("citation_rules", {})

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

        if citation_rules.get("enforce_source_entry_structure") and status in {"reviewed", "published"}:
            pattern = citation_rules.get("source_entry_regex")
            if pattern:
                source_line_re = re.compile(pattern)
                bad = [ln for ln in real_sources if not source_line_re.match(ln)]
                if bad:
                    issues.append(
                        "outline.md: one or more Suggested sources entries do not match "
                        "required format (title. issuer, date. url/id)."
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

    # Summary sentence count
    summary_min = targets.get("summary_min_sentences", 0)
    summary_max = targets.get("summary_max_sentences", 0)
    m_summary = re.search(
        r"\*\*Summary:\*\*\s*(.*?)\n\s*\*\*Mechanism in one sentence:\*\*",
        text,
        re.DOTALL,
    )
    if m_summary and (summary_min or summary_max):
        summary_text = m_summary.group(1).strip()
        sentence_count = _count_sentences(summary_text)
        if summary_min and sentence_count < summary_min:
            issues.append(
                f"outline.md: Summary has {sentence_count} sentence(s), need \u2265 {summary_min}"
            )
        if summary_max and sentence_count > summary_max:
            issues.append(
                f"outline.md: Summary has {sentence_count} sentence(s), need \u2264 {summary_max}"
            )

    # Mechanism word cap
    mechanism_max_words = targets.get("mechanism_max_words", 0)
    if mechanism_max_words:
        m_mech = re.search(r"\*\*Mechanism in one sentence:\*\*\s*(.+)", text)
        if m_mech:
            mech_text = re.sub(
                r"\s*\[(Observed|Inferred|Hypothesis)(?:\s*—[^\]]+)?\]", "",
                m_mech.group(1).strip(),
            )
            mechanism_words = len(mech_text.split())
            if mechanism_words > mechanism_max_words:
                issues.append(
                    f"outline.md: Mechanism sentence has {mechanism_words} word(s), "
                    f"need \u2264 {mechanism_max_words}"
                )

    # Process map minimum steps
    min_steps = targets.get("process_min_steps", 0)
    if min_steps:
        process_text = extract_section(text, "Process map")
        step_count = len([ln for ln in process_text.split("\n") if ln.strip().startswith("-")])
        if step_count < min_steps:
            issues.append(
                f"outline.md: Process map has {step_count} step(s), need \u2265 {min_steps}"
            )

    # Claim/source traceability enforcement for mature modules
    trace_mode = citation_rules.get("traceability_mode", "")
    if status in {"reviewed", "published"} and trace_mode == "strict-inline-or-mapping":
        has_inline = bool(re.search(r"\[Observed\s+—\s+source:\s*[^\]]+\]", text))
        has_mapping = "### Source mapping" in text
        if not has_inline and not has_mapping:
            issues.append(
                "outline.md: reviewed/published modules require claim-source traceability "
                "(inline [Observed — source: ...] or a '### Source mapping' section)"
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
                issues.extend(check_outline(outline, outline_schema, status))

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
