"""Export API-ready queue + index bundle artifacts.

Outputs:
  docs/indexes/queue.json
  docs/indexes/*.json (via build_indexes.py)

Usage:
  python scripts/export_api_bundle.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_DIR = ROOT / "docs" / "indexes"


def run(command: list[str]) -> None:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"Command failed ({' '.join(command)}):\n{result.stdout}\n{result.stderr}".strip()
        )


def main() -> int:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)

    run([sys.executable, "scripts/build_indexes.py", "--status", "sourced"])

    result = subprocess.run(
        [sys.executable, "scripts/generate_queue.py", "--format", "json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        return 1

    queue = json.loads(result.stdout)
    (INDEX_DIR / "queue.json").write_text(json.dumps(queue, indent=2) + "\n", encoding="utf-8")

    print("API bundle export complete")
    print(f"  queue: {INDEX_DIR.relative_to(ROOT) / 'queue.json'}")
    print(f"  indexes: {INDEX_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
