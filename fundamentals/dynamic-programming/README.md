
# Dynamic Programming

### Overview
Dynamic Programming (DP) is a method for solving problems than can be divided into **overlapping sub-instances**
Instead of solving the same subproblem multiple times (like pure recursion), DP **stores previous results** and reuses them.

DP is used when:
- The problem kan be divided into **subproblems**
- The subproblems **overlaps** (same subproblem occurs multiple times)
- There is an **optimal substructure**, the optimal solution is built from optimal solutions from the subinstances

### Two main types
| Type | Description | Characteristics |
|**Bottom-Up (table-based)** | Builds the solution from the smallest subproblems upwards | Uses `for`-loops and tables |
| **Top-Down (Memoization)** | Starts from the main problem and stores the results along the way | Uses recursion + cache (dictionary/list). |

## 💻 Kodeforslag du kan inkludere i mappen

| Filnavn | Beskrivelse |
|----------|--------------|
| `fibonacci_memo.py` | Top-Down DP med memoization |
| `rod_cutting.py` | Klassisk bottom-up-stavkutting |
| `knapsack.py` | 0/1 Knapsack bottom-up DP |
| `lcs.py` | Longest Common Subsequence med 2D-tabell |
| `coin_change.py` | Minste antall mynter for et beløp |
| `matrix_chain.py` | Optimal rekkefølge for matrise-multiplikasjon |

## (LCS) Longest Common Subsequence

LCS is a an algorithm that uses dynamic programming to lower the running time from exponential to polynomial time.

The algorithm builds a 2D table where each cell (i, i) represent the length of the LCs between prefixes X[0...i-1] and Y[0...j-1]. It uses overlapping subproblems and optimal substructure - the key ideas behind dynamic programming.

At each cell:
- If characters match: extend the sequence from the diagonal
- If not -> choose the longer sequence from above or left

There are two main approaches:
- Top-Down (Recursive + Memoization) - calls itself on smaller prefixes and caches results
- Bottom-Up (iterative) - fills the DP table row by row (I have implementet Bottom-Up in lcs.py)
<br>

- **Average/Worst case**: O(m·n)
- **Space Complexity**: O(m*n)
- **Stable**: Not applicable (n/a)
- **In-place**: No (requires DP tables)

<br>



