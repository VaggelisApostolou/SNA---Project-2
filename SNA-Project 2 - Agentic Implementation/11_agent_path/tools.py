from pathlib import Path
from graph import G
from typing import List, Dict, Any, Optional
import networkx as nx
import numpy as np
import scipy.io as sio

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