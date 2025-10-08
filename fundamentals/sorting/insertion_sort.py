"""
insertion_sort.py
-----------------
Simple implementation of insertion sort in Python.

The main idea:
    1. Start with second element in the list
    2. Compare it to the elements before it
    3. Insert it into its correct position among the previous elements
    4. Repeat for each element until the whole list is sorted
    - Like sorting a hand of playing cards: pick one card at a time and place 
      it in the right position relative to the cards already in your hand.

Time Complexity:
- Outer Loop runs (n-1) times -> O(n)
- Inner loop: shifts elements greater than key -> O(n) in worst case
- Total: O(n) * O(n) = O(n^2)

Author: David
Date: 08-10-2025
"""

def insertion_sort(list):
    n = len(list)

    for i in range(1, n):   #O(n)
        key = list[i]   # Element to insert in sorted part
        j = i - 1

        # Move elements that are greater than key to one position ahead
        # Each comparison and shift costs O(1)
        while j >= 0 and list[j] > key:     #Worst case: O(n)
            list[j + 1] = list[j]
            j = j - 1
        
        # Insert key into its correct position
        list[j + 1] = key
    
    return list

if __name__ == "__main__":
    example = [64, 25, 12, 22, 11]
    print("Before sorting:", example)
    sorted_list = insertion_sort(example)
    print("After sorting:", sorted_list)