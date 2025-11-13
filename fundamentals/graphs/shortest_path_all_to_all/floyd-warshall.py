"""
Floyd Warshall
---------------
"What is the shortest path from node i to node j, when we are allows to use all nodes in between"

The main idea:
    - Builds up gradually (first you are allowed to use no in-between-nodes, then 1, then 2....)
    - Tries a mellom-node" k at a time, and checks if it gives a shorter path from i to j and the previous known

Time Complexity:
    - O(n^3)

Author: David
Date: 13-11-2025
"""

def floyd_warshall(W):
    n = len(W)
    d = [row[:] for row in W] # copy

    for k in range(n): #mellomnode
        for i in range(n): #startnode
            for j in range(n): #sluttnode
                # Forsøk å gå via k
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    
    return d

if __name__ == "__main__":
    INF = float("inf")

    # 0 -> 1 koster 10 direkte
    # 0 -> 2 koster 2
    # 2 -> 1 koster 3
    # Korteste vei 0->1 = 2+3 = 5
    W = [
        [0,   10,  2],
        [INF, 0,   INF],
        [INF, 3,   0]
    ]

    dist = floyd_warshall(W)

    for row in dist:
        print(row)