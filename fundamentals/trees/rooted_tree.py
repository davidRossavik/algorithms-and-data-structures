"""
rooted_tree.py
---------------
Simple Implementation of a rooted tree in Python.

Author: David
Date: 11-10-2025
"""

class Node:
    def __init__(self, key):
        self.key = key          # The value
        self.children = []      # List of children
        self.parent = None      # pointer to parent

class rooted_tree:
    def __init__(self, root_value):
        self.root = Node(root_value)
    
    def add_child(self, parent, child_value):
        new_child = Node(child_value)
        new_child.parent = parent
        parent.children.append(new_child)
        return new_child
    
    

def print_tree(node, level=0):
    print("  " * level + str(node.key))
    for child in node.children:
        print_tree(child, level + 1)

# Test
if __name__ == "__main__":
    # Create a tree
    tree = rooted_tree("A")  # Root node
    
    # Add children to root
    child_b = tree.add_child(tree.root, "B")
    child_c = tree.add_child(tree.root, "C")
    child_d = tree.add_child(tree.root, "D")
    
    # Add grandchildren
    tree.add_child(child_b, "E")
    tree.add_child(child_b, "F")
    
    tree.add_child(child_c, "G")
    tree.add_child(child_c, "H")
    tree.add_child(child_c, "I")
    
    child_j = tree.add_child(child_d, "J")
    
    # Add great-grandchildren
    tree.add_child(child_j, "K")
    tree.add_child(child_j, "L")
    
    print("Tree structure:")
    print_tree(tree.root)