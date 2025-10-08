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