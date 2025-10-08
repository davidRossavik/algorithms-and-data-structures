# Fundamentals - Guide

# Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.  
It’s simple but inefficient for large datasets.

- **Best case:** O(n) (already sorted)
- **Average/Worst case:** O(n²)
- **Stable:** Yes
- **In-place:** Yes

<br>

# Merge Sort

Merge Sort is a divide-and-conquer sorting algorithm.
It works by recursively splitting a list into two halves, sorting each half and then merging the sorted halves back together
Merge Sort is more efficient than Bubble Sort for larger datasets, but it requires extra memory for the merged sublists

- **Best case:** O(n*logn)
- **Average/Worst case:** O(n*logn)
- **Space complexity:** O(n) due to temporary lists used during merging
- **Stable:** Yes
- **In-place:** No, the algorithm creates new lists when merging
