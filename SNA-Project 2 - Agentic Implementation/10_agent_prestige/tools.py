from pathlib import Path
from graph import G
from typing import List, Dict, Any, Optional


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