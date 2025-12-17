import streamlit as st
import requests

# ================= CONFIG =================
BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Document Chat (RAG)",
    layout="centered"
)

# ================= SESSION STATE =================
if "session_id" not in st.session_state:
    st.session_state.session_id = None

# ================= UI HEADER =================
st.title("📄 AI Document Chat")
st.write("Upload documents and ask questions using RAG")

# ================= FILE UPLOAD =================
st.subheader("Upload Documents")

uploaded_files = st.file_uploader(
    "Choose PDF or DOCX files",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if st.button("Upload"):
    if not uploaded_files:
        st.warning("Please upload at least one file")
    else:
        with st.spinner("Uploading and processing documents..."):
            files = []
            for file in uploaded_files:
                files.append(
                    ("files", (file.name, file.getvalue(), file.type))
                )

            response = requests.post(
                f"{BACKEND_URL}/upload/",
                files=files
            )

            if response.status_code == 200:
                data = response.json()
                st.session_state.session_id = data["session_id"]

                st.success("Documents uploaded successfully!")
                st.write("Session ID:", st.session_state.session_id)

                st.write("Uploaded files:")
                for f in uploaded_files:
                    st.write("•", f.name)
            else:
                st.error("Upload failed")

# ================= CHAT SECTION =================
st.divider()
st.subheader("Chat")

if st.session_state.session_id is None:
    st.info("Upload documents first to start chatting")
else:
    question = st.text_input("Ask a question from your documents")

    if st.button("Ask"):
        if not question.strip():
            st.warning("Please enter a question")
        else:
            with st.spinner("Thinking..."):
                payload = {
                    "session_id": st.session_state.session_id,
                    "question": question
                }

                response = requests.post(
                    f"{BACKEND_URL}/api/chat",
                    json=payload
                )

                if response.status_code == 200:
                    answer = response.json()["answer"]
                    st.markdown("### 🤖 Answer")
                    st.write(answer)
                else:
                    st.error("Error getting answer")
