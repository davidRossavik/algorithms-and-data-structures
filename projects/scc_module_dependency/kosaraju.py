"""
Implements the SCC algorithm with the help of DFS

Returns: a list off SCCs
"""

def dfs(graph, u, visited, stack):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs(graph, v, visited, stack)
    stack.append(u)

def transpose(graph):
    g_t = {u: [] for u in graph}
    for u in graph:
        for v in graph[u]:
            g_t[v].append(u)
    return g_t

def dfs_component_collect(graph, u, visited, component):
    visited.add(u)
    component.append(u)
    for v in graph[u]:
        if v not in visited:
            dfs_component_collect(graph, v, visited, component)



def calculate_scc(graph):
    visited = set()
    stack = []
    
    for u in graph:
        if u not in visited:
            dfs(graph, u, visited, stack)
    
    g_t = transpose(graph)

    visited.clear()
    SCCs = []
    while stack:
        u = stack.pop()
        if u not in visited:
            component = []
            dfs_component_collect(g_t, u, visited, component)
            SCCs.append(component)
    
    return SCCs


    