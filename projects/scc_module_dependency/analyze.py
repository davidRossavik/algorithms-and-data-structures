"""
Uses the graph and algorithm to find circular dependencies

Prints which files that has cycluses
"""

from graph_utils import parse_imports
from kosaraju import calculate_scc
import argparse
import os

def analyze_project(path):
    print(f"Analyzing Python project at: {path}")
    if not os.path.exists(path):
        print("Error: Path not found.")
        return
    
    graph = parse_imports(path)
    print(f"Found {len(graph)} modules.")
    sccs = calculate_scc(graph)

    circular_groups = [scc for scc in sccs if len(scc) > 1]

    if not circular_groups:
        print("\nNo circular dependencies detected!")
    else:
        print("\n Circular dependencies found:\n")
        for i, comp in enumerate(circular_groups, 1):
            print(f"{i}. {comp}")
    
    return sccs


# Debug
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect circular dependencies between Python modules.")
    parser.add_argument("path", help="Path to Python project directory.")
    args = parser.parse_args()
    analyze_project(args.path)

    # Filepath: C:\NTNU\3. Semester - Høst 25\ALG-DAT\algorithms-and-data-structures\projects\scc_module_dependency\test_project