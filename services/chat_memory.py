# Simple in-memory chat store
# session_id -> list of messages

MAX_TURNS = 3  # last 3 Q&A pairs = 6 messages

CHAT_MEMORY = {}


def get_history(session_id: str) -> list[dict]:
    """
    Get chat history for a session.
    Returns list of {role, content}.
    """
    return CHAT_MEMORY.get(session_id, [])



def add_user_and_assistant_message(session_id: str, user_msg: str, assistant_msg: str):
    """
    Add a user + assistant turn to memory
    and trim old history.
    """
    history = CHAT_MEMORY.get(session_id, [])

    history.append({"role": "user", "content": user_msg})
    history.append({"role": "assistant", "content": assistant_msg})

    # keep only last MAX_TURNS * 2 messages
    max_messages = MAX_TURNS * 2
    if len(history) > max_messages:
        history = history[-max_messages:]

    CHAT_MEMORY[session_id] = history