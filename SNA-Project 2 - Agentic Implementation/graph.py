import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict, Any, Optional
from networkx.algorithms import community

G = nx.read_edgelist("Wiki-Vote.txt", create_using=nx.DiGraph(), nodetype=int)

print("Calculating network communities (this might take a few seconds)...")
communities_list = list(community.greedy_modularity_communities(G))
print(f"Detected {len(communities_list)} distinct communities.")
