from services.rag import ask_rag

def test_rag():
    session_id = "test-session-123"
    question = "What is the late arrival policy?"

    answer = ask_rag(question, session_id)

    print("Answer:")
    print(answer)


if __name__ == "__main__":
    test_rag()


# python -m test.rag_test
