from __future__ import annotations

import csv
import json
from pathlib import Path
from .storage import Storage


def export_csv(root: Path) -> str:
    store = Storage(root)
    store.init()
    return str(store.data_file)


def export_json(root: Path) -> str:
    store = Storage(root)
    rows = [
        {
            "timestamp": e.timestamp.isoformat(),
            "mood": e.mood,
            "note": e.note,
        }
        for e in store.read_all()
    ]
    out = root / "data" / "moods.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rows, indent=2))
    return str(out)

