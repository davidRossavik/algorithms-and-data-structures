"""
bisect.py
----------
Bisect is a binary search algorithm. It uses a sorted array A to
search for a value v. It returns the index of the value if found, and NIL
(null) otherwise. The algorithm is based on the divide-and-conquer-principle.

There are two versions of the algorithm. Both Bisect and Bisect'.
Bisect: Solves recursive
Bisect': Solves iterative 

The main idea:
    1. Repeatedly divide a search interval in half
    2. Bisect: uses recursion to call itself on smaller arrays
       Bisect': uses while-loop to update variables startIndex and EndIndex, in-place
    3. Find the index of the target value

Time Complexity:
    - Recursive: T(n) = T(n/2) + O(1) => O(logn)
    - Iterative: O(log n)

Space Complexity:
    - Recursive: O(log n) (due to call stack)
    - Iteratice: O(1) (in-place)

Author: David
Date: 09-10-2025
"""

from math import floor

# BISECT (RECURSIVE)
def Bisect(list, startIndex, endIndex, value):

    # Base case check
    if startIndex <= endIndex:
        midIndex = floor((startIndex + endIndex) / 2)
        if value == list[midIndex]:
            return midIndex
        
        # Search each half further
        elif value < list[midIndex]: #Left
            return Bisect(list, startIndex, midIndex - 1, value) #T(n/2)
        else: #Right
            return Bisect(list, midIndex + 1, endIndex, value)   #T(n/2)
    else:
        return None


# BISECT' (ITERATIVE)
def bisect(list, startIndex, endIndex, value):
    valueFound = False
    midIndex = None

    # Loop runs ~log_2(n) times (each iteration halves search interval)
    while startIndex <= endIndex and not valueFound:
        midIndex = floor((startIndex + endIndex) / 2)
        if value == list[midIndex]:
            valueFound = True
        elif value < list[midIndex]:
            endIndex = midIndex - 1
        else:
            startIndex = midIndex + 1
    return midIndex

if __name__ == "__main__":
    sorted_list = [5, 9, 25, 27, 34, 38, 49, 62, 75, 76]
    index1 = Bisect(sorted_list, 0, len(sorted_list)-1, 76)
    index2 = bisect(sorted_list, 0, len(sorted_list)-1, 76)
    print("Index found with Bisect is at:", index1)
    print("Index found with Bisect' is at:", index2)




