"""Suggest related modules using metadata overlap + lexical similarity.

Usage:
  python scripts/suggest_related_modules.py --topic 020
  python scripts/suggest_related_modules.py --topic 020 --top 6 --format json
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / "topics"
TOPIC_RE = re.compile(r"^(\d{3})_(.+)$")
STATUS_RE = re.compile(r"^Status:\s*(.+)$", re.MULTILINE)
WORD_RE = re.compile(r"[a-z]{3,}")


class Module:
    def __init__(self, topic_id: str, topic_name: str, path: str, status: str, actors: set[str], legal: set[str], text_tokens: set[str]):
        self.topic_id = topic_id
        self.topic_name = topic_name
        self.path = path
        self.status = status
        self.actors = actors
        self.legal = legal
        self.text_tokens = text_tokens


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
    out = []
    for line in block_lines:
        s = line.strip()
        if s.startswith("-"):
            out.append(s[1:].strip())
    return [x for x in out if x]


def parse_actors(block_lines: list[str]) -> set[str]:
    out: set[str] = set()
    current: dict[str, str] = {}
    for raw in block_lines + ["- END"]:
        line = raw.strip()
        if line.startswith("-"):
            if current.get("name"):
                out.add(current["name"].lower())
            current = {}
            payload = line[1:].strip()
            if ":" in payload:
                k, v = payload.split(":", 1)
                current[k.strip()] = v.strip()
        elif ":" in line:
            k, v = line.split(":", 1)
            current[k.strip()] = v.strip()
    return out


def parse_status(text: str) -> str:
    m = STATUS_RE.search(text)
    return m.group(1).strip().lower() if m else "unknown"


def tokenize(text: str) -> set[str]:
    return set(WORD_RE.findall(text.lower()))


def load_modules() -> dict[str, Module]:
    mods: dict[str, Module] = {}
    for section in sorted(TOPICS.iterdir()):
        if not section.is_dir():
            continue
        for topic in sorted(section.iterdir()):
            if not topic.is_dir():
                continue
            m = TOPIC_RE.match(topic.name)
            if not m:
                continue
            topic_id = m.group(1)
            topic_name = m.group(2).replace("_", " ")

            readme = topic / "README.md"
            outline = topic / "outline.md"
            if not readme.exists() or not outline.exists():
                continue

            readme_text = readme.read_text(encoding="utf-8")
            outline_text = outline.read_text(encoding="utf-8")
            status = parse_status(readme_text)

            actors = parse_actors(extract_block(readme_text, "Actors"))
            statutes = set(x.lower() for x in parse_list_values(extract_block(readme_text, "Statutes")))
            cases = set(x.lower() for x in parse_list_values(extract_block(readme_text, "Cases")))
            legal = statutes | cases
            tokens = tokenize(topic_name + "\n" + outline_text[:3000])

            mods[topic_id] = Module(
                topic_id=topic_id,
                topic_name=topic_name,
                path=f"topics/{section.name}/{topic.name}",
                status=status,
                actors=actors,
                legal=legal,
                text_tokens=tokens,
            )
    return mods


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def score(base: Module, candidate: Module) -> dict:
    actor_overlap = len(base.actors & candidate.actors)
    legal_overlap = len(base.legal & candidate.legal)
    lexical = jaccard(base.text_tokens, candidate.text_tokens)

    total = (actor_overlap * 4.0) + (legal_overlap * 5.0) + (lexical * 8.0)
    return {
        "topic_id": candidate.topic_id,
        "topic_name": candidate.topic_name,
        "path": candidate.path,
        "score": round(total, 3),
        "actor_overlap": actor_overlap,
        "legal_overlap": legal_overlap,
        "lexical_similarity": round(lexical, 4),
    }


def main(argv: list[str]) -> int:
    if "--topic" not in argv:
        print("ERROR: pass --topic NNN", file=sys.stderr)
        return 1

    i = argv.index("--topic")
    if i + 1 >= len(argv):
        print("ERROR: missing topic id", file=sys.stderr)
        return 1
    topic_id = argv[i + 1].zfill(3)

    top_n = 6
    if "--top" in argv:
        j = argv.index("--top")
        if j + 1 < len(argv):
            top_n = int(argv[j + 1])

    fmt = "text"
    if "--format" in argv:
        j = argv.index("--format")
        if j + 1 < len(argv):
            fmt = argv[j + 1]

    mods = load_modules()
    if topic_id not in mods:
        print(f"ERROR: topic {topic_id} not found", file=sys.stderr)
        return 1

    base = mods[topic_id]
    scored = [score(base, m) for tid, m in mods.items() if tid != topic_id]
    scored.sort(key=lambda x: (-x["score"], x["topic_id"]))
    top = scored[:top_n]

    if fmt == "json":
        print(json.dumps(top, indent=2))
        return 0

    ids = ", ".join(item["topic_id"] for item in top)
    print(f"Topic {topic_id}: {base.topic_name}")
    print(f"Suggested related modules ({len(top)}): {ids}")
    for item in top:
        print(
            f"  [{item['topic_id']}] {item['topic_name'][:40]:<40} "
            f"score={item['score']:.3f} actors={item['actor_overlap']} legal={item['legal_overlap']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
