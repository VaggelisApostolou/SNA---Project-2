from pathlib import Path
from graph import G
from typing import List, Dict, Any, Optional
import networkx as nx
import numpy as np
import scipy.io as sio

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