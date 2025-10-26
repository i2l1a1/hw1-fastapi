from dataclasses import dataclass
from typing import Optional


@dataclass
class Question:
    title: str
    body: str = None
    id: int = None
