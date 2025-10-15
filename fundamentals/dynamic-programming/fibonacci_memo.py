"""
fibonacci_memo.py
------------------
An implementation of the fibonacci sequence optimization, solved with 
Dynamic Programming in Python.

Backgroundinfo:
    - Fibonacci follows the rule: F(n) = F(n-1) + F(n-2)
    - With base-cases: F(0) = 0, F(1) = 1
    - The goal is to find F(n)

Why Dynamic Programming?
    - The naiv, recursive method calls itself many times on the same values
        -> Exponential time complexity O(2^n)
    - DP removes duplication by storing earlier calculations

Two Methods:
    - Bottom-Up (Tabulation): Builds the sequence from the bottom. Iterates through and stores all values in a table.
    - Top-Down (Memoized): Starts from F(n) and stores the results along the way in a cache.


Author: David
Date: 15-10-2025
"""

# Bottom-Up (Iterative)
# Not a choice, just that it is built up by smaller

def fibonacci_bottom_up(n):
    fibonacci = [0] * (n+1)  
    
    #Base case
    fibonacci[0] = 0 #F(0)
    fibonacci[1] = 1 #F(1)

    # for-loop
    for i in range(2, n+1): # We want to reach n as well!
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    
    return fibonacci[n]


# Top-Down (Recursion)
# Start from the top, call itself all the way down
def fibonacci_top_down(n, memo):
    # Base-case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Check if it already is calculated in the memo
    if memo[n] != -1:
        return memo[n]
    
    # fibonacci
    memo[n] = fibonacci_top_down(n-1, memo) + fibonacci_top_down(n-2, memo)

    return memo[n]

if __name__ == "__main__":
    n = 8
    memo = [-1] * (n+1)

    print("Bottom-Up:", fibonacci_bottom_up(n))
    print("Top-Down:", fibonacci_top_down(n, memo))
