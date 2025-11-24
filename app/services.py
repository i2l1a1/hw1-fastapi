from __future__ import annotations

from typing import Optional

from app.question import Question
from app.repository import QuestionRepository
from app.schemas import QuestionCreate, QuestionRead


class QuestionService:
    def __init__(self, repo: Optional[QuestionRepository] = None):
        self.repo = repo or QuestionRepository()

    def create_question(self, payload: QuestionCreate) -> QuestionRead:
        # Здесь можно добавить логирование и метрики для отслеживания количества вызовов или ошибок
        question = Question(title=payload.title.strip(), body=payload.body or "")
        # Здесь можно добавить логирование или метрики для отслеживания времени выполнения
        saved = self.repo.create(question)
        if saved.id is None:
            raise ValueError("Question must have id after save")
        return QuestionRead(id=saved.id, title=saved.title, body=saved.body)

    def get_question(self, qid: int) -> Optional[QuestionRead]:
        # Здесь можно добавить логирование и метрики для отслеживания количества вызовов или ошибок
        q = self.repo.get(qid)
        if q is None:
            # Здесь можно добавить логирование (будет записываться, если вопрос не найден)
            return None
        if q.id is None:
            raise ValueError("Question must have id")
        return QuestionRead(id=q.id, title=q.title, body=q.body)


def get_question_service() -> QuestionService:
    return QuestionService()
