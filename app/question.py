from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Question:
    title: str
    body: str = ""
    id: int | None = None
