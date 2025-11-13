"""
Implementation of Djikstra's algorithm in Python.
-------------------------------------------------
Goal: Find the shortest path from one startnode to all other nodes in a directed graph with non-negative weights.

UTILIZES A GREEDY STRATEGY:
    - Always chooses the "nearest" next node, effectively

The main idea:
    - When you find the shortes path to a node,
      Then you are sure that the node can't be improved later (as long as all edges are non-negative)
    1. Initialize start to 0 and all others to infinity
    2. Choose the node with the smallest estimat that are not pre-processed
    3. Relax all edges from that one
    4. Repeat until all nodes are processed

Time Complexity:
    - O((V + E) log V) with heap

Area of Usage:
    - Navigationssystem (GPS, maps, routs)
    - Networkrouting (the web)
    - Transportsystem and logistics
    - In GameDev for pathfinding and artificial intelligence
    - Time planning


Author: David
Date: 11-11-2025
"""

import heapq

def dijkstra(graph, weight, start):
    dist = {v: float("inf") for v in graph}
    dist[start] = 0
    pq = [(0, start)] # (distance, node)
    visited = set()
    
    # Uses an heapqueue to retrieve the smallest element fast without having to iterate through an entire list
    while pq: 
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        for v in graph[u]: # The heap is growing as we go. Updating if the path we have found is shorter than its current
            if dist[v] > d + weight[(u, v)]:
                dist[v] = d + weight[(u, v)]
                heapq.heappush(pq, (dist[v], v))
        
    return dist
    

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['C', 'D', 'E'],
        'C': ['B', 'D', 'E'],
        'D': ['E', 'F'],
        'E': ['F'],
        'F': []
    }

    weight = {
        ('A', 'B'): 4,
        ('A', 'C'): 2,
        ('B', 'C'): 3,
        ('B', 'D'): 2,
        ('B', 'E'): 3,
        ('C', 'B'): 1,
        ('C', 'D'): 4,
        ('C', 'E'): 5,
        ('D', 'E'): 1,
        ('D', 'F'): 2,
        ('E', 'F'): 3
    }

    print(dijkstra(graph, weight, "A"))