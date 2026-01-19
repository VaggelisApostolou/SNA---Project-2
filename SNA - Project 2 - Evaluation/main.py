import numpy as np
import scipy.io as sio
import networkx as nx
from graph import G, communities_list

prestige_id = int(input("Enter the user id for prestige: \n"))
path_source_id = int(input("Enter the user id for source in the path: \n"))
path_target_id = int(input("Enter the user id for target in the path: \n"))
cluster_id = int(input("Enter the user id for cluster: \n"))
community_id = int(input("Enter the user id for community: \n"))
pagerank_id = int(input("Enter the user id for pagerank: \n"))

#Prestige
if prestige_id not in G:
    print(f"User {prestige_id} does not exist in the Wiki-Vote network.\n")
else:
    prestige = G.in_degree(prestige_id)
    activity = G.out_degree(prestige_id)
    print(f"User {prestige_id} Analysis:\n"
          f"- Prestige (In-Degree): {prestige} votes received.\n"
          f"- Activity (Out-Degree): {activity} votes given.\n")

#Path
if path_source_id not in G or path_target_id not in G:
    print(f"Error: One or both users for the path do not exist in the network.\n")
else:
    try:
        path = nx.shortest_path(G, source=path_source_id, target=path_target_id)
        distance = len(path) - 1
        print(f"Path found!\n"
              f"- Geodesic Distance: {distance} steps.\n"
              f"- Path Sequence: {path}\n")

    except nx.NetworkXNoPath:
        print(f"No path exists. User {path_source_id} cannot influence User {path_target_id}.\n")

#Cluster
if cluster_id not in G:
    print(f"User {cluster_id} does not exist in the Wiki-Vote network.\n")
else:
    coef = nx.clustering(G, cluster_id)
    print(f"User {cluster_id} Clustering Coefficient: {coef:.4f}.\n")

#Community
if community_id not in G:
    print(f"User {community_id} does not exist in the Wiki-Vote network.\n")
else:
    for i, comm in enumerate(communities_list):
        if community_id in comm:
            size = len(comm)
            top_members = sorted(list(comm), key=lambda n: G.degree(n), reverse=True)[:3]
            print(f"User {community_id} belongs to Community #{i}.\n"
                  f"- Community Size: {size} members.\n"
                  f"- Key Leaders in this group: {top_members}\n")

#Bridges
top_n = 5
bc = nx.betweenness_centrality(G, normalized=True, endpoints=False)
top_bridges = sorted(bc.items(), key=lambda item: item[1], reverse=True)[:top_n]
result = "Top Network Bridges (Information Brokers):\n"
for rank, (user, score) in enumerate(top_bridges, 1):
    result += f"{rank}. User {user} (Score: {score:.4f})\n"
print(result)

#Pagerank
if pagerank_id not in G:
    print(f"User {pagerank_id} does not exist in the Wiki-Vote network.\n")
else:
    pr_scores = nx.pagerank(G, alpha=0.85)
    score = pr_scores.get(pagerank_id)
    print(f"User {pagerank_id} PageRank: {score:.6f}.\n")
