"""
huffman_coding.py
------------------
Implementationof huffman Coding using a Greedy Algorithm in Python.

Background:
    - Huffman coding is a lossless data compression algorithm
    - It assigns variable-length binary codes to input symbols
      such that more frequent symbols get shorter codes
    - The result is a prefix-free binary encoding tree (node code
       is a prefix of another / doesnt start with same binary codes)

Problem:
    - given a set of characters and their frequencies, build an 
      optimal binary prefix code that minimizes the total cost:
    - Cost =  Σ (frequency(char) * length(code(char)))

Goal:
    - Minimize the average code length (bits per symbol)
    - Encode frequent symbols using fewer bits

Main Idea (Greedy Strategy):
    1. Start with all symbols as separate nodes with their frequencies.
    2. Repeatedly merge the two nodes with the lowest frequencies.
        > Create a new internal node whose frequency is the sum of the two
        > Attach the two as left and right children
    3. Continue merging until only one node (the root) remains
    4. Traverse the tree:
        > Assign 0 to left edges and 1 to right edges to form the code

Why Greed Works:
    - Greedy-choice property: Combining the two least frequent symbols first
      never prevents an optimal prefix code
    - Optimal substructure: After merging two symbols, the remaining (reduced
      alphabet) has the same optimal structure

Time Complexity:
    - Building the tree: O(n logn)
    - Generating codes: O(n)
    - Total: O(n logn)

Space Complexity:
    - O(n): For the heap (priority queue) and Huffman tree

Author: David
Date: 17-10-2025
"""

import heapq

class Node:
    def __init__(self, char, freq): #initialize
        self.char = char
        self.freq = freq
        self.left = self.right = None
    
    def __lt__(self, other): # Less than
        return self.freq < other.freq
    

def build_huffman_tree(char_freqs):
    """
    Builds the Huffman tree using a greedy algorithm

    The process:
        1. Create a lead node for each character and insert it into a min-heap
        2. While more than one node remains:
            - Extract the two nodes with smallest frequencies
            - Create a new internal node with frequency = sum of the two
            - Set the two extracted nodes as children
            - insert the new node back into the heap
        3. The remaining node is the root of the Huffman tree
    """

    # STEP 1: Create initial heap with all characters
    heap = [Node(c, f) for c,f in char_freqs]
    heapq.heapify(heap)     # Converts list into valid min-heap (O(n))

    # STEP 2: Merge the two smallest nodes until only one node remains
    while len(heap) > 1:
        # Extract two least frequent nodes (O(log n) each)
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create new internal node with combines freuency
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        #Push the merged node back into the heap (O(logn))
        heapq.heappush(heap, merged)
    
    # STEP 3: The heap now contains a single element = root of Huffman tree
    return heap[0]

def generate_codes(node, current_code="", codes=None):
    """
    Traverse the Huffman tree and generate binary codes for each character

    The traversal:
        - Follow the left child -> append '0' to the code
        - Follow the right child -> append '1' to the code
        - When a leaf node (char != None) is reached, store the code
    """

    if codes is None:
        codes = {}
    
    if node is None:
        return codes

    # Leaf node: store its character and code
    if node.char is not None:
        codes[node.char] = current_code
        return codes
    
    # Recursive traversal
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)
    return codes


if __name__ == "__main__":
    char_freqs = [('a', 5), ('b', 9), ('c', 12), ('d', 13), ('e', 16), ('f', 45)]
    root = build_huffman_tree(char_freqs)
    codes = generate_codes(root)
    print("Huffman Codes:", codes)