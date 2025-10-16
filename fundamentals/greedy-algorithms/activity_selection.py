"""
activity_selection.py
----------------------
Implementation of an algorithm that uses a greedy strategi to find the optimal solution.

The problem:
    - You are in charge of booking for an auditorium
    - Given a lot of requests for activites you need to select
      the maximum number of non-overlapping activites

The main idea:
    - Greedy-choice: Choose the activity that ends first. 
    - Optimal substructure: You are left with a bunch of other activities where you
      also can choose the activity that ends first

Time Complexity:
    - O(n*logn)

Space Complexity:
    - Storing of start/end-time: O(n)

Author: David
Date: 16-10-2025
"""

def activity_selection(activites):
    # Sort the activites by finish time
    activites.sort(key=lambda x: x[1])  #O(n lgn)

    selected = []
    last_finish = 0

    for start, finish in activites:     #O(n)
        if start >= last_finish: # Checks that the starttime is after last_endtime
            selected.append((start, finish))
            last_finish = finish
    return selected


if __name__ == "__main__":
    activites = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 9), (8, 9)]
    chosen = activity_selection(activites)
    print("Selected activites:", chosen)
