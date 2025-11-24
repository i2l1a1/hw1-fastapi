import unittest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base, get_db
from app.api import get_service
from main import app

TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(bind=engine)
        cls.client = TestClient(app)

    def test_create_question_api(self):
        resp = self.client.post("/api/questions", json={"title": "Test", "body": "Body"})
        self.assertEqual(resp.status_code, 201)
        data = resp.json()
        self.assertEqual(data["title"], "Test")
        self.assertEqual(data["body"], "Body")

    def test_get_not_found(self):
        resp = self.client.get("/api/questions/9999")
        self.assertEqual(resp.status_code, 404)

    def test_get_existing_question(self):
        created = self.client.post("/api/questions", json={"title": "Keep", "body": "Me"}).json()
        resp = self.client.get(f"/api/questions/{created['id']}")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["id"], created["id"])
        self.assertEqual(data["title"], "Keep")
        self.assertEqual(data["body"], "Me")
