from app.db import SessionLocal, QuestionModel
from app.question import Question


class QuestionRepository:
    def __init__(self, db_session=None):
        self.db = db_session or SessionLocal()

    def create(self, question: Question) -> Question:
        # Здесь можно добавить логирование
        db_q = QuestionModel(title=question.title, body=question.body)
        self.db.add(db_q)
        self.db.commit()
        self.db.refresh(db_q)
        # Здесь можно добавить логирование успешного создания и метрики времени выполнения
        return Question(id=db_q.id, title=db_q.title, body=db_q.body)

    def get(self, qid: int):
        # Здесь можно добавить логирование запроса к базе данных
        q = self.db.query(QuestionModel).filter(QuestionModel.id == qid).first()
        if q is None:
            # Здесь можно добавить логирование (если вопрос не найден)
            return None
        return Question(id=q.id, title=q.title, body=q.body)
