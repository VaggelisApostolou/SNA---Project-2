import networkx as nx
from networkx.algorithms import community
import pickle
import os

G = nx.read_edgelist("Wiki-Vote.txt", create_using=nx.DiGraph(), nodetype=int)

if os.path.exists("communities_cache.pkl"):
    print("Loading communities from cache... (Fast)")
    with open("communities_cache.pkl", "rb") as f:
        communities_list = pickle.load(f)
else:
    print("Calculating communities... (This happens only once)")
    communities_list = list(community.greedy_modularity_communities(G))
    with open("communities_cache.pkl", "wb") as f:
        pickle.dump(communities_list, f)

print(f"Detected {len(communities_list)} distinct communities.")
