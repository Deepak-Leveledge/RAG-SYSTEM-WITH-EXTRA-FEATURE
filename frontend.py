# import streamlit as st
# import requests

# # ================= CONFIG =================
# BACKEND_URL = "http://127.0.0.1:8000"

# st.set_page_config(
#     page_title="AI Document Chat",
#     layout="wide"
# )

# # ================= SESSION STATE =================
# if "session_id" not in st.session_state:
#     st.session_state.session_id = None

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # ================= CSS (CHATGPT STYLE + DARK/LIGHT SAFE) =================
# st.markdown("""
# <style>
# :root {
#   --bg: var(--background-color);
#   --text: var(--text-color);
#   --user-bg: #DCF8C6;
#   --ai-bg: #FFFFFF;
#   --border: rgba(0,0,0,0.15);
# }

# @media (prefers-color-scheme: dark) {
#   :root {
#     --user-bg: #2E7D32;
#     --ai-bg: #1E1E1E;
#     --border: rgba(255,255,255,0.2);
#   }
# }

# .chat-wrapper {
#     height: calc(100vh - 220px); /* 🔥 FIX: prevents chat from going off-screen */
#     display: flex;
#     flex-direction: column;
#     border-radius: 10px;
#     border: 1px solid var(--border);
#     background-color: var(--bg);
# }

# .chat-scroll {
#     flex: 1;
#     overflow-y: auto;
#     padding: 14px;
# }

# .chat-input {
#     border-top: 1px solid var(--border);
#     padding: 10px;
#     background-color: var(--bg);
# }

# .user-msg {
#     background-color: var(--user-bg);
#     color: var(--text);
#     padding: 10px 12px;
#     border-radius: 10px;
#     margin: 8px 0;
#     max-width: 75%;
#     margin-left: auto;
# }

# .ai-msg {
#     background-color: var(--ai-bg);
#     color: var(--text);
#     padding: 10px 12px;
#     border-radius: 10px;
#     margin: 8px 0;
#     max-width: 75%;
#     margin-right: auto;
# }
# </style>
# """, unsafe_allow_html=True)

# # ================= LAYOUT =================
# left, right = st.columns([3, 7], gap="large")

# # ================= LEFT PANEL (DOCUMENTS – FIXED) =================
# with left:
#     st.markdown("## 📂 Documents")

#     with st.container():
#         uploaded_files = st.file_uploader(
#             "Upload PDF or DOCX",
#             type=["pdf", "docx"],
#             accept_multiple_files=True
#         )

#         if st.button("Upload"):
#             if not uploaded_files:
#                 st.warning("Please upload at least one file")
#             else:
#                 files = [
#                     ("files", (f.name, f.getvalue(), f.type))
#                     for f in uploaded_files
#                 ]
#                 with st.spinner("Uploading documents..."):
#                     res = requests.post(
#                         f"{BACKEND_URL}/upload/",
#                         files=files
#                     )

#                 if res.status_code == 200:
#                     st.session_state.session_id = res.json()["session_id"]
#                     st.success("Documents uploaded successfully")
#                 else:
#                     st.error("Upload failed")

#         st.divider()
#         st.subheader("📑 Document Summary")

#         if st.session_state.session_id:
#             if st.button("Generate Summary"):
#                 with st.spinner("Generating summary..."):
#                     res = requests.post(
#                         f"{BACKEND_URL}/api/summary",
#                         json={"session_id": st.session_state.session_id}
#                     )
#                 if res.status_code == 200:
#                     st.write(res.json().get("summary", "No summary"))
#                 else:
#                     st.error("Failed to generate summary")

# # ================= RIGHT PANEL (CHAT – FIXED & SCROLLABLE) =================
# with right:
#     st.markdown("## 💬 Chat")

#     if st.session_state.session_id is None:
#         st.info("You can chat generally. Upload documents for document-based answers.")

#     # Chat wrapper
#     st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)

