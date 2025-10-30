""""
Kruskal's Minimum Spanning Tree Algorithm
-----------------------------------------
Problem:
    - Given a connected, undirected weighted graph
    - Find the subset of edges that connects all vertices
      with the minimum total weight and no cycles

Time complexity: O(E log E)
Space complexity: O(V)

Author: David
Date: 30-10-2025
"""

class DisjointSet:
    # Disjoint Set (Union-Find) data structure

    def __init__(self, vertices):
        # Each vertex is its own parent initially
        self.parent = {v : v for v in vertices}
        # Rank keeps the trees shallow
        self.rank = {v: 0 for v in vertices}
    
    def find(self, v):
        # Find the root (representative) of the set that vertex v belongs to
        if self.parent[v] != v:
            # Path compression: make all nodes point directly to the root
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, u, v):
        # Union two sets by rank
        root_u = self.find(u) # Find the roots
        root_v = self.find(v)

        if root_u == root_v:
            return False #already in the same set (would form a cycle)
        
        # Attach smaller tree under root of larger tree
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        
        return True
    
def kruskal(vertices, edges):
    # Compute the Minimum Spanning Tree (MST) using Kruskal's algorithm
    # Params:
        # vertices: list of vertices in the graph
        # edges: list of tuples (weight, u, v)
        # return: list of edges included in MST and total weight
    
    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[0])

    ds = DisjointSet(vertices)
    mst = []
    total_weight = 0

    for weight, u, v in sorted_edges:
        # If u and v are in different sets, include this edge in the MST
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
        
        # Early stopping: MST always has (V - 1) edges
        if len(mst) == len(vertices) - 1:
            break

    return mst, total_weight



if __name__ == "__main__":
    # Example usage
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        (1, 'A', 'B'),
        (3, 'A', 'C'),
        (3, 'B', 'C'),
        (6, 'B', 'D'),
        (4, 'C', 'D'),
        (2, 'C', 'E'),
        (5, 'D', 'E')
    ]

    mst, total = kruskal(vertices, edges)

    print("Edges in MST:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")
    print(f"Total weight of MST: {total}")

        