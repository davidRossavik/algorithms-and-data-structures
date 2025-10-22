"""
traversing_classic.py
----------------------
Implementation of the fundamental traversingalgorithm for graphs in Python.
This graph creates the foundation for DFS and BFS (dept/breadth-first search).

The main idea:
    1. A traversal will visit all the nodes that can be reached from a startnode u
    2. It keeps track of which nodes that are already visited to avoid endless cycles

Includes:
    - Recursive DFS (Depth-First Search) (stack-based traversal)

Time Complexity:
    - O(V + E): Number of vertices and edges

Space Complexity:
    - O(V)

Author: David
Date: 22-10-2025
"""

def dfs(graph, u, visited=None):
    if visited is None:
        visited = set()
    
    print(u)    # Prints the node
    visited.add(u)  # Mark as visited

    for v in graph[u]: # Traverses through all the neighbours
        if v not in visited:
            dfs(graph, v, visited)
    

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    dfs(graph, 'A')