"""
Extend-Shortest-Path Implementation in Python
----------------------------------------------
W: Weightmatrix
L: Matrix where shortes path from i to j with the maximum of r edges
L' or M: New matrix that will be the shortest path from i to j with maximum of r + 1 edges

The main idea:
    1. You already know the shortest path from node i to k when you use r edges (matrix L)
    2. You also know how much a single edge from k to j costs (from matrix W)
    3. For every possible startnode i and finishnode (since its all to all)
    4. We try to go from i to k using up to r edges (from L), then use 1 new edge from k to j (from W).
    6. Choose the cheapest one of these
    7. Results: a new matrix that tells you the shortest path from i to j with one edge more than before

Time Complexity:
    - O(n^3)

Author: David
Date: 13-11-2025
"""

def extend_shortest_paths(L, W, L_prime, n):
    # Calculate every cell of the matrix
    for i in range(n):
        for j in range(n):
            # min_k (L[i][k] + W[k][j])
            best = float("inf") # Shortest path we have seen so far in the cell (nothing is found)
            
            # Tries to go from i to j
            #       - By first going from i to k with r edges
            #       - Then going from k to j with +1 edges
            #       - If weight smaller, then update the best
            for k in range(n):
                cand = L[i][k] + W [k][j]
                if cand < best:
                    best = cand
            L_prime[i][j] = best


if __name__ == "__main__":
    INF = float("inf")
    
    # Simple graph:
    # 0 -> 1 (weight 3)
    # 1 -> 2 (weight 4)
    # 0 -> 2 (weight 10)
    W = [
        [0,   3,  10],
        [INF, 0,  4],
        [INF, INF, 0]
    ]

    # L = W (shortest paths using at most 1 edge)
    L = [row[:] for row in W]

    # Prepare empty L_prime
    L_prime = [[INF] * 3 for _ in range(3)]

    extend_shortest_paths(L, W, L_prime, 3)

    print("L' (shortest paths with at most 2 edges):")
    for row in L_prime:
        print(row)
