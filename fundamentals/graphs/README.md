
# Graphs

## Topological Sort

Creates an order of nodes so that all arrows (edges) is pointing forward

- Topological sorting is used at direct, acyclic graphs (DAGs)
- Typical use: dependencies between tasks, planning, course-order

Topological sorting is a spesific problem that can be solved with the help of DFS or BFS

### DFS

Depth-First-Search based methods uses Finish-time to find the order.
We sort the nodes in decreasing order after finishtime. 
- A node is finished when all its descendants is finished
- Explores all the children and granchildren of a node 
- Uses a LIFO-queue (Last in - first out), a stack more spesific, to keep track of which nodes that need to be treated

### BFS

Breadth-First-Search uses indegree to decide which nodes that should be taken out next
- Explores all the nodes on one level, and then moves on the the next level
- Uses a Fifo-queue (First in - first out) to keep track of which nodes that needs to be treated