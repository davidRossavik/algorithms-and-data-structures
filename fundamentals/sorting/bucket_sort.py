"""
bucket_sort.py
--------------
Implementation of Bucket Sort in Python.
Needs a stable rubroutine for sorting (Insertion sort here).

Notes:
    - Uses insertion sort (because it is almost sorted in buckets)
    - Stable sorting algorithm
    - Pros: 
        Can achieve linear running time O(n) if numbers are evenly distributed and numbers of buckets is appropriate
        No predecided size: Each bucket is a dynamic list
        Memory efficient: Only buckets with elements allocates space
        Simple implementation
    - Cons: 
        Demands input from 0-1
        can get ineffective if numbers are unevenly distributed and all numbers end in one bucket (Insertion sort)

The main idea:
    1. Assumes all input numbers are evenly distributed between 0-1
    2. Splits interval in n buckets
    3. Distributes numbers in the appropriate bucket
    4. On each bucket: sort by insertion sort
    5. Concatenate each bucket


Time Complexity:
    - Create empty lists: O(n)
    - Distribute into buckets: O(n)
    - Sort each bucket: O(n)
            Best case: O(1) per bucket if nearly empty
            Average case: O(n^2), but O(n) if evenly distributed
            Worst case: O(n^2) all elements in one bucket
    - Concatenate buckets: O(n)
    - Total: O(n) * 4 = O(n) IF evenly distributed, O(n^2) if not

Space Complexity:
    - O(n) extra memory for the buckets

Author: David
Date: 10-10-2025
"""

from insertion_sort import insertion_sort

def bucket_sort(list):
    # Create n buckets
    n = len(list)
    B = [[] for _ in range(n)]      #O(n)

    # Distributies in correct bucket
    for number in list:
        B[int(number * n)].append(number)   #O(n)
    
    # Sort each bucket
    for i in range(n):      #O(n)
        B[i] = insertion_sort(B[i])     #O(n^2)
    
    # Concatenate
    result = []
    for bucket in B:    #O(n)
        result.extend(bucket)
    
    return result


if __name__ == "__main__":
    test_list = [0.5, 0.3, 0.25, 0.9, 0.1, 0.6, 0.6, 0.5, 0.8, 0.3, 0.2]
    print("Before sorting:", test_list)
    sorted_list = bucket_sort(test_list)
    print("After sorting:", sorted_list)



