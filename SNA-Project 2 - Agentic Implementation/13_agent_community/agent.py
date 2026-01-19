from google.adk.agents import Agent
from .tools import get_community_info
from graph import G
from google.adk.tools import FunctionTool
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="Community_Agent",
    model=LiteLlm(model="ollama_chat/llama3.1:8b"),
    instruction="""You are a Community Structure Analyst for the Wiki-Vote network.
    Your task is to identify which broader group (community) a user belongs to using the 'get_community_info' tool.
    
    THEORY CONTEXT:
    - Networks are often divided into communities (modules) where nodes are densely connected internally (High Modularity).
    - Knowing a user's community helps identify their political faction or interest group.
    
    When asked about a user, specify their community ID and who the key leaders in that group are.""",
    tools=[
        FunctionTool(get_community_info)
    ],

)
