# 🛡️ CyberGuard AI - Agentic Cybersecurity RAG Assistant

**Advanced Option 3 Project** — Agentic RAG built with LangChain + LangGraph + Groq

![Streamlit](https://img.shields.io/badge/Interface-Streamlit-brightgreen) 
![Groq](https://img.shields.io/badge/LLM-Groq%20Llama3-70B-blue) 
![LangGraph](https://img.shields.io/badge/Agent-LangGraph-orange)

## ✨ Features

- **Fully Agentic RAG** (Option 3) — The agent autonomously decides when to retrieve knowledge, analyze logs, or answer directly
- **Re-ranking** for better retrieval quality
- **Multiple Tools**:
  - Cybersecurity Knowledge Base Search (with citations)
  - Security Log Analysis (SOC-level)
  - CVE Information Lookup
- **Conversation Memory** (multi-session)
- **Dynamic Document Upload** + Ingestion
- **Professional Streamlit UI** with sidebar controls

## 🏗️ Architecture

- **Ingestion**: PyPDF + RecursiveCharacterTextSplitter + ChromaDB + all-MiniLM-L6-v2 embeddings
- **Retrieval**: Contextual Compression + Cross-Encoder Re-ranker
- **Agent**: LangGraph ReAct Agent (Llama3-70B via Groq)
- **UI**: Streamlit (professional & user-friendly)

## 🚀 Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/yourusername/cybersec-rag-agent.git
cd cybersec-rag-agent
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 2. Environment
Create .env:
```bash
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxx
```
### 3. Add Documents
Put cybersecurity PDFs in the data/ folder (see recommended corpus in docs).
### 4. Ingest
```bash
python -c "from src.ingestion import ingest_documents; ingest_documents()"
```
### 5. Run
```bash
streamlit run app.py
```
## Project Structure
```bash
cybersec-rag-agent/
├── data/                 # Put your PDFs here
├── vectorstore/          # ChromaDB (auto-created)
├── src/
│   ├── config.py
│   ├── ingestion.py
│   ├── tools.py
│   ├── agent.py
│   └── ...
├── app.py
├── requirements.txt
└── README.md
```
## 🎯 Alignment with Project Requirements
- **Option 1**: Fully implemented (Loader, Chunking, Embeddings, Vector Store, Retrieval, LLM)
- **Option 2**: Re-ranking, Prompt Engineering, Memory, Professional UI
- **Option 3**: LangGraph Agent + Multiple Tools + Autonomous Decision Making
## 📄 License
MIT License
