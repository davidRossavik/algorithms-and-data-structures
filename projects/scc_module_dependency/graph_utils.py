"""
Reads all the .py-files and builds a graph (nodes + edges)

Result: Returns a directed graph over imports 
Returns: dict[str, list[str]]
"""

import os, re
from collections import defaultdict

def parse_imports(base_path):
    graph = defaultdict(list)

    for root, _, files in os.walk(base_path):
        for f in files:
            if f.endswith('.py'):
                file_path = os.path.join(root, f)
                module = os.path.relpath(file_path, base_path)
                graph[module]
                with open(file_path, 'r', encoding='utf-8') as source:
                    for line in source:
                        target = None
                        match = re.match(r'^\s*(?:from|import)\s+([\w\.]+)', line)
                        if match:
                            target = match.group(1).split('.')[0] + '.py'
                            if target != module:
                                graph[module].append(target)
    return graph



# Debugging
if __name__ == "__main__":
    path = r"C:\NTNU\3. Semester - Høst 25\ALG-DAT\algorithms-and-data-structures\projects\scc_module_dependency\test_project"
    print("----------")
    print(path)
    print("Path exists:", os.path.exists(path))
    print("----------\n")
    graph = parse_imports(path)
    print("Graph of imports:", graph)
    
