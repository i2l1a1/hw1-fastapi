from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas import QuestionCreate, QuestionRead
from app.services import QuestionService, get_question_service

router = APIRouter()


def get_service() -> QuestionService:
    return get_question_service()


@router.post(
    "/questions", response_model=QuestionRead, status_code=status.HTTP_201_CREATED
)
def create_question(
    payload: QuestionCreate, service: QuestionService = Depends(get_service)
):
    try:
        created = service.create_question(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return created


@router.get("/questions/{question_id}", response_model=QuestionRead)
def read_question(question_id: int, service: QuestionService = Depends(get_service)):
    q = service.get_question(question_id)
    if q is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return q
