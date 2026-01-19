from pathlib import Path
from graph import G, communities_list
from typing import List, Dict, Any, Optional
import networkx as nx
from networkx.algorithms import community
import numpy as np
import scipy.io as sio

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