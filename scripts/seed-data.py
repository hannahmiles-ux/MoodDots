#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
import random

from mooddots.storage import Storage, MoodEntry

root = Path.cwd()
store = Storage(root)
store.init()

start = datetime(2024, 6, 1)
for i in range(7):
    ts = start + timedelta(days=i, hours=random.randint(9, 22), minutes=random.randint(0, 59))
    store.append(MoodEntry(timestamp=ts, mood=random.randint(2, 5), note="seed"))

print("seeded")