#     # Scrollable chat area
#     st.markdown('<div class="chat-scroll">', unsafe_allow_html=True)

#     # Empty state (IMPORTANT FIX)
#     if not st.session_state.messages:
#         st.markdown(
#             '<div class="ai-msg">🤖 Hello! Ask me anything, or upload documents to start.</div>',
#             unsafe_allow_html=True
#         )

#     # Chat history
#     for msg in st.session_state.messages:
#         if msg["role"] == "user":
#             st.markdown(
#                 f'<div class="user-msg">🧑 {msg["content"]}</div>',
#                 unsafe_allow_html=True
#             )
#         else:
#             st.markdown(
#                 f'<div class="ai-msg">🤖 {msg["content"]}</div>',
#                 unsafe_allow_html=True
#             )

#     st.markdown('</div>', unsafe_allow_html=True)

#     # Fixed input area
#     st.markdown('<div class="chat-input">', unsafe_allow_html=True)
#     with st.form("chat_form", clear_on_submit=True):
#         question = st.text_input("Type your message…")
#         send = st.form_submit_button("Send")
#     st.markdown('</div>', unsafe_allow_html=True)

#     st.markdown('</div>', unsafe_allow_html=True)

#     # ================= SEND MESSAGE =================
#     if send and question.strip():
#         # Add user message
#         st.session_state.messages.append({
#             "role": "user",
#             "content": question
#         })

#         payload = {
#             "session_id": st.session_state.session_id,
#             "question": question
#         }

#         with st.spinner("Thinking..."):
#             res = requests.post(
#                 f"{BACKEND_URL}/api/chat",
#                 json=payload
#             )

#         if res.status_code == 200:
#             data = res.json() or {}
#             answer = data.get("answer", "No response")

#             st.session_state.messages.append({
#                 "role": "assistant",
#                 "content": answer
#             })
#         else:
#             st.session_state.messages.append({
#                 "role": "assistant",
#                 "content": "Error getting response from server"
#             })

#         st.rerun()

# # ================= AUTO-SCROLL TO BOTTOM =================
# st.markdown("""
# <script>
# const chatScroll = document.querySelector('.chat-scroll');
# if (chatScroll) {
#   chatScroll.scrollTop = chatScroll.scrollHeight;
# }
# </script>
# """, unsafe_allow_html=True)














import streamlit as st
import requests

# ================= CONFIG =================
# BACKEND_URL = "http://127.0.0.1:8000"
BACKEND_URL = "https://rag-system-with-extra-feature.onrender.com/"


st.set_page_config(
    page_title="AI Document Chat",
    layout="wide"
)

# ================= SESSION STATE =================
if "session_id" not in st.session_state:
    st.session_state.session_id = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# ================= CSS (FIXED CHAT LAYOUT) =================
st.markdown("""
<style>
:root {
  --bg: var(--background-color);
  --text: var(--text-color);
  --user-bg: #DCF8C6;
  --ai-bg: #FFFFFF;
  --border: rgba(0,0,0,0.15);
}

@media (prefers-color-scheme: dark) {
  :root {
    --user-bg: #2E7D32;
    --ai-bg: #1E1E1E;
    --border: rgba(255,255,255,0.2);
  }
}

/* Hide Streamlit's default padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 0rem;
}

/* Chat container - fixed height */
.chat-container {
    height: calc(100vh - 250px);
    display: flex;
    flex-direction: column;
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
}

/* Scrollable messages area */
.chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    display: flex;
    flex-direction: column;
}

/* Fixed input at bottom */
.chat-input-container {
    border-top: 1px solid var(--border);
    padding: 15px;
    background-color: var(--bg);
}

.user-msg {
    background-color: var(--user-bg);
    color: var(--text);
    padding: 10px 14px;
    border-radius: 12px;
    margin: 6px 0;
    max-width: 70%;
    align-self: flex-end;
    word-wrap: break-word;
}

.ai-msg {
    background-color: var(--ai-bg);
    color: var(--text);
    padding: 10px 14px;
    border-radius: 12px;
    margin: 6px 0;
    max-width: 70%;
    align-self: flex-start;
    word-wrap: break-word;
    border: 1px solid var(--border);
}

/* Hide Streamlit form spacing */
.stForm {
    margin: 0 !important;
    padding: 0 !important;
}

/* Improve text input */
.stTextInput > div > div > input {
    border-radius: 20px;
}
</style>
""", unsafe_allow_html=True)

