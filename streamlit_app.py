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

if "messages" not in st.session_state:
    st.session_state.messages = []
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


# ================= DOCUMENT SUMMARY =================
st.divider()
st.subheader("📑 Document Summary")

if st.session_state.session_id is None:
    st.info("Upload documents to generate summary")
else:
    if st.button("Generate Summary"):
        with st.spinner("Generating document summary..."):
            response = requests.post(
                f"{BACKEND_URL}/api/summary",
                json={"session_id": st.session_state.session_id}
            )

            if response.status_code == 200:
                data = response.json()

                st.markdown("### 📝 Summary")
                st.write(data.get("summary", "No summary available"))
            else:
                st.error("Failed to generate summary")


# # ================= CHAT SECTION =================
# st.divider()
# st.subheader("Chat")

# # Friendly helper text
# if st.session_state.session_id is None:
#     st.info("You can ask general questions. Upload documents for document-based answers.")

# question = st.text_input("Ask anything (general or document-based)")

# if st.button("Ask"):
#     if not question.strip():
#         st.warning("Please enter a question")
#     else:
#                 payload = {
#                     "session_id": st.session_state.session_id,
#                     "question": question
#                 }

#                 response = requests.post(
#                     f"{BACKEND_URL}/api/chat",
#                     json=payload
#                 )

#                 if response.status_code == 200:
#                     data = response.json()

#                     st.markdown("### 🤖 Answer")
#                     st.write(data["answer"])
                      
#                     if data.get("sources"):
#                        st.markdown("### 📄 Sources")
#                        for src in data["sources"]:
#                          st.write("•", src)
#                 else:
#                     st.error("Error getting answer")




# ================= CHAT SECTION =================
st.divider()
st.subheader("💬 Chat")

# Helper text
if st.session_state.session_id is None:
    st.info("You can ask general questions. Upload documents for document-based answers.")

# 🔁 Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 AI:** {msg['content']}")

# 🔽 Input always at bottom (FORM FIX)
with st.form(key="chat_form", clear_on_submit=True):
    question = st.text_input("Ask anything (general or document-based)")
    submitted = st.form_submit_button("Ask")

if submitted:
    if not question.strip():
        st.warning("Please enter a question")
    else:
        # 1️⃣ Add user message to history
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        payload = {
            "session_id": st.session_state.session_id,
            "question": question
        }

        with st.spinner("Thinking..."):
            response = requests.post(
                f"{BACKEND_URL}/api/chat",
                json=payload
            )

        if response.status_code == 200:
            data = response.json()

            answer = data.get("answer", "")

            # 2️⃣ Add AI response to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

            # 3️⃣ Clear input
            st.session_state.chat_input = ""

            # 4️⃣ Rerun to show updated chat
            st.rerun()

        else:
            st.error("Error getting response from AI")
