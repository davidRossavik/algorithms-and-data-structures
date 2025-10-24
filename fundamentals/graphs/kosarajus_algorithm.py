"""
kosarajus_algorithm.py
-------
Implementation of algorithm for finding strongly connected Components in Python.

Definition:
    - Group of nodes where everyone can reach everyone

Strongly Connected Components are used to discover and isolate subgraphs where
all the nodes can reach eachother. This makes it possible to simplify, analyze
and optimize complex direct graphs.

The main idea:
    1. Run DFS over the entire graph
        > When finished with a node, we note the finish-time
        > When finished with a node, we know that all nodes that can be reached from that one, is visited
        > The finish-time of this node tells us about the order of the components (using a stack here)
    2. Turn every edge 
        > Components that earlier pointed out is now entrances
        > Therefore is possible to enter the SCC from the outside
    3. Run DFS on the transposed graph, but start in the order of decreasing finish-time
        > Everytime we start on a new node: We get a new SCC, DFS will only keep itself inside the component (all outgoing edges is now ingoing)


Time Complexity:
    - Running DFS twice over all vertices and edges: O(V + E)

Space Complexity:
    - O(V + E)

Author: David
Date: 24-10-2025
"""

# Simple DFS with finish-time
def dfs(graph, u, visited, stack): #O(V + E)
    visited.add(u) 
    for v in graph[u]:
        if v not in visited:
            dfs(graph, v, visited, stack)
    stack.append(u) 

# Transpose the graph
def transpose(graph): #O(n * v)
    g_t = {u: [] for u in graph}    # Initialixed as a dict with lists
    for u in graph:
        for v in graph[u]:
            g_t[v].append(u)
    return g_t

# DFS to find a whole SCC
def dfs_collect(graph, u, visited, component):
    visited.add(u)
    component.append(u)
    for v in graph[u]:
        if v not in visited:
            dfs_collect(graph, v, visited, component)


# Function for finding SCC
def find_SCC(graph):
    visited = set()
    stack = []

    # Phase 1: run DFS and find finish-time
    for u in graph:
        if u not in visited:
            dfs(graph, u, visited, stack)
    
    # Phase 2: Transpose the graph
    g_t = transpose(graph)

    # Phase 3: DFS on the transposed graph in decreasing finish-time
    visited.clear()
    SCCs = []

    while stack:    #O(V)
        u = stack.pop()     # Highest finish-time first
        if u not in visited:
            component = []
            dfs_collect(g_t, u, visited, component)
            SCCs.append(component)
    
    return SCCs

if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['C', 'D'],
        'C': ['A'],
        'D': ['E'],
        'E': ['D']
    }

    print(find_SCC(graph))





