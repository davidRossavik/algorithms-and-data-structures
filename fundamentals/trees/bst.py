"""
bst.py
-------
Implementation of a Binary Search Tree in Python.
The file also contains the fundamental operations for BST:

Note:
    - Worst case for all operations is O(n) (because worst-case height is linear)
    - Random input-permutation gives logarithmic height
    - We can balance after each insertion and deletion, in logarithmic time

INORDER-TREEWALK: 
    > Functionality: Visits all nodes in sorted order (left -> node -> right == least -> mid -> most)
    > Going all the way down to the left node first, then to the parent, then to the right
    > The right node then goes all the way down to the left if it can, then parent, then right...
    > Appends the entire binary search tree as a sorted list
    > Time Complexity: O(n)

TREE-INSERT:
    > Functionality: Looks for an open spot and inserts the node under its correct parent
    > Checks the key value with all of the nodes, traverses down the tree until it finds a parent with no children
    > Checks if the new node should be left- or right-child
    > Inserts the new node in its correct position
    > Time Complecity: O(h)

TREE-SEARCH:
    > Functionality: Finds the key in input through recursion
    > Returns the key or none if current nodes key matches input-key (Base-case)
    > Calls itself on the left- or right-child of current node (based on input-key value in comparison to current nodes key-value)
    > (Has a iterative version too)
    > Time Complexity: O(h)

TREE-MINIMUM / -MAXIMUM:
    > Functionality: Traverses all the way down to the left or right node of the tree
    > This node is the minimum / maximum
    > Time Complexity: O(h)

TREE-SUCCESSOR:
    > Functionality: Finds the next node in the inorder-order (key that is the next sorted element bigger)
    > Important to remember: L < N < R
    > First try to get the left-most child of right-child (the smallest larger element than node)
    > Then try to get the first parent that has current_node as left-child (if node is left-child then parent is next)
    > Time Complexity: O(h)

TREE-PREDECCESSOR:
    > Functionality: Finds the previous node in the inorder-order (key that is before the node in a sorted list)
    > First try to get the right-most child of left-child (the biggest element smaller than node)
    > Then try to get the first parent that has current-node as a right-child (if node is right-child then parent is previous)
    > Time Complexity: O(h)

TRANSPLANT:
    > Functionality: Replace a subtree with another subtree
    > Replaces a subtree (with rote in node u) with another subtree (root in node v)
    > Updates the parent-referances correctly
    > Handles the special-case of u beeing the root of the whole tree
    > Time Complexity: 

TREE-DELETE:
    > Functionality: Search for where the Node is and deletes it. Afterwards it needs to repair the tree so it maintains a bst-structure
    > Doesnt need to know the details of this one
    > When a node with 1 child is deleted, it removes the node and replaces it with the root of one of the nodes subtree
    > When a node with 2 children is deleted, it replaces itself with its successor (so that left subtree is less still, and right subtree is more still)
    > Time Complexity: O(h)

Author: David
Date: 12-10-2025
"""

# Node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
    
    def __repr__(self):
        return f"Node({self.key})"
    

# Binary Search Tree
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # -------- Traversing -------------
    def inorder_walk(self, node = None):
        # Left -> Node -> Right

        # Initializing node to be the root
        if node is None:
            node = self.root
        if node is None:
            return []
        
        result = []
        # Going all the way down to the left node (smallest element)
        if node.left:
            result += self.inorder_walk(node.left)
        
        # Visit the parent node to the smallest left node
        result.append(node.key)

        # Visit the right-child of the last parent and appending that child and its subtree.
        if node.right:
            result += self.inorder_walk(node.right)
        
        return result
    
    # --------- INSERTING ------------
    def tree_insert(self, key):
        new_node = Node(key)
        parent = None

        # Finding the first parent that has no child where value is supposed to be (while current is not None)
        current = self.root
        while current:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        
        new_node.parent = parent

        # Checking if the new node should be left or right-child to the parent based on key-value
        if parent is None:
            self.root = new_node  #If parent=NIL then the new node is the root
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        return new_node
    
    # --------- SEARCHING -----------
    def tree_search(self, node, key):
        # Base-case: Return none or that the root x is the answer
        if node == None or node.key == key:
            return node
        
        # Searches recursively through either of current nodes children
        if k < node.key:
            return self.tree_search(node.left, key)
        else:
            return self.tree_search(node.right, key)
    
    def iterative_tree_search(self, node, key):
        while node != None and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node
    
    # ------ MINIMUM / MAXIMUM ---------
    def tree_minimum(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def tree_maximum(self, node):
        current = node
        while current.right:
            current = current.right
        return current
    
    # ------ Successor / Predecessor --------
    def tree_successor(self, node):
        # Finds the next left-child from current nodes right.child
        if node.right:
            return self.tree_minimum(node.right)
        
        # Checks that the node is the left child of its parent (left-child means that parent is bigger)
        # Traverses up to the first parent that has its x-generation parent as a left-child (can go up to the root => parent == None)
        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = parent.parent
        return parent
    
    def tree_predecessor(self, node):
        #Finds the next left-childs max (deepest-right-child of left-child) (left-child is less than parent)
        if node.left:
            return self.tree_maximum(self, node.left)
        
        # Finds the parent that has current node as its right-child
        parent = node.parent
        while parent and node == parent.left:
            node = parent
            parent = parent.parent
        return parent

    # -------- TRANSPLANT ------------
    def _transplant(self, u, v):
        # If u is the root
        if u.parent is None:
            self.root = v

        # If u is left-child of its parent
        elif u == u.parent.left:
            u.parent.left = v

        # If u is right-child of its parent
        else:
            u.parent.right = v
        
        #Update the parent-referance to v
        if v is not None:
            v.parent = u.parent
    
    # --------- DELETE ----------
    def tree_delete(self, z):
        # If no left-child: replaces the node with the root of right-child and moves everything under one up
        if z.left is None:
            self._transplant(z, z.right)
        # if no right-child: replaces the node with the root of left-child and moves everyting under one up
        elif z.right is None:
            self._transplant(z, z.left)
        
        # If z has both children
        else:
            # Find the successor
            y = self.tree_minimum(z.right)
            # If the sucessor is not the direct child of z
            if y.parent != z:
                # Replace the successor with its right-child
                self._transplant(y, y.right)
                # Place z's right-subtree as y's right-subtree
                y.right = z.right
                y.right.parent = y
            
            # Replace z with the successor y
            self._transplant(z, y)
            # Put z's left-subtree as y's left-subtree
            y.left = z.left
            y.left.parent = y
    


# --- Example Usage ---
if __name__ == "__main__":
    bst = BinarySearchTree()
    for k in [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]:
        bst.tree_insert(k)

    #Traversing
    print("Inorder:", bst.inorder_walk())
    print("----------------------------")

    #Searching
    node = bst.tree_search(bst.root, 7)
    node2 = bst.iterative_tree_search(bst.root, 7)
    if node: 
        print("Key found recursively:", node)
        print("Key found iteratively:", node2)
    else:
        print("Key not found:(")
    print("----------------------------")
    
    #Min/Max
    print("Minimum:", bst.tree_minimum(bst.root))
    print("Maximum:", bst.tree_maximum(bst.root))
    print("----------------------------")

    #Successor/Predeccesor
    nodeTest = bst.iterative_tree_search(bst.root, 7)
    print("Successor to 7:", bst.tree_successor(nodeTest))
    print("Predeccessor to 7:", bst.tree_predecessor(nodeTest))

    


        
        
    