# ================= LAYOUT =================
left, right = st.columns([3, 7], gap="large")

# ================= LEFT PANEL (DOCUMENTS) =================
with left:
    st.markdown("## 📂 Documents")

    uploaded_files = st.file_uploader(
        "Upload PDF or DOCX",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    if st.button("Upload", use_container_width=True):
        if not uploaded_files:
            st.warning("Please upload at least one file")
        else:
            files = [
                ("files", (f.name, f.getvalue(), f.type))
                for f in uploaded_files
            ]
            with st.spinner("Uploading documents..."):
                res = requests.post(
                    f"{BACKEND_URL}/upload/",
                    files=files
                )

            if res.status_code == 200:
                st.session_state.session_id = res.json()["session_id"]
                st.success("Documents uploaded successfully")
            else:
                st.error("Upload failed")

    st.divider()
    st.subheader("📑 Document Summary")

    if st.session_state.session_id:
        if st.button("Generate Summary", use_container_width=True):
            with st.spinner("Generating summary..."):
                res = requests.post(
                    f"{BACKEND_URL}/api/summary",
                    json={"session_id": st.session_state.session_id}
                )
            if res.status_code == 200:
                st.write(res.json().get("summary", "No summary"))
            else:
                st.error("Failed to generate summary")

# ================= RIGHT PANEL (CHAT) =================
with right:
    st.markdown("## 💬 Chat")

    if st.session_state.session_id is None:
        st.info("You can chat generally. Upload documents for document-based answers.")

    # Create chat container with messages area
    chat_placeholder = st.container()
    
    with chat_placeholder:
        # Messages container (scrollable)
        messages_html = '<div class="chat-container"><div class="chat-messages" id="chat-messages">'
        
        # Empty state or chat history
        if not st.session_state.messages:
            messages_html += '<div class="ai-msg">🤖 Hello! Ask me anything, or upload documents to start.</div>'
        else:
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    messages_html += f'<div class="user-msg">🧑 {msg["content"]}</div>'
                else:
                    messages_html += f'<div class="ai-msg">🤖 {msg["content"]}</div>'
        
        messages_html += '</div></div>'
        st.markdown(messages_html, unsafe_allow_html=True)

    # Fixed input at bottom (outside the scrollable area)
    st.markdown('<div class="chat-input-container">', unsafe_allow_html=True)
    
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([6, 1])
        with col1:
            question = st.text_input("Type your message…", label_visibility="collapsed")
        with col2:
            send = st.form_submit_button("Send", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # ================= SEND MESSAGE =================
    if send and question.strip():
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        payload = {
            "session_id": st.session_state.session_id,
            "question": question
        }

        with st.spinner("Thinking..."):
            res = requests.post(
                f"{BACKEND_URL}/api/chat",
                json=payload
            )

        if res.status_code == 200:
            data = res.json() or {}
            answer = data.get("answer", "No response")

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })
        else:
            st.session_state.messages.append({
                "role": "assistant",
                "content": "Error getting response from server"
            })

        st.rerun()

# ================= AUTO-SCROLL TO BOTTOM =================
st.markdown("""
<script>
// Auto-scroll to bottom when page loads
setTimeout(function() {
    const chatMessages = document.getElementById('chat-messages');
    if (chatMessages) {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}, 100);
</script>
""", unsafe_allow_html=True)