## Fundamentals - Guide

# Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.  
It’s simple but inefficient for large datasets.

- **Best case:** O(n) (already sorted)
- **Average/Worst case:** O(n²)
- **Stable:** Yes
- **In-place:** Yes

<br>

# Insertion Sort

Insertion Sort is a simple and intuitive sorting algorithm.
It performs well on small or nearly sorted datasets.

Builds a sorted list one element at a time by inserting each element into its correct position among the previously sorted elements. It compares backward until it finds the right spot.

- **Best case:** O(n) (already sorted)
- **Average/Worst case:** O(n^2) (worst: reversed array)
- **Space complexity:** O(1) extra memory
- **Stable:** Yes
- **In-place:** Yes

<br>

# Merge Sort

Merge Sort is a divide-and-conquer sorting algorithm. It is more efficient than Bubble Sort for larger datasets, but it requires extra memory for the merged sublists.

It works by recursively splitting a list into two halves, sorting each half and then merging the sorted halves back together.

- **Best case:** O(n*logn)
- **Average/Worst case:** O(n*logn)
- **Space complexity:** O(n) due to temporary lists used during merging
- **Stable:** Yes
- **In-place:** No, creates new lists when merging

<br>

# Bisect (Binary Search)

Bisect is a divide-and-conquer searching algorithm. 
It is more effective than just iterating through a list. The iterative version requires no memory.

It finds the position of a value in a sorted list by repeatedly dividing the search interval in half. At each step it compares the target value with the element at midIndex. The process repeats til the value is found or the search interval becomes empty.

There are two main implementations: <br>
    - Bisect: recursive (calls itself on smaller halves) <br>
    - Bisect': iterative (uses while-loop and updates indexes in-place)

- **Best case:** O(1) value found on first check
- **Average/Worst case:** O(logn)
- **Space complexity:** (Recursive) O(logn) extra call stack frames 
                        (Iterative) O(1)
- **Stable:** not applicable
- **In-place:** (Iterative) Yes

<br>

# Quicksort

Quicksort is a divide-and-conquer sorting algorithm.
The algorithm is often faster in practice than Merge Sort or Insertion Sort, because it works **in-place**, has **low overhead** from extra operations.

The algorithm selects a **pivot** element from the list and partitions the other into two sublist: those less than and those greater than pivot.
It then recursively sorts the sublist and combines them with the pivot in the middle.

**Randomized Quicksort** is a practical implementation of quicksort, which chooses a pivot randomly. Reducing the likelihood of encountering the worst-case scenario

- **Best case:** O(n*logn) (balanced partitions)
- **Average case:** O(n*logn)
- **Wost case:** O(n^2) (when pivot consistently divides poorly)
- **Space complexity:** O(logn) due to recursive calls
- **Stable:** No
- **In-place:** Yes

<br>

# Counting Sort

Counting sort is a non-comparison-based sorting algorithm
Effective for sorting integers when the values are within a limited range 0 to k.

The algorithm works by counting how many times each value occurs and then using this count to place each element directly in its correct position. To maintain stabilit, it processes the input array from right to left when placing elements.

Limitations:
    - if k >> n, the algorithm becomes memory-intensive and inefficient
        - Example: Sorting 1,000 numbers in range 1-10,000,000 would allocate a huge array C mostly filled with zeros
    - Only works with integers or discrete values within known range
Best for:
    - Small ranges of integers, or when stable sorting is needed

- **Best case:** O(n + k) (Counting sort always counts and place elements, independent of input distribution)
- **Average case:** O(n + k)
- **Wost case:** O(n + k)
- **Space complexity:** O(n+k) (output array B + count array C)
- **Stable:** Yes
- **In-place:** No (requires additional arrays)

<br>