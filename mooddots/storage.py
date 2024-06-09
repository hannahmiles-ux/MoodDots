from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import csv


@dataclass
class MoodEntry:
    timestamp: datetime
    mood: int
    note: str = ""

    def to_row(self) -> list[str]:
        return [self.timestamp.replace(tzinfo=timezone.utc).isoformat(), str(self.mood), self.note]


class Storage:
    def __init__(self, root: Path):
        self.root = root
        self.data_file = self.root / "data" / "moods.csv"

    def init(self) -> None:
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.data_file.exists():
            with self.data_file.open("w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "mood", "note"])

    def append(self, entry: MoodEntry) -> None:
        self.init()
        with self.data_file.open("a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(entry.to_row())

    def read_all(self) -> list[MoodEntry]:
        if not self.data_file.exists():
            return []
        entries: list[MoodEntry] = []
        with self.data_file.open("r", newline="") as f:
            rdr = csv.DictReader(f)
            for row in rdr:
                try:
                    ts = datetime.fromisoformat(row["timestamp"])  # type: ignore[arg-type]
                    mood = int(row["mood"])  # type: ignore[arg-type]
                    note = row.get("note", "") or ""
                    entries.append(MoodEntry(ts, mood, note))
                except Exception:
                    # Skip malformed rows silently for now
                    continue
        return entries

