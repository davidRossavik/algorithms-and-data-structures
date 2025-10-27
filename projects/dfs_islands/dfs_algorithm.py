"""
Expecting:
graph: 2D-array
u: startNode
visited: set (expecting to be None the first time)
"""

def dfs(graph, x, y, visited):
    # Validity check
    if x < 0 or x >= len(graph[0]) or y < 0 or y >= len(graph):
        return
    # Check if water or already visited
    if graph[y][x] == 0 or (x, y) in visited:
        return
    # Mark cell as visited
    visited.add((x, y))
    # Explore neighbours
    dfs(graph, x + 1, y, visited) # right
    dfs(graph, x - 1, y, visited) # left
    dfs(graph, x, y + 1, visited) # down
    dfs(graph, x, y - 1, visited) # up
