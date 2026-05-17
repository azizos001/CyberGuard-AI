import streamlit as st
import os
from src.agent import ask_cybersec_agent
from src.ingestion import ingest_documents

st.set_page_config(page_title="CyberGuard AI", page_icon="🛡️", layout="wide")

st.title("🛡️ CyberGuard AI")
st.subheader("Agentic RAG Cybersecurity Assistant — Option 3")

# Sidebar
with st.sidebar:
    st.header("Document Management")
    uploaded_files = st.file_uploader("Upload new PDFs", accept_multiple_files=True, type=["pdf"])
    
    col1, col2 = st.columns(2)
    with col1:
        if uploaded_files and st.button("Process Documents"):
            os.makedirs("data", exist_ok=True)
            for file in uploaded_files:
                with open(f"data/{file.name}", "wb") as f:
                    f.write(file.getbuffer())
            with st.spinner("Ingesting..."):
                ingest_documents()
            st.success("✅ Documents added!")

    with col2:
        if st.button("Rebuild Vectorstore"):
            with st.spinner("Rebuilding..."):
                ingest_documents()
            st.success("Vectorstore updated!")

    st.divider()
    thread_id = st.text_input("Session ID", value="main", help="Change for new conversation")

# Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about vulnerabilities, attacks, logs..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Agent is thinking..."):
            response = ask_cybersec_agent(prompt, thread_id=thread_id)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})