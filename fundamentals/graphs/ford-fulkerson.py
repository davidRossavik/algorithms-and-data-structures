"""
Ford-Fulkerson (Edmonds-Karp) - Maximum Flow in a Directed Graph
--------------------------------------------------------------

Goal:
    - Compute the maximum possible flow from a source node s to a sink node t
      in a directed graph where each edge has a capacity.

Key ideas:
    - Start with zero flow on all edges
    - As long as there exists an "augmenting path" from s to t
      in the residual graph, we can increase the total flow.
    - Residual graph:
        > For each edge (u -> v), the residual capacity is:
                capacity(u, v) - flow(u, v)
        > Every forward edge also has a backward edge, whose residual
          capacity equals current flow on u -> v
          This indicated how much flow can be canceled or pushed back.

Implementation details:
    - Graph representation:
        graph[u] = list of outgoing neighbours v
        capacity[u][v] = capacity of edge u -> v (0 if no edge)
    
    - The algorithm constructs a residual graph and updates it every time 
      we find an augmenting path.

    - We use BFS to find augmenting paths, making this the Edmonds-Karp
      version of Ford-Fulkerson.

Complexity:
    Edmonds-Karp runs in: O(V * E^2)

Variables inside the implementation:
    residual[u][v]: residual capacity of edge u -> v
    parent:         used by BFS to reconstruct the augmenting path
    bottleneck:     the minimum residual capacity on the found path


Author: David + ChatGPT :)
Date: 16-11-2025
"""

from collections import deque
from typing import Dict, List, Tuple, Any

def _bfs_find_path(
        residual: Dict[Any, Dict[Any, float]],
        graph: Dict[Any, List[Any]],
        source: Any,
        sink: Any,
) -> Dict[Any, Any] | None:
    """
    BFS on the residual graph to find and augmenting path from source to sink.

    Returns:
        parent: dict mapping each node to its predecessor, so the path can be reconstructed backwards from sink
        Returns None if no path is available
    """
    parent = {source: None}
    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in residual[u]:
            if v not in parent and residual[u].get(v, 0) > 0:
                parent[v] = u
                if v == sink:
                    return parent
                queue.append(v)
    return None
    

def ford_fulkerson_max_flow(
        graph: Dict[Any, List [Any]],
        capacity: Dict[Any, Dict[Any, float]],
        source: Any,
        sink: Any,
) -> Tuple[float, Dict[Any, Dict[Any, float]]]:
    """
    Compute maximum flow from source to sink using the Ford-Fulkerson method
    (specifically the BFS-based Edmonds-Karp version).

    Parameters:
        graph:  adjacency list
        capacity: capacity[u][v] = capacity of edge u -> v
        source: source node
        sink: sink node
    
    Returns:
        max_flow: numeric maximum flow
        flow: actual flow per edge in the final solution
    """

    # 1. Initialize residual graph
    residual: Dict[Any, Dict[Any, float]] = {}
    for u in graph:
        residual[u] = {}
    for u in graph:
        for v in graph[u]:
            residual[u][v] = capacity[u][v]
            if v not in residual:
                residual[v] = {}
            if u not in residual[v]:
                residual[v][u] = 0.0 #Backwards edge
    
    max_flow = 0.0

    # 2. Search for augmenting paths
    while True:
        parent = _bfs_find_path(residual, graph, source, sink)
        if parent is None:
            break # No more augmenting paths

        # Reconstruct path
        path = []
        v = sink
        while v != source:
            u = parent[v]
            path.append((u, v))
            v = u
        path.reverse()

        # Determine bottleneck
        bottleneck = min(residual[u][v] for u, v in path)

        # update residual capacities
        for u, v in path:
            residual[u][v] -= bottleneck
            residual[v][u] += bottleneck

        max_flow += bottleneck

    # 3. Extract final flow
    flow: Dict[any, Dict[Any, float]] = {u: {} for u in graph}
    for u in graph:
        for v in graph[u]:
            original_cap = capacity[u][v]
            used = original_cap - residual[u].get(v,0)
            flow[u][v] = used
    
    return max_flow, flow



if __name__ == "__main__":
    # Example:
    # Graph:
    #   s -> a (3), s -> b (2)
    #   a -> b (1), a -> t (2)
    #   b -> t (3)

    graph = {
        "s": ["a", "b"],
        "a": ["b", "t"],
        "b": ["t"],
        "t": [],
    }

    capacity = {
        "s": {"a": 3, "b": 2},
        "a": {"b": 1, "t": 2},
        "b": {"t": 3},
        "t": {},
    }

    max_flow, flow = ford_fulkerson_max_flow(graph, capacity, "s", "t")
    print("Maximum flow:", max_flow)
    print("Flow per edge:")
    for u in flow:
        for v in flow[u]:
            if flow[u][v] > 0:
                print(f"{u} -> {v}: {flow[u][v]}")