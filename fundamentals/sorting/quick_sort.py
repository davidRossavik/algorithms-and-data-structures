"""
quick_sort.py
--------------
Implementation of the Quicksort and/or Randomized Quicksort algorithm in Python.
The sorting algorithm is based on the divide-and-conquer-principle.

There are two implementations of the algorithm:
    - Quick Sort: Main idea 
    - Randomized Quick Sort: Same algorithm, but chooses pivot randomly

The main idea:
    1. Pick a pivot element from the list
    2. Divide: Partition the list into two parts (elements lesser and greather than pivot)
    3. Conquer: Recursively sort left and right parts
    4. Combine the sorted parts and pivot to get sorted list

Time Complexity
    - Partitioning: O(n)
    - Recursive left: T(n/2)
    - Recursive right: T(n/2)
    - T(n) = 2*T(n/2) + O(n) (solved with master theorem)
    - Total: O(n*logn)

Space Complexity:
    - Recursive calls: O(logn) - Demands extra call stack frames
    - Worst-case: O(n)

Author: David
Date: 09-10-2025
"""

import random 

def Quicksort(list, startIndex, endIndex):
    if startIndex < endIndex:
        pivot = Partition(list, startIndex, endIndex)   #O(n)
        Quicksort(list, startIndex, pivot - 1)          #T(n/2)
        Quicksort(list, pivot + 1, endIndex)            #T(n/2)

"""
Partitioning: Rearranges the list to (elements less < pivot < elements greater)

The main idea:
    1. Choose pivot (last element)
    2. Set boundary index (start with index 0)
    3. Iterate through list (except pivot) and place elements less than pivot
        on index 1, 2, 3, ... 
    4. Place pivot to the right from the lesser elements
    5. End up with elements less than pivot - pivot - elements greater than pivot
"""
def Partition(list, startIndex, endIndex):
    pivot = list[endIndex]
    i = startIndex - 1

    for j in range(startIndex, endIndex):   #O(n)
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    
    list[i + 1], list[endIndex] = list[endIndex], list[i + 1]

    return i + 1

"""
Randomized Quick Sort
    - Difference in worst-case probability
"""
def Randomized_Quicksort(list, startIndex, endIndex):
    if startIndex < endIndex:
        pivot = Randomized_Partition(list, startIndex, endIndex)
        Randomized_Quicksort(list, startIndex, pivot - 1)
        Randomized_Quicksort(list, pivot + 1, endIndex)


"""
Randomized Partition

Main idea:
    - pick a random index between start and end
    - move chosen pivot to the end and return Partition
"""
def Randomized_Partition(list, startIndex, endIndex):
    randomIndex = random.randint(startIndex, endIndex)
    list[randomIndex], list[endIndex] = list[endIndex], list[randomIndex]
    return Partition(list, startIndex, endIndex)



if __name__ == "__main__":
    test_list = [5, 2, 9, 25, 20, 17, 34]
    test_list2 = [5, 2, 9, 25, 20, 17, 34]
    print("Unsorted:", test_list)
    Quicksort(test_list, 0, len(test_list)-1)
    print("Sorted with Quick Sort:", test_list)
    Randomized_Quicksort(test_list2, 0, len(test_list2)-1)
    print("Sorted with Randomized Quick Sort:", test_list2)