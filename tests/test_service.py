import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db import Base
from app.repository import QuestionRepository
from app.schemas import QuestionCreate
from app.services import QuestionService

TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class TestService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(bind=engine)
        cls.db = TestingSessionLocal()
        cls.repo = QuestionRepository(cls.db)
        cls.service = QuestionService(cls.repo)

    def test_create_and_get_question(self):
        q = self.service.create_question(QuestionCreate(title="Title", body="Body"))
        self.assertEqual(q.title, "Title")
        self.assertEqual(q.body, "Body")

        fetched = self.service.get_question(q.id)
        self.assertEqual(fetched.id, q.id)
        self.assertEqual(fetched.title, q.title)
        self.assertEqual(fetched.body, q.body)
