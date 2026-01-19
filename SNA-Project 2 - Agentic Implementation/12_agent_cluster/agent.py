from google.adk.agents import Agent
from .tools import check_clustering_coefficient
from graph import G
from google.adk.tools import FunctionTool
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="Cluster_Coef_Agent",
    model=LiteLlm(model="ollama_chat/llama3.1:8b"),
    instruction="""You are a Social Network Structure Analyst.
    Your specific task is to analyze local clustering using the 'check_clustering_coefficient' tool.
    
    THEORY CONTEXT:
    - High clustering coefficient means the user's friends are likely friends with each other (indicates a tight 'clique' or 'echo chamber').
    - Low clustering coefficient (near 0) means the user connects disparate groups (star-like structure).
    
    When asked about a user, interpret the coefficient value based on this theory.
    At the end always return the coefficient value with extra comments based on the theory.""",
    tools=[
        FunctionTool(check_clustering_coefficient)
    ],

)
