"""
coin_change.py
--------------
Implementation of the Coin Change (Minimum) DP optimization problem in python

Backgroundinfo:
    - You have a n unlimited amount of each coin (1, 5, 10, 20) and an target amount 12
    - Find the least amount of coins you need to form the target-amount

Why Dynamic Programming:
    - Overlapping subproblems: To find the solution for amount=11 , you need the solution for amount=10, 9 8, ... etc.
    - Optimal substructure: The best solution for amount = n is built upon the best solution for smaller amounts
    - At each amount we have two choices for the coin:
        > Considerate the coin in the coin-sum
        > Dont considerate the coin in the coin-sum

Two Methods:
    - Top-Down (Memoization): 
        > Check for each coin:
            - If bringing the coin along, is number of coins smaller than not bringing it along? 
            - Continously update each index for amount in memo for the smallest current number of coins
            - Helper-function for reconstructing the different choices of coins
    - Bottom-Up (Tabulation): 
        > Builds a table where min amount of coins to store the amount x
        > For one coin: 
            - If the coin fits, we can check what the optimal sum is for adding this coin to the previous coins
            - If it doesnt fit (transfer min-value from last optimal coin)

Author: David
Date: 15-10-2025
"""

# Bottom-Up (Iteration)
def coin_change_bottom_up(coins, amount):
    # What is the best number of coins for amount given that I already know solutions for amount - coin

    dp = [float("inf")] * (amount + 1) # 1Dimentional list
    dp[0] = 0 # Base case
    choices = [-1] * (amount + 1) #Store last best choice for the coin

    for current_amount in range(1, amount + 1):
        for coin in coins:

            if coin <= current_amount:

                # Choice one, bring the coin
                bring_coin = 1 + dp[current_amount - coin]

                # Choice two, dont bring coin
                dont_bring = dp[current_amount]

                if bring_coin < dont_bring:
                    choices[current_amount] = coin  # Store choices
                    dp[current_amount] = bring_coin
    
    
    return dp[amount], reconstruct_choices(amount, choices, dp)

def reconstruct_choices(amount, choices, dp):

    # No solution
    if dp[amount] == float("inf"):
        return []
    
    # Go backwards in solution
    used_coins = []
    current = amount
    while current > 0:
        coin = choices[current]
        used_coins.append(coin)
        current -= coin

    return used_coins

# Top-Down (Recursion) with Memoization:
def coin_change_top_down(amount, coins, memo, choices):
    # What is the leas amount of coins I need to make amount?
    # For each coin-choice, we call coin_change_top(amount - coin) and take the best of them

    #Base case
    if amount <= 0:
        return 0

    if memo[amount] != float("inf"):
        return memo[amount]
    
    for coin in coins:
        # If coin fits in amount
        if coin <= amount:
            bring_coin = 1 + coin_change_top_down(amount - coin, coins, memo, choices) #Bring the coin
            
            if bring_coin < memo[amount]:   #Check if bringing the coins lead to fewer coins being used
                memo[amount] = bring_coin
                choices[amount] = coin      # Track coin-choices that we bring along
    
    return memo[amount]

def reconstruct(amount, choices, memo):

    if memo[amount] == float("inf"): #No solution
        return []

    updated_coins = []
    current = amount
    while current > 0:
        coin = choices[current]
        updated_coins.append(coin)
        current -= coin
    return updated_coins

if __name__ == "__main__":
    coins = [1, 5, 10, 20]
    amount = 12
    memo = [float("inf")] * (amount + 1)
    choices = [-1] * (amount + 1)

    number_of_coins, coins_chosen = coin_change_bottom_up(coins, amount)

    print("Minimum number of coins (Bottom-Up):", number_of_coins)
    print("The coins used:", coins_chosen)
    print("--------------------------------" * 2)

    number_of_coins2 = coin_change_top_down(amount, coins, memo, choices)
    coins_used = reconstruct(amount, choices, memo)
    

    print("Minimum number of coins (Top-Down):", number_of_coins2)
    print("The coins used:", coins_used)

