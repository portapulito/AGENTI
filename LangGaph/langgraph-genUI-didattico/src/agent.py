import uuid
from typing import Annotated, Sequence, TypedDict

from langchain_core.messages import AIMessage, BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
# Note: Ensure langgraph is updated to support these imports or check documentation if they moved.
# Based on the user request tutorial:
from langgraph.graph.ui import AnyUIMessage, ui_message_reducer, push_ui_message

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    ui: Annotated[Sequence[AnyUIMessage], ui_message_reducer]

async def weather(state: AgentState):
    class WeatherOutput(TypedDict):
        city: str

    # Using GPT-4o-mini as per tutorial
    llm = ChatOpenAI(model="gpt-4o-mini")
    
    # Simple structured output to extract city
    weather_data: WeatherOutput = (
        await llm.with_structured_output(WeatherOutput)
        .with_config({"tags": ["nostream"]})
        .ainvoke(state["messages"])
    )

    message = AIMessage(
        id=str(uuid.uuid4()),
        content=f"Here's the weather for {weather_data['city']}",
    )

    # Emit UI elements associated with the message
    # The first argument "weather" must match the key in the React component map
    push_ui_message("weather", weather_data, message=message)
    
    return {"messages": [message]}

workflow = StateGraph(AgentState)
workflow.add_node("weather", weather)
workflow.add_edge("__start__", "weather")
graph = workflow.compile()
