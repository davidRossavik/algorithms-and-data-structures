def knapsack(items, capacity_g):
    """
    0/1 knapsack.
    items: list of (name, weight_g, value)
    capacity_g: max weight in grams
    Returns (total_value, selected_items)
    """
    n = len(items)
    # dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (capacity_g + 1) for _ in range(n + 1)]

    for i, (_, weight, value) in enumerate(items, start=1):
        for w in range(capacity_g + 1):
            dp[i][w] = dp[i - 1][w]
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)

    # Backtrack to find selected items
    selected = []
    w = capacity_g
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(items[i - 1])
            w -= items[i - 1][1]

    return dp[n][capacity_g], selected
