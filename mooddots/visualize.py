from __future__ import annotations

from typing import Iterable


def dots(moods: Iterable[int]) -> str:
    scale = {1: "·", 2: "•", 3: "○", 4: "●", 5: "⬤"}
    return " ".join(scale.get(m, "·") for m in moods)

