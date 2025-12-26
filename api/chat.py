from fastapi import APIRouter, HTTPException
from services.rag import ask_rag
from services.general_llm import ask_general_llm
from services.intent_router import detect_intent
from services.tool_router import select_tool,execute_tool
from services.tool_registry import TOOLS


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
        print("Detected intent:", intent)

        # 🔵 RAG
        if intent == "rag":
            return ask_rag(question=question, session_id=session_id)

        # 🟡 TOOL
        if intent == "tool":
            tool_result = execute_tool(question)
            print("Tool result:", tool_result)
            if tool_result:
                return tool_result
            else:
                return {
                    "answer": "Tool could not process the request.",
                    "sources": []
                }
        else:
           answer = ask_general_llm(question,session_id)
           return answer
        
    except Exception as e:
        return {
            "answer": f"Internal error: {str(e)}",
            "sources": []
        }

   
  