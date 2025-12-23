from fastapi import APIRouter, HTTPException
from services.rag import summarize_documents

router = APIRouter()

@router.post("/summary")
async def summarize(payload: dict):
    session_id = payload.get("session_id")

    if not session_id:
        raise HTTPException(
            status_code=400,
            detail="session_id is required"
        )
    
    try:
        summary = summarize_documents(session_id=session_id)
        return summary
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )