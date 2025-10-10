"""
select.py
----------
Implementation of Select searching algorithm in Python.
The deterministic version of Ranomized Select.
It has a garuanteed running time of O(n) in worst case and is more predictable.
But it is more complicated and slower (more overhead), and it therefore
rarely used in "normal" code

Notes:
    - Methos is called Median of Medians
    - Guaruantees that the median is somewhat balanced

The main idea:
    1. Split the list in groups of 5 elements
    2. Find the median in each group (by sorting)
    3. Find the median of all these medians - this is the pivot
    4. Partition the list around this pivot and keep on going

Time complexity:
    - Total: O(n)

Space complexity:
    - O(n) (recursive calls and temporary lists)

Author: David
Date: 10-10-2025
"""

from insertion_sort import insertion_sort

def select(A, k):
    # Base case: small lists is sorted directly
    if len(A) <= 5:
        return insertion_sort(A)[k-1]
    
    # Split the list in group of 5 elements
    groups = [A[i:i+5] for i in range(0, len(A), 5)]

    # Find the median in each group
    medians = [insertion_sort(group)[len(group)//2] for group in groups]

    # Find the pivot as the median of medians
    pivot = select(medians, len(medians)//2 + 1)

    # Partition around the pivot
    lower = [x for x in A if x < pivot]
    equal = [x for x in A if x == pivot]
    higher = [x for x in A if x > pivot]

    # Choose recursively the correct part
    if k <= len(lower):
        return select(lower, k)
    elif k <= len(lower) + len(equal):
        return pivot
    else:
        return select(higher, k - len(lower) - len(equal))
    

if __name__ == "__main__":
    A = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    for i in range(1, len(A) + 1):
        print(f"{i}-th smallest element:", select(A, i))



