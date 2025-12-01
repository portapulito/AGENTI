from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END

from .llm_client import LLMClient
from .prompts import SYSTEM_PROMPT
from .postprocess import fix_html

class UIState(TypedDict):
    """State for the UI generation graph."""
    user_prompt: str
    html: str

async def generate_page(state: UIState) -> UIState:
    """
    Node that generates the HTML page based on the user prompt.
    """
    user_prompt = state["user_prompt"]
    
    # Initialize LLM Client
    client = LLMClient()
    
    # Generate HTML
    raw_html = client.generate_html(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt
    )
    
    # Post-process HTML
    clean_html = fix_html(raw_html)
    
    return {"html": clean_html}

def get_graph():
    """
    Constructs and compiles the LangGraph.
    """
    workflow = StateGraph(UIState)
    
    # Add nodes
    workflow.add_node("generate_page", generate_page)
    
    # Define edges
    workflow.set_entry_point("generate_page")
    workflow.add_edge("generate_page", END)
    
    # Compile
    return workflow.compile()

async def generate_html_from_prompt(prompt: str) -> str:
    """
    Helper function to run the graph with a given prompt and return the HTML.
    """
    app = get_graph()
    initial_state = {"user_prompt": prompt, "html": ""}
    result = await app.ainvoke(initial_state)
    return result.get("html", "")
