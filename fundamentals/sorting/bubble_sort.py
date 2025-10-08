""" 
bubble_sort.py 
-------------- 
A simple implementation of the Bubble Sort algorithm in Python. 
Bubble Sort is a basic comparison-based sorting algorithm. It repeatedly steps through 
the list, compares adjacent elements, and swaps them if they are in the wrong order. 
This process continues until the list is sorted. 

Although easy to understand and implement, Bubble Sort is inefficient for large datasets, 
with an average and worst-case time complexity of O(n²). 

This file is part of the "fundamentals" section of my Algorithms and Data Structures repository. 
It demonstrates basic algorithmic logic, nested loops, and step-by-step array manipulation. 

Author: David 
Date: 2025-10-08 
"""

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Before sorting:", numbers)
    bubble_sort(numbers)
    print("After sorting:", numbers)
