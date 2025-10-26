from app.repository import QuestionRepository
from app.question import Question
from app.schemas import QuestionCreate, QuestionRead


class QuestionService:
    def __init__(self, repo: QuestionRepository = None):
        self.repo = repo or QuestionRepository()

    def create_question(self, payload: QuestionCreate):
        # Здесь можно добавить логирование и метрики для отслеживания количества вызовов или ошибок
        question = Question(title=payload.title.strip(), body=payload.body or "")
        # Здесь можно добавить логирование или метрики для отслеживания времени выполнения
        saved = self.repo.create(question)
        return QuestionRead(id=saved.id, title=saved.title, body=saved.body)

    def get_question(self, qid):
        # Здесь можно добавить логирование и метрики для отслеживания количества вызовов или ошибок
        q = self.repo.get(qid)
        if q is None:
            # Здесь можно добавить логирование (будет записываться, если вопрос не найден)
            return None
        return QuestionRead(id=q.id, title=q.title, body=q.body)


def get_question_service():
    return QuestionService()
