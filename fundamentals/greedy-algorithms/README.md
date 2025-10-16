
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



