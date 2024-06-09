from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys

from .storage import Storage, MoodEntry


def cmd_add(args: argparse.Namespace) -> int:
    try:
        mood = int(args.value)
    except ValueError:
        print("mood must be an integer 1-5", file=sys.stderr)
        return 2
    if not (1 <= mood <= 5):
        print("mood must be between 1 and 5", file=sys.stderr)
        return 2
    note = args.note or ""
    store = Storage(Path.cwd())
    store.append(MoodEntry(timestamp=datetime.utcnow(), mood=mood, note=note))
    print("added")
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    store = Storage(Path.cwd())
    entries = store.read_all()
    if not entries:
        print("No entries yet.")
        return 0
    # Simple ASCII visualization: most recent 30 entries as dots
    last = entries[-30:]
    scale = {1: "·", 2: "•", 3: "○", 4: "●", 5: "⬤"}
    line = " ".join(scale.get(e.mood, "·") for e in last)
    print(line)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="mood", description="Minimal mood tracker")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="Add a mood entry")
    a.add_argument("value", help="Mood 1-5")
    a.add_argument("--note", help="Optional note")
    a.set_defaults(func=cmd_add)

    s = sub.add_parser("show", help="Show recent moods")
    s.set_defaults(func=cmd_show)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())

