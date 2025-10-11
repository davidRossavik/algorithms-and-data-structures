"""
first_child_next_sibling.py
----------------------------
Simple implementation of a rooted tree where each node points to
its first child and next sibling. Classic way of representing rooted 
trees with an arbitrary number of children

Works nicely with linked list for siblings

Author: David
Date: 11-10-2025
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.first_child = None
        self.next_sibling = None

class RootedTree:
    def __init__(self, root_value):
        self.root = Node(root_value)
    
    def add_child(self, parent, child_value):
        # Adds a child under a given parent-node
        new_child = Node(child_value)
        if not parent.first_child:
            parent.first_child = new_child
        else:
            # Find the last sibling and put it after it
            current = parent.first_child
            while current.next_sibling:
                current = current.next_sibling
            current.next_sibling = new_child
        return new_child
    
    def traverse_preorder(self, node):
        # Visit parent before children
        if node:
            print(node.value)
            self.traverse_preorder(node.first_child)
            self.traverse_preorder(node.next_sibling)


tree = RootedTree("ROOT")
b = tree.add_child(tree.root, "1. Generation child")
c = tree.add_child(tree.root, "1. Generation sibling 1")
d = tree.add_child(b, "2. Generation child")
e = tree.add_child(b, "2. Generation sibling 1")
f = tree.add_child(b, "2. Generation sibling 2")
tree.traverse_preorder(tree.root)