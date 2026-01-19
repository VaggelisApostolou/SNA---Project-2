from pathlib import Path
from graph import G
from typing import List, Dict, Any, Optional
import networkx as nx
import numpy as np
import scipy.io as sio

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