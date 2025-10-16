
# Greedy algorithms

## Overview
Greedy algorithms are optimizing algorithms that tries to find the global optimum, by choosing the locally optimal choice at each step.
They work when the problem satisfies:
- **Greedy Choice Property**: A global optimum is can by reached by choosing the local optima
- **Optimal substructure**:  An optimal solution can be built from optimal subsolutions

Typical examples include:
- Activity Selection
- Fractional (Continuous) Knapsack
- Huffman Coding
<br>

## The Greedy Choice Property
This property ensures that choosing the local option (greedy choice) at each steps leads to the overall global optimum
<br>

### Example intuition:
- **Activity selection**: always choose the activity that finishes earliest.
- **Knapsack**: always take the most valuable item per weight unit.
- **Huffman coding**: always merge the two least frequent symbols.
- **Rod cutting**: always choose the most valuable length
<br>

## Proof 
<br>

### Activity Selection
- Greedy choice: always choose the activity that ends the earliest among those who dont overlap

Proof-method: Exchange argument

Greedy-choice property:
- Assume there is an optimal solution that dont start with the activity that ends first
- Let a_k be the activity with the lowest end-time
- Switch the first activity in O with a_k
  - This is legal because a_k ends earlier, and gives space to at least as many activites afterwards
- Therefore we can construct an optimal solution that starts with the greedy-choice
- Greedy-choice property PROVEN

Optimal substructure:
- After choosing a_k, we can ignore all activites that starts before the endtime of a_k
- The rest of the problem has an identical structure: choose the maximum amount activites from the ones remaining
- Optimal substructure PROVEN
<br>

### Fractional (Continuos) Knapsack

- Greedy choice: Always bring items after biggest value/weight ratio, until te knapsack is full (last item is taken partially if nescesarry)

Proof method: Exchange argument

Greedy-choice property:
- x_i is the amount of each item i we take
- Assume that an optimal solution O dont take the best ratio first
- Switch out a part of the item with lower ratio with a part of that of higher ratio
- This increases the total value, without going over the weight capacity
- Therefore the optimal solution is always going to obtain as much as possible from the item with higest value/weight ratio

Optimal substructure:
- After the first item is chosen (or parrts of it), we are left with a problem og same type
  - Maximum value for a new capacity, and the suproblem has the same structure

Note: For 0/1 Knapsack, greed fails. Because it isnt necessarily the "local" best combination that leads to the global optimum.

<br>

### Huffman Coding

- Greedy choice: Always merge the two symbols with the lowest frequency to a new node

Proof method: Induction + Exchange argument

Greedy-choice property:
- Assyme that there is an optimal treestructure T that dont combine the two lowest frequencies first
- Let a,b be the two with lowest frequency
- We can switch place on the undertrees in T, so that a and b are siblings, without increasing total cost
- There there is always an optimal tree where the two lowest frequencies are combined first

Optimal substructure:
- When merging a and b to a new node with frequency of them combined, we end up with a new problem with one less node  same structure
- Therefore Huffman-solution builds optimal from bottom to top.


