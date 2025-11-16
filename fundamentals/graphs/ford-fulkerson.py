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
        for v in graph[u]:
            if v not in parent and residual[u].get(v, 0) > 0:
                parent[v] = u
                if v == sink:
                    return parent
                queue.append(v)
        return None
    
