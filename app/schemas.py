from pydantic import BaseModel


class QuestionCreate(BaseModel):
    title: str
    body: str


class QuestionRead(BaseModel):
    id: int
    title: str
    body: str
