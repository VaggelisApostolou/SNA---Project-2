from google.adk.agents import Agent
from .tools import get_node_prestige
from graph import G
from google.adk.tools import FunctionTool
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="Prestige_Agent",
    model=LiteLlm(model="ollama_chat/llama3.1:8b"),
    instruction="""You are a Network Analysis Agent. 
    You have access to a tool 'get_node_prestige' which analyzes the Wiki-Vote graph.
    When asked about a user's influence or activity, ALWAYS use this tool first.
    Do not guess the numbers.""",
    tools=[
        FunctionTool(get_node_prestige)
    ],

)
