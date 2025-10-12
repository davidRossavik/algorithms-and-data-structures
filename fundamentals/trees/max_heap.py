"""
max_heap.py
------------
Implementation of the datastructure Max-Heap in python.


Author: David
Date: 12-10-2025
"""

class MaxHeap:
    # Constructor
    def __init__(self, array=None):
        self.heap = array or []
        if self.heap:
            self.build_max_heap()
    
    # Relations
    def left(self, i): return 2*i + 1
    def right(self, i): return 2*i + 2
    def parent(self, i): return (i - 1) // 2

    def max_heapify(self, i):
        """ Secures that heap-property applies to the node on index i"""
        length = len(self.heap)
        leftIndex, rightIndex = self.left(i), self.right(i)
        largestIndex = i

        # Checks if either of the children are larger and puts their index as the largest in that case
        if leftIndex < length and self.heap[leftIndex] > self.heap[largestIndex]:
            largestIndex = leftIndex
        if rightIndex < length and self.heap[rightIndex] > self.heap[largestIndex]:
            largestIndex = rightIndex
        
        # If it finds a larger child, it switches with the childs position
        if largestIndex != i:
            self.heap[i], self.heap[largestIndex] = self.heap[largestIndex], self.heap[i]
            self.max_heapify(largestIndex) # Calls itself recursively on the nodes switched place (check if it smaller than its next children)
        
    def build_max_heap(self):
        """ Builds a max heap from an unsorted array """
        n = len(self.heap)
        for i in range(n//2 - 1, -1 , -1):
            self.max_heapify(i) # Max-heapifyer alle elementer i arrayen utenom løvnodene (derfor // 2), for de kan ikke ha barn å sammenligne med
        
    def extract_max(self):
        """ Removes and returns the biggest element """
        if not self.heap:
            raise IndexError("Heap is empty")
        
        # Defines max_val as root
        max_val = self.heap[0]
        # Switches the largest element with the smallest
        self.heap[0] = self.heap[-1]
        # Removes the last (which is now the biggest)
        self.heap.pop()
        # Max-heapify to move the smallest element down
        if self.heap:
            self.max_heapify(0)
        return max_val
    
    def insert(self, key):
        """ Puts a new element in the heap"""
        self.heap.append(float('-inf')) # Puts (-infinity) as the last value
        self.increase_key(len(self.heap) - 1, key) # Puts input-key as the new value and bubbles it to its correct position
    
    def increase_key(self, i, key):
        """ Increases the value of a node and moves it upward"""
        if key < self.heap[i]:
            raise ValueError("New key is smaller than current key")
        self.heap[i] = key
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            parent = self.parent(i)
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
    
    # toString
    def __repr__(self):
        return f"MaxHeap({self.heap})"


if __name__ == "__main__":
    h = MaxHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    print("Build heap:", h)
    print("Extract Max-value:", h.extract_max())
    print("Heap now:", h)
    h.insert(15)
    print("After insertion of 15:", h)
        

