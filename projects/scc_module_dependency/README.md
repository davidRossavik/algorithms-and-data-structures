
# Module Dependency Analyzer (SCC Project)

##  Issue

Big Python-projects often have complex dependencies between modules. When modules import each other, circular dependencies arises, which can lead to:
- Difficult testing
- Errors on loading (`ImportError`)
- Lack of modularity and bad architecture

This project uses Kosarajus algorithm to discover such mutual dependencies (SCC) in a Python-project


## My solution
1. Gather Data
    - Go through all the .py-files in a project
    - Read lines that contains import or from ... import ...
    - Use that to build a graph:
      - Each node is a file
      - Each edge is an import statement
    - Ends up with a directed graph where the direction shows who imports who
2. Find connected groups (SCC)
    - Uses Kosaraju's algorithm on the graph of files and imports to find strongly connected components:
      - If a SCC has more than one file, it means that the project contains circular dependencies
3. Present the results
    - When the SCCs is found I show:
      - Which files that are indepdendent
      - Which files that are mutual dependent

<br>

## Theoretical background

### Strongly Connected Components (SCC)
A SCC is a group of nodes in a directed graph where all the vertices can reach each other. <br>
In moduledependencies this means that the files import each other directly or indirectly.

Kosaraju's algorithm finds SCCs like this:
1. Run DFS on the graph and register the finish-times
2. Turn all the edges (transpose the graph)
3. Run DFS again in decreasing finish-time-order
    - Each DFS is one SCC


### Typical Use
- Analyze big Python-projects for architectural weaknesses
- Discover unintentional circular imports
- Visualize modules dependencies
- Automated qualitycontroll in CI/CD

### Examples of real problems
- `a.py` imports `b.py` mwhile `b.py` imports `a.py`
- `models.py` and `views.py` calls each other
- An "utilites"-module that imports core-classes

# How To Run
1. Navigate into `scc_module_dependency` in the terminal (use **cd**)
2. Run `python analyze.py test_project/` in the terminal


