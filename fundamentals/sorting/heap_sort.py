"""
heap_sort.py
------------
This is an array-based Implementation of Heap Sort in Python.
The heap is inside the array.

Notes:
    - Starts with a heap, and gradually builds the sorted array from backwards. Making the heap smaller for each iteration.
    - Indexes for relations:
        - Parents: floor(i // 2)
        - Child-left: 2*i + 1
        - Child-right: 2*i + 2 

The main idea:
    1. Builds a Max-Heap
    2. Iterates backwards over the indexes of the heap:
        3. Switches the root (biggest element) with the last index in the array
        4. Reduces the heap by 1 (that space is used by sorted last number)
        5. Repares the root with MAX-HEAPIFY

Time Complexity:
    - Iterating through each rootnode: O(n)
        - Calling Max_Heapify for each rootnode: O(log n)
    - Total: O(n*log n)

Space Complexity:
    - O(log n) for recursion stack (each recursion allucates a new stack frame with variables, return adress ...)
    - O(1) for auxiliary space (hjelpeplass)

Author: David
Date: 11-10-2025
"""

from math import ceil, log2


def heap_sort(A):
    n = len(A)

    #Builds Max-Heap
    Build_Max_Heap(A, n)

    #Iterates through, placing rootnodes in sorted order in the back of the array
    for i in range(n - 1, 0, -1):   #O(n)
        A[0], A[i] = A[i], A[0]
        n -= 1
        Max_Heapify(A, 0, i)    #O(logn)
        


"""
Max_Heapify
-----------
Goal: Let the node sink to its correct spot, where it its larger than its children

The main idea:
    1. Finds left and right children
    2. If left-child is bigger than the current node, set left-node as temp_max
    3. Check right-child, and set as the new temp_max if it is bigger than current node and temp_max
    4. If temp_max found, switch current node and biggest child
    5. Recursively call itself with the same node til it can't go further down    
"""

def Max_Heapify(A, i, heap_size):
    # Define index of left and right child
    leftIndex = 2 * i + 1
    rightIndex = 2 * i + 2

    # Checking if left-child is bigger than current Node
    if leftIndex < heap_size and A[leftIndex] > A[i]:
        temp_max = leftIndex
    else:
        temp_max = i
    
    # Checking if right-child is bigger than current Node and left-child
    if rightIndex < heap_size and A[rightIndex] > A[temp_max]:
        temp_max = rightIndex
    
    # If one of the children are bigger, then switch and call itself on the next index
    if temp_max != i:
        A[i], A[temp_max] = A[temp_max], A[i]
        Max_Heapify(A, temp_max, heap_size)     #O(logn) worst-case: height of the heap

"""
Build_Max_Heap
--------------
Goal: Build a max-heap from an unsorted array

The main idea:
    1. Uses Max_Heapify for each node recursively
"""

def Build_Max_Heap(A, n):

    for i in range(n // 2 - 1, -1, -1):     #O(n)
        Max_Heapify(A, i, n)


"""
This one is just for printing the heap.
Better visualization
"""

def print_heap_tree(A):
    n = len(A)
    level = 0
    next_level = 2 ** level
    i = 0
    while i < n:
        # Find the elements on this level
        level_nodes = A[i:i + next_level]
        spacing = " " * (2 ** (ceil(log2(n + 1)) - level))
        print(spacing.join(map(str, level_nodes)))
        i += next_level
        level += 1
        next_level = 2 ** level


if __name__ == "__main__":
    test_heap = [1, 5, 8, 3, 2, 10, 15, 9, 11, 4]
    print("-----------Before Sorting-----------")
    print(test_heap)
    print()
    print_heap_tree(test_heap)
    heap_sort(test_heap)
    print("----------After sorting------------")
    print(test_heap)
    print()

