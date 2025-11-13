"""
Faster All-Pair Shortest Path
------------------------------
Increases the number of edges exponentially instead of one by one.
First we know all 1-edge paths, then 2-edge paths, then 4-edge paths, then 8-edge paths ...
Works because the min-plus matrixproduct by itself

The main idea:

Time Complexity:
    - O(n^3 logn)

Author: David
Date: 13-11-2025
"""

from extend_shortest_path import extend_shortest_paths

def faster_apsp(W, n):
    # L = shortest paths with at most 1 edge
    L = [row[:] for row in W]
    m = 1 #Number of edges L can represent

    while m < n - 1:
        #Compute L' = L x L
        L_prime = [[float("inf")] * n for _ in range(n)]
        extend_shortest_paths(L, L, L_prime, n)
        L = L_prime
        m *= 2
    
    return L



if __name__ == "__main__":
    INF = float("inf")
    
    W = [
        [0,   3,  10],
        [INF, 0,   4],
        [INF, INF, 0]
    ]
    n = len(W)

    dist = faster_apsp(W, n)

    print("ALL PAIRS SHORTEST PATHS (FASTER-APSP):")
    for row in dist:
        print(row)
