"""
rod_cut.py
-----------
Implementation of the DP optimization algorithm Rod Cutting in Python.

The goal is to determine the maximum revenue obtainable by cutting a rod
of length n into smaller pieces and selling them according to a given price list.

The main idea:
    - At each length, we have two choices:
        > Cut the rot at position i and solve the subproblem for the remaining length n-i
        > Do not cut further (keep as is)
    1. 

Time Complexity:
    -    

Space Complexity:
    -

    
Author: David
Date: 13-10-2025
"""

# Bottom-Up (Iterative)
def rod_cut_bottomUp(prices, length):
    dp = [0] * (length+1) # dp[j] maximal income for a rod with length j
    cuts = [0] * (length+1) # To reconstruct where we cut cut[j] first optimal cut for roclength j

    for j in range(1, length+1): # For each length from 1 to length of rod
        q = float("-inf") # Best price found so far for length j

        # Evaluate every possible cut from 1 to j
        for i in range(1, j+1):
            # Choice 1: "Bring" cut of length i
            current_value = prices[i-1] + dp[j - i] # Bring and add to the optimal length of the length minus this one

            # Choice 2: Skipp, we keep on searching for better

            if q < current_value:
                q = current_value
                cuts[j] = i # Store first cut
        
        # Set optimal value for rodlength j
        dp[j] = q
    
    return dp[length], cuts

def reconstruct_cuts(cuts, length):
    result = []
    while length > 0:
        result.append(cuts[length])
        length -= cuts[length]
    return result

# Top-Down with Memoization (Recursion)
def rod_cut_topdown(prices, n, memo, first_cuts):
    # Base case
    if n == 0:
        return 0
    
    # Return from cache if we already have calculated it
    if memo[n] >= 0:
        return memo[n]
    
    q = float("-inf")
    for i in range(1, n+1):

        # Current_value is the price of the item we have now + the optimal prize for the remaining length n-i
        current_val = prices[i-1] + rod_cut_topdown(prices, n-i, memo, first_cuts)

        # Update optimal value
        if current_val > q:
            q = current_val
            first_cuts[n] = i #Stores first optimal cut for length n

    memo[n] = q
    return q

def reconstruct_topdown(first_cuts, n):
    cuts = []
    while n > 0:
        cuts.append(first_cuts[n])
        n -= first_cuts[n]
    return cuts


if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    n = 8
    first_cuts = [0] * (n+1)
    memo = [-1] * (n+1)

    value, cuts = rod_cut_bottomUp(prices, n)
    value2 = rod_cut_topdown(prices, n, memo, first_cuts)
    cuts2 = reconstruct_topdown(first_cuts, n)

    print("Bottom-Up Result:", value)
    print("Cuts:", reconstruct_cuts(cuts, n))
    print("Top-Down results:", value2)
    print("Cuts2:", cuts2)
        
                

    
    