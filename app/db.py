from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import (
    DeclarativeMeta,
    declarative_base,
    scoped_session,
    sessionmaker,
)

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base: DeclarativeMeta = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class QuestionModel(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(), nullable=False)
    body = Column(Text, nullable=True)


def init_db(bind_engine=None):
    e = bind_engine or engine
    Base.metadata.create_all(bind=e)
