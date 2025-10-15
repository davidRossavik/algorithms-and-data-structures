"""
knapsack.py
------------
Implementation of DP algorithm 0/1 Knapsack in Python.
This file implements both the recursive and iterative method of solving it.

Note:
    - This is 0/1 (binary) version: We have only one of each item, you can either choose it or not.
    - Unbounded Knapsack: The other version states that you can bring any number of the same item
    - How to reduce running time: Memoization
    - How to know what to bring in the backpack: store decisions

The problem states that we have a set with items that has a weight and a value.
We want a set with indexes that maximises the total value, but doesnt exceed the weight-capasity

The main idea (Recursive Top-Down):
    1. Has a base-case to stop recursion: number of items = 0
    2. Further we have two possibilites: 
        a) Skip the item and find the optimal solution for all the others
        b) Put the item in the backpack (if we have the capacity)
    3. Tries to call upon itself with both cases, and chooses the best solution
    4. Add Memoization:
        - A table with all the solution of what we already have calculated
        - Look it up before we calculate
        - To not make it eksponential running time


Time Complexity:
    - O(n*W) OR REALLY O(n*2^m)

Space Complexity:
    - O(n*W)

Author: David
Date: 13-10-2025
"""

def knapsack_topdown(values, n, weights, W, dp, choices):
    # Base case: if we ran out of items or weight_capacity
    if n == 0 or W == 0:
        return 0
    
    # Memoization: If we already have calculated this sub-problem
    # DP has items as columns and weight-capacity as rows
    # All items in dp-table is initialized as -1
    if dp[n][W] != -1:
        return dp[n][W]
    
    # Skip if items weight is bigger than capacity left
    if weights[n-1] > W:
        dp[n][W] = knapsack_topdown(values, n-1, weights, W, dp, choices)
        choices[n][W] = 0

    # Choose between not bringing and bringing the item
    else:
        skip = knapsack_topdown(values, n-1, weights, W, dp, choices)
        take = knapsack_topdown(values, n-1, weights, W - weights[n-1], dp, choices) + values[n-1]
        
        # Log the choices and set the best alternative
        if take > skip:
            dp[n][W] = take
            choices[n][W] = 1
        else:
            dp[n][W] = skip
            choices[n][W] = 0
    
    return dp[n][W]

"""
Knapsack Unbounded: You can choose any item you want any number of times
"""

def knapsack_topdown_unbounded(values, n, weights, W, dp, choices):
    # Base case
    if W == 0 or n == 0:
        return 0
    
    # Memoization
    if dp[n][W] != -1:
        return dp[n][W]
    
    # Choose it if the capacity can hold it
    if weights[n-1] > W:
        dp[n][W] = knapsack_topdown_unbounded(values, n-1, weights, W, dp, choices)
        choices[n][W] = 0
    else:
        skip = knapsack_topdown_unbounded(values, n-1, weights, W, dp, choices)
        take = knapsack_topdown_unbounded(values, n, weights, W - weights[n-1], dp, choices) + values[n-1]

        if take > skip:
            dp[n][W] = take
            choices[n][W] = 1
        else:
            dp[n][W] = skip
            choices[n][W] = 0
    
    return dp[n][W]

"""
Recounstruct choices: Helper-function for showing the items that was chosen
"""
def reconstruct_choices_01(values, weights, W, n, choices):
    # Traverses backwards in the choices-table and finds which elements that was chosen
    selected_items = []
    i = n
    capacity = W

    while i > 0 and capacity > 0:
        if choices[i][capacity] == 1:
            selected_items.append(values[i-1]) # Append the index of the items
            capacity -= weights[i-1] # Reduce the capacity
        i-= 1 # Go to the previous element
    
    return selected_items[::-1] #turn around so that the order is natural

def reconstruct_choices_unbound(values, weights, W, n, choices):
    # Traverses backwards in the choices-table and finds which elements that was chosen
    selected_items = []
    i = n
    capacity = W

    while i > 0 and capacity > 0:
        if choices[i][capacity] == 1:
            selected_items.append(values[i-1]) # Append the index of the items
            capacity -= weights[i-1] # Reduce the capacity
            i = n # DIFFERENT: STAY IN THE SAME ELEMENT STILL
        else:
            i -= 1
    
    return selected_items[::-1] #turn around so that the order is natural

""" 
Knapsack 0/1 - Bottom-Up (Iterative)

The main idea:
    1. Make a 2D array and insert 0 as an optimum if we have no items or weight
    2. Iterates through every item and weight. There we have two choices for each:
        a) Dont use the item: then look up the value of the best weight for the previous item
        b) Use the item: look up the value of this item + last item that we can fit with the left capacity
    3. Return the maximum of these two options
"""

def knapsack_iterative(n, W, weights, values):
    #Initialize table
    table = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):

            # If the items weight is too much, then skip the item
            if w < weights[i-1]:
                table[i][w] = table[i-1][w]
            
            # If it has the capacity: check if it better to keep this item and last best combination of items within weight capacity
            else:
                table[i][w] = max(
                    table[i-1][w - weights[i-1]] + values[i-1],
                    table[i-1][w]
                )
            
    return table[n][W]

if __name__ == "__main__":
    values = [60, 100, 120, 1000]
    weights = [10, 20, 30, 10]
    W = 50
    n = len(values)

    # Create a DP-table for memoization
    dp1 = [[-1 for _ in range(W+1)] for _ in range(n+1)]
    dp2 = [[-1 for _ in range(W+1)] for _ in range(n+1)]
    choices1 = [[0 for _ in range(W+1)] for _ in range(n+1)]
    choices2 = [[0 for _ in range(W+1)] for _ in range(n+1)]


    result1 = knapsack_topdown(values, n, weights, W, dp1, choices1)
    select1 = reconstruct_choices_01(values, weights, W, n, choices1)

    result2 = knapsack_topdown_unbounded(values, n, weights, W, dp2, choices2)
    select2 = reconstruct_choices_unbound(values, weights, W, n, choices2)

    result_iterative = knapsack_iterative(n, W, weights, values)

    print("Maximum value (0/1):", result1, " | choices:", select1)
    print("Maximum value unbounded:", result2, " | choices:", select2)
    print("Maximum value with iterative (0/1):", result_iterative)