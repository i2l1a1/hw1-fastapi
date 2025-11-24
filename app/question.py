from dataclasses import dataclass


@dataclass
class Question:
    title: str
    body: str = None
    id: int = None
