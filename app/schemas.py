from pydantic import BaseModel, Field
from typing import Optional


class QuestionCreate(BaseModel):
    title: str
    body: str


class QuestionRead(BaseModel):
    id: int
    title: str
    body: str
