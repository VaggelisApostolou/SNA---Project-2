from google.adk.agents import Agent
from .tools import get_node_prestige, check_connection_path, check_clustering_coefficient, get_community_info, get_network_bridges, get_pagerank_score
from google.adk.tools import AgentTool, FunctionTool
from google.adk.models.lite_llm import LiteLlm

prestige_agent = Agent(
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

path_agent = Agent(
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

cluster_coef_agent = Agent(
    name="Cluster_Coef_Agent",
    model=LiteLlm(model="ollama_chat/llama3.1:8b"),
    instruction="""You are a Social Network Structure Analyst.
    Your specific task is to analyze local clustering using the 'check_clustering_coefficient' tool.
    
    THEORY CONTEXT:
    - High clustering coefficient means the user's friends are likely friends with each other (indicates a tight 'clique' or 'echo chamber').
    - Low clustering coefficient (near 0) means the user connects disparate groups (star-like structure).
    
    When asked about a user, interpret the coefficient value based on this theory and return this value with extra comments based on the theory.""",
    tools=[
        FunctionTool(check_clustering_coefficient)
    ],

)

community_agent = Agent(
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

bridges_agent = Agent(
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

pagerank_agent = Agent(
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

root_agent = Agent(
    name="Manager_Agent",
    model=LiteLlm(model="ollama_chat/llama3.1:8b"),
    instruction="""You are an expert Network Campaign Manager and Strategist.
    Your goal is to identify the best 'seed' user to start a diffusion campaign in the Wiki-Vote network by coordinating a team of specialized analysts.
    
    YOUR WORKFLOW:
    1.  Receive the candidate user IDs from the user.
    2.  DELEGATE tasks to your sub-agents (Prestige, Pagerank, Community, Cluster_Coef) to get specific data for EACH candidate.
    3.  WAIT for the information from all agents.
    4.  SYNTHESIZE the results. Compare the candidates side-by-side based on:
        * Prestige (Votes) vs PageRank (Authority)
        * Community Size (Reach)
        * Clustering (Local vs Global influence)
    5.  FINAL DECISION: Clearly state who is the best seed and WHY, based on the data provided by your team.
    
    IMPORTANT: Do not just list the tool calls. You must read their output and generate a final recommendation report text.""",
    tools=[
        AgentTool(prestige_agent),
        AgentTool(path_agent),
        AgentTool(cluster_coef_agent),
        AgentTool(community_agent),
        AgentTool(bridges_agent),
        AgentTool(pagerank_agent)
    ],

)