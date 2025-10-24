"""
bfs.py
-------
Implementation of an BFS (Breadth-First-Search) algorithm in Python.

BFS is used for 

The main idea:
    - (Explores all the nodes in increasing distance from the startnode)
    - Uses a FIFO-queue (First-in-First-out) Just a normal queue
    1. Starts at a node s (marks as visited and is put in the queue)
    2. Takes ut the first node from the queue
    3. Visits all its neighbours that are not visited
        > Mark them as visited and is put in the queue
    4. Repeat until the queue is empty

Time Complexity:
    - O(V + E)

Space Complexity:
    - O(V)

Author: David
Date: 24-10-2025
"""
from collections import deque

def bfs(graph, start):
    visited = set()
    parent = {start: None}     # Keep tracks over who discovered who
    queue = deque([start])


    while queue:
        node = queue.popleft()

        for neighbour in graph[node]:
            if neighbour not in visited and neighbour not in parent:
                parent[neighbour] = node
                queue.append(neighbour)
        visited.add(neighbour)
    return parent

# Printing function
def print_path(graph, parent, s, v):
    #1. We have reached the startnode
    if v == s:
        print(s, end=" ")

    # 2. We cannot reach endnode v
    elif v not in parent or parent[v] is None:
        print(f"No path from {s} to {v}")
    
    # 3. Recursive call: go back to start
    else:
        print_path(graph, parent, s, parent[v])
        print(v, end=" ")
    


if __name__ == "__main__":
    graph = {
        'A': ['B', 'D'],
        'B': ['C', 'E'],
        'C': [],
        'D': [],
        'E': []
    }

    parent = bfs(graph, 'A')
    print("Parent dictionary:", parent)

    print("\nPath from A to E:")
    print_path(graph, parent,'A', 'E')

