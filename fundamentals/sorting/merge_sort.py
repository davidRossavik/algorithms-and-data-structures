"""
merge_sort.py
-------------- 
Implementation of Merge Sort algorithm in Python.
The algorithm is based on the divide and conquer-principle. 

The main idea:
    1. Divide the list in two halfs, rougly the same size
    2. Conquer: Sort each part with recursion
    3. Merge the two parts to one sorted list

Time Complexity:
- Divide: O(1) for mid, O(n) for slicing
- Conquer: 2 * T(n/2)
- Merge: O(n)
- Total: T(n) = 2*T(n/2) + O(n) => O(n*logn)    

Author: David
Date: 08-10-2025
"""

def merge_sort(list):
    # Basecase: a list of 0 or 1 is already sorted
    if len(list) <= 1:
        return list
    
    # Divide: Split list into two halfs
    mid = len(list) // 2
    left = list[:mid]       #O(n) slicing
    right = list[mid:]      #O(n) slicing

    # Conquer: sort each half recursively
    left_sorted = merge_sort(left)      #T(n/2) 
    right_sorted = merge_sort(right)    #T(n/2)

    # Merge sorted halves
    return merge(left_sorted, right_sorted)     #O(n)

def merge(left, right):
    result = []
    i = j = 0
    
    # Merge until one list runs out
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append remaining elements to result
    result.extend(left[i:])
    result.extend(right[j:])

    return result

if __name__ == "__main__":
    test_list = [38, 27, 43, 3, 9, 82]
    print("Original list:", test_list)
    sorted_list = merge_sort(test_list)
    print("Sorted list:", sorted_list)

