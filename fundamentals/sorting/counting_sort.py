"""
counting_sort.py
----------------
Implementation of Counting Sort algorithm in Python.
Counting Sort is a non-comparison-based sorting algortihm that works in linear time.
Note: Only works for integers in limited range (For example: 0 to k)

Counts how many times each value occur, and uses that to place the numbers
directly in the right place.

The main idea:
    1. Find the biggest value in the list
    2. Initialize a list C with k+1 zeros
    3. Count how many times each number occurs
    4. Make a cumulative-sum (prefix-sum) in list C
       Each position reflects how many numbers that are <= that value
    5. Make an empty list B of same size as list A 
    6. Place the elements in the right position (right to left)
       Go backwards through A to maintain stability

Time Complexity:
    - Count occurrences: O(n)
    - Compute cumulative sum: O(k)
    - Place elements in B: O(n)
    - Total: O(n + k)

Space Complexity:
    - O(n) for B
    - O(k+1) for C
    - Total: O(n + k)

Author: David
Date: 09-10-2025
"""

def Counting_sort(list):
    #Initialize
    length = len(list)
    max_value = max(list)

    C = [0] * (max_value + 1) # max_value + 1 because C needs to store the value C[max_value] #O(k+1) space
    B = [0] * length # O(n) space

    # Count occurrences
    for number in list: # O(n)
        C[number] += 1

    # Cumulative sum
    for i in range(1, max_value + 1): #O(k)
        C[i] += C[i - 1]
    
    # Place element into B
    for i in range(length - 1, -1, -1): #O(n)
        value = list[i]
        sortedIndex = C[value] - 1 # C are "not" indexed to 0 while B and A are (as usual) (wee need to count elements in its own index)
        B[sortedIndex] = value
        C[value] -= 1 # Decrease count so next equal value goes to the left
    
    return B

if __name__ == "__main__":
    test_list = [3,5,6,3,2,3,4,6,1]
    print("Before sorting:", test_list)
    sorted_list = Counting_sort(test_list)
    print("After sorting:", sorted_list)

    

