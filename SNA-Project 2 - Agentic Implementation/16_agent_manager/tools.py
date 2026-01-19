from pathlib import Path
#from graph import G, communities_list
from typing import List, Dict, Any, Optional
import networkx as nx
import numpy as np
import scipy.io as sio
from networkx.algorithms import community

G = nx.read_edgelist("Wiki-Vote.txt", create_using=nx.DiGraph(), nodetype=int)

print("Calculating network communities (this might take a few seconds)...")
communities_list = list(community.greedy_modularity_communities(G))
print(f"Detected {len(communities_list)} distinct communities.")

def get_node_prestige(user_id: int) -> str:
    """
    Returns the Prestige (in-degree) and Activity (out-degree) of a user.
    Use this tool when you need to evaluate if a user is influential or active in the network.
    
    Args:
        user_id (int): The ID of the user to analyze (e.g. 30, 4037).
    """
    if user_id not in G:
        return f"User {user_id} does not exist in the Wiki-Vote network."
    
    prestige = G.in_degree(user_id) 
    activity = G.out_degree(user_id)
    
    return (f"User {user_id} Analysis:\n"
            f"- Prestige (In-Degree): {prestige} votes received.\n"
            f"- Activity (Out-Degree): {activity} votes given.\n"
            f"Note: High prestige indicates an influential 'opinion leader'.")

def check_connection_path(source_id: int, target_id: int) -> str:
    """
    Checks if a path exists between two users and calculates the geodesic distance.
    Use this tool to determine if influence can spread from a source user to a target user.
    
    Args:
        source_id (int): The starting user ID.
        target_id (int): The target user ID.
    """

    if source_id not in G or target_id not in G:
        return "Error: One or both users do not exist in the network."
    
    try:
        path = nx.shortest_path(G, source=source_id, target=target_id)
        distance = len(path) - 1
        
        return (f"Path found!\n"
                f"- Geodesic Distance: {distance} steps.\n"
                f"- Path Sequence: {path}\n"
                f"Interpretation: Influence can flow directly or indirectly.")
                
    except nx.NetworkXNoPath:
        return f"No path exists. User {source_id} cannot influence User {target_id}."
    
def check_clustering_coefficient(user_id: int) -> str:
    """
    Calculates the Local Clustering Coefficient of a user.
    Use this to see if the user's neighbors also know each other (forming a 'clique').
    """
    if user_id not in G:
        return f"User {user_id} not found."
    
    coef = nx.clustering(G, user_id)
    
    analysis = "Low clustering (Star-like)" if coef < 0.1 else "High clustering (Clique member)"
    return f"User {user_id} Clustering Coefficient: {coef:.4f}. Interpretation: {analysis}."

def get_community_info(user_id: int) -> str:
    """
    Identifies which community (group) a user belongs to.
    Use this to understand the user's broader group allegiance.
    """
    if user_id not in G:
        return f"User {user_id} not found."

    for i, comm in enumerate(communities_list):
        if user_id in comm:
            size = len(comm)
            top_members = sorted(list(comm), key=lambda n: G.degree(n), reverse=True)[:3]
            return (f"User {user_id} belongs to Community #{i}.\n"
                    f"- Community Size: {size} members.\n"
                    f"- Key Leaders in this group: {top_members}")
    
    return "User does not belong to any detected community."

def get_network_bridges(top_n: int = 5) -> str:
    """
    Identifies the top 'Bridge' users (Brokers) in the network based on Betweenness Centrality.
    Use this tool to find users who control the flow of information between different groups.
    
    Args:
        top_n (int): The number of top brokers to return (default is 5).
    """
    print("Calculating Betweenness Centrality (approximated for speed)...")
    
    bc = nx.betweenness_centrality(G, normalized=True, endpoints=False)
    
    top_bridges = sorted(bc.items(), key=lambda item: item[1], reverse=True)[:top_n]
    
    result = "Top Network Bridges (Information Brokers):\n"
    for rank, (user, score) in enumerate(top_bridges, 1):
        result += f"{rank}. User {user} (Score: {score:.4f})\n"
        
    result += "Theory: These users act as 'gatekeepers' connecting different communities."
    return result

def get_pagerank_score(user_id: int) -> str:
    """
    Calculates the PageRank score of a user.
    Use this to measure 'quality' influence: being voted for by other influential users.
    Difference from Prestige: Prestige counts votes, PageRank weighs them.
    """
    
    try:
        pr_scores = nx.pagerank(G, alpha=0.85)
        score = pr_scores.get(user_id)
        
        if score is None:
            return f"User {user_id} not found."
            
        avg_score = sum(pr_scores.values()) / len(pr_scores)
        status = "High Authority" if score > avg_score * 2 else "Average/Low Authority"
        
        return (f"User {user_id} PageRank: {score:.6f}.\n"
                f"Interpretation: {status}. (Higher score means endorsement by other VIPs).")
    except Exception as e:
        return f"Error calculating PageRank: {e}"