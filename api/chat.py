from fastapi import APIRouter, HTTPException
from services.rag import ask_rag


router = APIRouter()


@router.post("/chat")
async def chat(payload: dict):
    session_id = payload.get("session_id")
    question = payload.get("question")

    if not session_id or not question:
        raise HTTPException(
            status_code=400,
            detail="session_id and question are required"
        )

    try:
        answer = ask_rag(question=question, session_id=session_id)
        return answer

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
