from pathlib import Path
from graph import G, communities_list
from typing import List, Dict, Any, Optional
import networkx as nx
from networkx.algorithms import community
import numpy as np
import scipy.io as sio

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