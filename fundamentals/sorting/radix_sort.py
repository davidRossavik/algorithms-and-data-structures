"""
radix_sort.py
-------------
Implementation of Radix Sort algorithm in Python.
Radix Sort is an algorithm that works in linear time.

The main idea:
    1. Sort each digit in the numbers with a stable subroutine
       (Uses Counting Sort)

Time Complexity:
    - O(d * (n + k))
        d = number of digits
        n = number of elements
        k = range of each digit (base, e.g 10)
    - Because for each digit, Counting Sort rundt in O(n + k)
    - When d is constant (like base 10-integers): it behaves as O(n)

Space Complexity:
    -O(n + k)
        (Counting array C and array B in counting_sort_by_digit)
    - Auxiliary space is resued for each digit
    (Auxiliary - extra memory used during sorting)

Author: David
Date: 10-10-2025
"""

def radix_sort(list, numberOfDigits):
    base = 10

    for i in range(numberOfDigits):     #O(d) * O(n + k)
        list = counting_sort_by_digit(list, base, base ** i)
    
    return list


"""
Counting Sort modified to sort by digit in digit_place

"""
def counting_sort_by_digit(list, base, digit_place):
    # Initialize
    length = len(list)
    C = [0] * base
    B = [0] * length

    # Count occurences
    for number in list:     #O(n)
        digit = number // digit_place % base
        C[digit] += 1
    
    # Cumulative sum
    for i in range(1, base):    #O(base)
        C[i] += C[i-1]
    
    # Place element into B
    for i in range(length - 1, -1, -1):     #O(n)
        digit = list[i] // digit_place % base
        sortedIndex = C[digit] - 1 # C is cumulative. Number on digit-spot is the number of numbers before that digit. Since number of numbers is 1-based we must - 1.
        B[sortedIndex] = list[i]
        C[digit] -= 1
    
    return B

if __name__ == "__main__":
    test_list = [34, 68, 912, 38, 16, 5, 11, 25]
    print("Before sorting:", test_list)
    sorted_list = radix_sort(test_list, 3)
    print("After sorting:", sorted_list)



