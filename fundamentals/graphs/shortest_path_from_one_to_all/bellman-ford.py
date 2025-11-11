"""
Bellman-Ford Implementation in Python
---------------------------------------
Goal: Find the shortest way from one startnode to all other nodes
        -> Also when the graph has negative edge-weight

Area of Usage:
    - Shortest Path between computers in a network
    - Graphs with negative weights
    - Discover negative cycles
    - Like an algortihm that "spreads" knowledge about the shortest way in a system

Time Complexity:
    - Relax: E * (V-1) = Θ(VE)
    - Check negative cycles: O(E)
    = Total: Θ(VE) + O(E) = Θ(VE)

Author: David
Date: 11-11-2025
"""

def bellman_ford(graph, weight, start):
    #Initialize
    dist = {v: float("inf") for v in graph }
    dist[start] = 0

    # Update shortest path
    for _ in range(len(graph) - 1): # Repeat V - 1 times (this is what we can maximum do if there are no negative cycles)
        for u in graph:
            for v in graph[u]:
                if dist[v] > dist[u] + weight[(u, v)]:
                    dist[v] = dist[u] + weight[(u, v)]
    
    # Check for negative cycle
    for u in graph:
        for v in graph[u]:
            if dist[v] > dist[u] + weight[(u, v)]: # If it is possible to update then we can update forever
                raise Exception("Negative cycle discovered!")
    return dist

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['B', 'D'],
        'D': []
    }

    weight = {
        ('A', 'B'): 4,
        ('A', 'C'): 2,
        ('C', 'B'): -1,
        ('B', 'D'): 2,
        ('C', 'D'): 3
    }

    print(bellman_ford(graph, weight, "A"))
