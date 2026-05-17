from langchain.tools import tool
from langchain_groq import ChatGroq
from src.ingestion import get_vectorstore
from src.config import GROQ_API_KEY, LLM_MODEL, RERANKER_MODEL
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain.retrievers import ContextualCompressionRetriever

vectorstore = get_vectorstore()
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 12})

# Reranker
cross_encoder = HuggingFaceCrossEncoder(model_name=RERANKER_MODEL)
reranker = CrossEncoderReranker(model=cross_encoder, top_n=5)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=reranker,
    base_retriever=base_retriever
)

llm = ChatGroq(api_key=GROQ_API_KEY, model=LLM_MODEL, temperature=0)

@tool
def search_cybersecurity_knowledge(query: str) -> str:
    """Search the cybersecurity knowledge base with reranking."""
    docs = compression_retriever.invoke(query)
    formatted = []
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get('source', 'Unknown').split('/')[-1]
        formatted.append(f"**[{i}] {source}**\n{doc.page_content}\n")
    return "\n".join(formatted)

@tool
def analyze_security_log(log_text: str) -> str:
    """Analyze security logs for anomalies and attack patterns."""
    prompt = f"""You are a senior SOC analyst. Analyze this log carefully:

{log_text}

Return in this format:
- Summary
- Detected Threats
- Risk Level (Low/Med/High/Critical)
- Recommended Actions"""
    
    response = llm.invoke(prompt)
    return response.content

@tool
def get_latest_cve_info(cve_id: str) -> str:
    """Get information about a specific CVE (e.g., CVE-2024-1234)."""
    # For now, it will use knowledge base. You can add real API later.
    return f"Searching knowledge base for {cve_id}..."