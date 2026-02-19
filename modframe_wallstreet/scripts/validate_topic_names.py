from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / "topics"

SECTION_RE = re.compile(r"^\d{2}_[A-Za-z0-9-]+(?:_[A-Za-z0-9-]+)*$")
TOPIC_RE = re.compile(r"^(\d{3})_[A-Za-z0-9-]+(?:_[A-Za-z0-9-]+)*$")


def main() -> int:
    if not TOPICS.exists():
        print("ERROR: topics directory not found")
        return 1

    section_dirs = sorted([p for p in TOPICS.iterdir() if p.is_dir()])
    errors: list[str] = []
    topic_ids: list[int] = []

    for section in section_dirs:
        if not SECTION_RE.match(section.name):
            errors.append(f"Invalid section folder name: {section.name}")

        for topic in sorted([p for p in section.iterdir() if p.is_dir()]):
            match = TOPIC_RE.match(topic.name)
            if not match:
                errors.append(f"Invalid topic folder name: {section.name}/{topic.name}")
                continue
            topic_ids.append(int(match.group(1)))

    if topic_ids:
        duplicates = sorted({n for n in topic_ids if topic_ids.count(n) > 1})
        if duplicates:
            errors.append(f"Duplicate topic IDs: {duplicates}")

        expected = set(range(min(topic_ids), max(topic_ids) + 1))
        missing = sorted(expected.difference(topic_ids))
        if missing:
            errors.append(f"Missing topic IDs: {missing[:20]}{'...' if len(missing) > 20 else ''}")

    if errors:
        print("Topic naming validation FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Topic naming validation PASSED")
    print(f"Sections: {len(section_dirs)}")
    print(f"Topics: {len(topic_ids)}")
    print(f"ID range: {min(topic_ids) if topic_ids else 0}-{max(topic_ids) if topic_ids else 0}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
