from fastapi import APIRouter, HTTPException
from services.rag import ask_rag
from services.general_llm import ask_general_llm
from services.intent_router import detect_intent


router = APIRouter()


@router.post("/chat")
async def chat(payload: dict):
    session_id = payload.get("session_id") or "general"

    question = payload.get("question")

    if not session_id or not question:
        raise HTTPException(
            status_code=400,
            detail="session_id and question are required"
        )
    try:
        intent = detect_intent(question)

        if intent == "rag":
           answer = ask_rag(question=question, session_id=session_id)
           return answer
        elif intent == "general":
           answer = ask_general_llm(question,session_id)
           return answer
        else:
           answer = ask_general_llm(question,session_id)
           return answer
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

   
  