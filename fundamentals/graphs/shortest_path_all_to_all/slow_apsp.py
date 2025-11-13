"""
Slow ALL-Pais Shortest Paths
-----------------------------
Find the shortest paths from all nodes to all nodes by increasing the 
number of allowed edges one by one.

The main idea:
    1. "What is the shortes path between ALL nodes"?
    2. Here we try ALL different paths that uses 1, 2, 3, ..., n-1 edges
            - Until we have tried ALL possible paths that we can do without visiting a node twice
    3. 

Time Complexity:
    - O(n^4)

Author: David
Date: 13-11-2025
"""
from extend_shortest_path import extend_shortest_paths

def slow_apsp(W, n):
    # L = W = shortest paths with at most 1 edge
    L = [row[:] for row in W]

    # Compute L^(2), L^(3), ..., L^(n-1)
    for _ in range(2, n):
        L_prime = [[float("inf")] * n for _ in range(n)]
        extend_shortest_paths(L, W, L_prime, n)
        L = L_prime
    
    return L

if __name__ == "__main__":
    INF = float("inf")

    # Simple graph:
    # 0 -> 1 (3)
    # 1 -> 2 (4)
    # 0 -> 2 (10)
    W = [
        [0,   3,  10],
        [INF, 0,   4],
        [INF, INF, 0]
    ]

    n = len(W)
    dist = slow_apsp(W, n)

    print("ALL PAIRS SHORTEST PATHS (SLOW-APSP):")
    for row in dist:
        print(row)

