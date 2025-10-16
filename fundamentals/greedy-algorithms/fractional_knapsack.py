"""
fractional_knapsack.py
-----------------------
Implementation of the Fractional (Continuous) Knapsack problem using a Greedy Algorithm.

Problem:
    - You have a set of items, each with a value and a weight
    - The knapsack can hold at most W weight
    - You can take *fractions* of an item (unlike the 0/1 knapsack)

Goal:
    - Maximize the total value without exceeding the weight capacity

Greedy Strategy:
    1. Compute value/weight ratio for each item (maximixe bang for bucks)
    2. Sort items by this ratio in descending order
    3. Take as much as possible of the item with highest ratio
    4. Continue until the knapsack is full

Why Greedy Works:
    - Greedy-choice property: taking the highest ratio first never reduces optimality
    - Optimal substructure: after taking the best item, remaining problem has the same strucutre

Time Complexity:
    - O(n log n) (sorting dominates)

Space Complexity:
    - O(1) (in-place, after sorting)

Author: David
Date: 16-10-2025
"""

def fractional_knapsack(values, weights, capacity):
    n = len(values)
    items = [(values[i], weights[i], values[i] / weights[i]) for i in range(n)]
    items.sort(key=lambda x: x[2], reverse=True) # Sort by value/weight ratio

    total_value = 0
    for value, weight, ratio in items:
        if capacity <= 0:
            break
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity #Append the rest of the item since it weighs too much for the knapsack
            capacity = 0

    return total_value

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    print("Maximum value in Fractional Knapsack:", fractional_knapsack(values, weights, capacity))