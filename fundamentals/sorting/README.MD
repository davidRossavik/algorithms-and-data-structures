## Fundamentals - Guide

| Algoritme          | Best Case    | Average Case | Worst Case   | Stabil | In-place |
| ------------------ | ------------ | ------------ | ------------ | ------ | -------- |
| **Insertion Sort** | Θ(n)         | Θ(n²)        | Θ(n²)        |   ✅  |   ✅     |
| **Merge Sort**     | Θ(n log n)   | Θ(n log n)   | Θ(n log n)   |   ✅  |   ❌     |
| **Heap Sort**      | Θ(n log n)   | Θ(n log n)   | Θ(n)         |   ❌  |   ✅     |
| **Quick Sort**     | Θ(n log n)   | Θ(n log n)*  | Θ(n²)        |   ❌  |   ✅     |
| **Counting Sort**  | Θ(n + k)     | Θ(n + k)     | Θ(n + k)     |   ✅  |   ❌     |
| **Radix Sort**     | Θ(d·(n + k)) | Θ(d·(n + k)) | Θ(d·(n + k)) |   ✅  |   ❌     | 
| **Bucket Sort**    | Θ(n)         | Θ(n    )     | Θ(n²)        |   ✅  |   ❌     |




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

Counting sort is a non-comparison-based sorting algorithm.
Effective for sorting integers when the values are within a limited range 0 to k.

The algorithm works by counting how many times each value occurs and then using this count to place each element directly in its correct position. To maintain stabilit, it processes the input array from right to left when placing elements.

Limitations: <br>
    - if k >> n, the algorithm becomes memory-intensive and inefficient <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -Example: Sorting 1,000 numbers in range 1-10,000,000 would allocate a huge array C mostly filled with zeros <br>
    - Only works with integers or discrete values within known range <br>
Best for: <br>
    - Small ranges of integers, or when stable sorting is needed

- **Best case:** O(n + k) (Counting sort always counts and place elements, independent of input distribution)
- **Average case:** O(n + k)
- **Wost case:** O(n + k)
- **Space complexity:** O(n+k) (output array B + count array C)
- **Stable:** Yes
- **In-place:** No (requires additional arrays)

<br>

# Radix Sort

Radix sort is a non-comparison-based, stable sorting algortihm. <br>
It uses a stable subroutine like Counting Sort, ensuering that the relative order of numbers with the same digit is preserved.

The algorithm works by sorting numbers **digit by digit**, starting from the least significant digit to the most significant digit. It uses a stable sorting algorithm for sorting each digit.

Notes:
- Works efficiently when the number of digits is small compared to the number of elements
- Useful for sorting integers, strings of equal length or fixed-size keys
<br> ---

- **Best case:** O(n * k) (processes each of the n element for each of the k digits)
- **Average case:** O(n * k)
- **Wost case:** O(n * k)
- **Space complexity:** O(n + base)  (auxiliary arrays used in Counting sort for each digit (output array + count array)) (Same space is reused for each digit, so we dont multiply by k)
- **Stable:** Yes
- **In-place:** No (requires additional arrays)

<br>

# Bucket Sort

Bucket sort is a stable sorting algorithm. <br>
It uses a stable subroutine, Insertion Sort, for the sorting-part.

The algorithm assumes that the input is a list of numbers between 0 and 1. It then creates n buckets, and distributes the numbers in their corresponing bucket (by value). The individual buckets is sorted by Insertion Sort, and then concatenated back to the original list.

Notes:
- Pseudo-code uses n=length(A), but you could use n=sqrt(length(A)) or n = length(A) // k depending on how various you think the values are distributed
<br> ---

- **Best case:** O(n)  (if elements are uniformly distributed and buckets are small (Insertion sort fast))
- **Average case:** O(n)  (if numbers evenly distributed)
- **Wost case:** O(n^2)  (all numbers in same bucket)
- **Space complexity:** O(n)  (extra space for the buckets)
- **Stable:** No  (Can make stable tho) (Insertion Sort stable, concatenating not always in order)
- **In-place:** No  (requires additional arrays)

<br>

# Randomized Select

Randomized Select (also called Quickselect) is a searching algorithm <br>
It uses a subroutine, Randomized Partition, to speed up the search process.

It is used to fint the i-th smallest element in an unsorted list, without having to sort the entire list. It uses Randomized Partition to randomly choose a pivot and split the list in two halves divided by the value relative to pivot.

Notes:
- Based on Quicksort, but only uses recursion on one part of the list
- Useful when:
    - We need a spesific element (For example: mean value)
    - Dont want to sort the entire array
    - Can tolerate some variation in running time (random pivot = risc   for bad results)
    - Small extra memory (in place)
- Bad algorithm when:
    - Need many order statistics (then sorting is better)
    - Need a garuanteed worst-case running time
    - Need stability

<br> ---

- **Best case:** O(n)  
- **Average case:** O(n)
- **Wost case:** O(n^2) (Pivot divides poorly)
- **Space complexity:** O(log n) recursion depth in average
- **Stable:** No 
- **In-place:** Yes

<br>

## Select (Median of Medians)

Select is a searching algorithm. <br>
Its purpose is to find the k-th smallest element in an unsorted list, without sorting the entire list, using a pivot chosen in a deterministic way to guarantee good splits.

Similar to Randomized Select, but instead of choosing random pivot, it calculates the median of medians to ensure balances partitions

Notes:
- Guarantees worst-case linear running time O(n)
- Useful when:
    - can tolerate extra computation to find a good picot
    - predictable running time
- Bad algotihm when:
    - need many order statistics
    - we want simple, fast average-case solution
    - need stability
<br> ---

- **Best case:** O(n)
- **Average case:** O(n)
- **Wost case:** O(n)
- **Space complexity:** O(n)
- **Stable:** No 
- **In-place:** No

<br>

# Heap Sort

Heap Sort is an sorting algorithm, based on heaps.
It uses Max-Heapify and Build-Max-Heap to repair the Max-Heap after removing its root-node for sorting.

The algorithm works by arranging the input-array as a heap, then using heap-operations to rearrange the maximum value to the root. When the maximum value is at the root, it puts it at the back of the array and makes the heap one index smaller. 

- **Best case:** O(n) (if array is already max-heap. then Max_Heapify runs in O(1))
- **Average case:** O(n*log n) (sort each index n with an Max_heapify that takes O(logn) time)
- **Wost case:** O(n*logn)
- **Space complexity:** O(logn)
- **Stable:** No 
- **In-place:** Yes

