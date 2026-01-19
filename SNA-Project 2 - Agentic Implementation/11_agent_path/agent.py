from google.adk.agents import Agent
from .tools import check_connection_path
from graph import G
from google.adk.tools import FunctionTool
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="Path_Agent",
    model=LiteLlm(model="ollama_chat/llama3.1:8b"),
    instruction="""You are a Connectivity Analyst for the Wiki-Vote network.
    Your main task is to find if and how users are connected using the 'check_connection_path' tool.
    When a user asks about the relationship or distance between two users, calculate the shortest path.
    Explain the results in terms of 'steps' of influence.""",
    tools=[
        FunctionTool(check_connection_path)
    ],

)
