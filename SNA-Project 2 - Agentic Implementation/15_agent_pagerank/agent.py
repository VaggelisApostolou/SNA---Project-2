from google.adk.agents import Agent
from .tools import get_pagerank_score
from graph import G
from google.adk.tools import FunctionTool
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="Pagerank_Agent",
    model=LiteLlm(model="ollama_chat/llama3.1:8b"),
    instruction="""You are an Authority Analyst for the Wiki-Vote network.
    Your sole purpose is to evaluate the 'quality' of a user's influence using the 'get_pagerank_score' tool.
    
    THEORY CONTEXT:
    - Standard popularity (Degree Centrality) counts votes.
    - PageRank measures authority: a user is influential if they are voted for by other influential users.
    
    When asked about a user, explain if they are considered a high-authority figure based on their PageRank score.""",
    tools=[
        FunctionTool(get_pagerank_score)
    ],

)
