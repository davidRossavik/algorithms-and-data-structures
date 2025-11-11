"""
(Directed Acyclic Graph)-Shortest Path implementation in Python
----------------------------------------------------------------
One of three algorithms to find the shortest path from one to all (SSSP - Single source shortest Path)

Is used when the graph is directed and with no cycles. 

DAG-Shortest-Path is very useful in situation where tasks or processes has to happen
in a particular order, where you wish to find the minimal cost / time to get from
start to finish.

Typical Use:
    - Find shortest (or longest) time to finish a project with dependencies between tasks
    - Find the order on files that needs to be compiles - a file must be built after what it is dependent on

The main idea:
    1. Topological sort of the graph (every edhe (u,v) goes from a node that comes before v)
        > That wat we know that when we reach v, we have already found the shortest path to all the predecessors
    2. Initialize the distances
    3. Go through the nodes in topological order

Time Complexity:
    - Topological sort: O(2V)    

Author: David
Date: 11-11-2025
"""

from collections import deque

def topological_sort(graph): # Recursive
    visited = set()
    order = []

    def dfs(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
        order.append(u)
    
    for u in graph:
        if u not in visited:
            dfs(u)

    return order[::-1] #Turns the array to the right order

def topological_sort_kahn(graph): 
    indegree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    
    queue = deque([u for u in graph if indegree[u] == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    return order

def dag_shortest_path(graph, weight, start):
    order = topological_sort(graph)
    dist = {v: float("inf") for v in graph} # Initialize to infinity for all nodes in graph
    dist[start] = 0

    for u in order:
        for v in graph[u]:
            if dist[v] > dist[u] + weight[(u, v)]: #Relaxation
                dist[v] = dist[u] + weight[(u, v)]
    return dist


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": []
    }
    weight = {
        ("A", "B"): 3,
        ("A", "C"): 2,
        ("B", "D"): 4,
        ("C", "D"): 1
    }

    print(dag_shortest_path(graph, weight, "A"))






