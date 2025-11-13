"""
Transitive Closure
-------------------
"Can I even get from node A to node B?" (No matter how far and the cost)

The main idea:
    - Uses a boolean matrix for 1="can reach" and 0="cannot reach"
    - Builds up knowledge gradually by adding more and more nodes as legal mellomnodes
    1. Starts with the matrix T where: 
            > T[i][j] = True if the graph has a direct edge i -> j
            > T[i][i] = True (a node can always reach itself)
    2. Continues by checking if it may work if we try to go through node 1 first
            > First we may just use {0} then {0, 1} then {0, 1, 2} then {0, ..., n-1}
    3. When we are done we have all the reachinformation that exists in the graph
    - "If I can go from i to k, and from k to j, then I can go grom i to j


Time Complexity:
    -

Author: David
Date: 13-11-2025
"""

def transitive_closure(graph):
    # Graph: adjacency matrix with True/False values
    # Returns: transitive closure matrix T

    n = len(graph)

    T = [[graph[i][j] for j in range(n)] for i in range(n)] # T = graph (copy)

    for i in range(n):
        T[i][i] = True
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                T[i][j] = T[i][j] or (T[i][k] and T[k][j])

    return T




if __name__ == "__main__":
    # Example graph:
    # 0 -> 1
    # 1 -> 2
    # 0 -> 3 (direct)
    graph = [
        [False, True,  False, True ],
        [False, False, True,  False],
        [False, False, False, False],
        [False, False, True,  False],
    ]

    T = transitive_closure(graph)

    print("Transitive Closure Matrix:")
    for row in T:
        print(row)
