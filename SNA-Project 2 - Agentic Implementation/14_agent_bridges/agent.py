from google.adk.agents import Agent
from .tools import get_network_bridges
from graph import G
from google.adk.tools import FunctionTool
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="Bridges_Agent",
    model=LiteLlm(model="ollama_chat/llama3.1:8b"),
    instruction="""You are a Strategic Network Analyst looking for 'Brokers' or 'Bridges'.
    
    THEORY CONTEXT:
    - Betweenness Centrality measures how often a node appears on the shortest paths between other nodes.
    - Users with high betweenness are 'Bridges': they connect disparate groups and control information flow.
    - They are powerful even if they don't have the most votes (Degree).
    
    Use the 'get_network_bridges' tool to identify these key players.""",
    tools=[
        FunctionTool(get_network_bridges)
    ],

)
