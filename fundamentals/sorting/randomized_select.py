"""
randomized_select.py
--------------------
Implementation of Randomized Select searching algorithm in Pyhthon.
Uses recursion to find the i-th smallest element in an unsorted list, 
without sorting the entire list

Notes:
    - Like an easier version of Quicksort
    - Also called Quickselect

The main idea:
    1. Choose a random pivot and organize so that all elements less than pivot is before and all greater is after
        elements less than < pivot < elements greater than
    2. Calculate how many elements that are less than or equal to pivot
       pivot is the k-smallest element
    3. If i = k, then pivot is the i-th smallest element
    4. Otherwise, search recursively on the half that contains the i-th element (smaller or greater)


Time Complexity:
    - Randomized_Partition: O(n) -> iterates through entire list
    - Recursive call: O(n/2)
    - Total: O(n) + O(n/2) => O(n)

Space Complexity:
    - O(log n) recursion stack (average)
    - O(n) recurstion stack (worst case if pivot choice is unlucky)

Author: David
Date: 10-10-2025
"""

from quick_sort import Randomized_Partition

def randomized_select(list, startIndex, endIndex, i):
    # Base-case
    if startIndex == endIndex:
        return list[startIndex]
    
    # Split array in half
    midIndex = Randomized_Partition(list, startIndex, endIndex)     #O(n)

    # Check (what?)
    k = midIndex - startIndex + 1 #Elements on left side
    if i == k:
        return list[midIndex]
    
    # Recursive searching
    elif i < k: # Search Left
        return randomized_select(list, startIndex, midIndex - 1, i)     #O(n/2) Chooses only one of these
    else:       # Search Right
        return randomized_select(list, midIndex + 1, endIndex, i - k)   #O(n/2)
    

if __name__ == "__main__":
    arr = [7, 2, 1, 6, 8, 5, 3, 4]
    print("Original list:", arr)

    n = len(arr)
    i = 4  # for example: find the 4th smallest element

    result = randomized_select(arr, 0, n - 1, i)
    print(f"The {i}-th smallest element is:", result)


