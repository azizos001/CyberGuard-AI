from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import SystemMessage
from src.config import GROQ_API_KEY, LLM_MODEL
from src.tools import search_cybersecurity_knowledge, analyze_security_log, get_latest_cve_info

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=LLM_MODEL,
    temperature=0.1,
    max_tokens=2000
)

tools = [search_cybersecurity_knowledge, analyze_security_log, get_latest_cve_info]

system_prompt = SystemMessage(content="""You are **CyberGuard AI** — an elite cybersecurity expert and Agentic SOC Analyst.

Core Rules:
- Always use tools when needed (especially search_cybersecurity_knowledge for factual info)
- For any log → always use analyze_security_log tool
- For specific CVEs → use get_latest_cve_info
- Cite sources clearly using the numbers [1], [2], etc.
- Be professional, precise, and actionable.
- Think step-by-step.""")

memory = MemorySaver()

agent_executor = create_react_agent(
    model=llm,
    tools=tools,
    prompt=system_prompt,
    checkpointer=memory
)

def ask_cybersec_agent(query: str, thread_id: str = "default"):
    config = {"configurable": {"thread_id": thread_id}}
    
    response = agent_executor.invoke({
        "messages": [("user", query)]
    }, config=config)
    
    return response["messages"][-1].content
