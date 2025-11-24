import unittest

from app import db as db_module


class FakeSession:
    def __init__(self):
        self.closed = False

    def close(self):
        self.closed = True


class TestDB(unittest.TestCase):
    def test_get_db_returns_session_and_closes_it(self):
        fake_session = FakeSession()  # фейковая сессия

        def fake_session_local():
            return fake_session

        original_session_local = db_module.SessionLocal  # сохраняем ссылку на реальную сессию
        db_module.SessionLocal = fake_session_local  # подменяем SessionLocal на фейковую сессию

        try:
            generator = db_module.get_db()  # вызываем генератор
            session_from_generator = next(generator)  # получаем сессию из yield
            self.assertIs(session_from_generator, fake_session)  # убеждаемся, что пришла именно фейковая сессия

            with self.assertRaises(StopIteration):
                next(generator)  # второй next() нужен, чтобы генератор завершился и вызвал close()
        finally:
            db_module.SessionLocal = original_session_local  # возвращаем настоящую сессию

        self.assertTrue(fake_session.closed)  # проверяем, что close() сработал
