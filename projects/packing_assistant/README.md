# Packing Assistant

You're heading to the airport with a 10 kg cabin baggage limit.
Given a list of items — each with a weight and a usefulness score — which ones should you bring?

This is a classic 0/1 knapsack problem: each item can be taken or left behind (not split).

## Algorithm

Standard bottom-up dynamic programming knapsack.

- `dp[i][w]` = max value achievable using the first `i` items with capacity `w`
- After filling the table, backtrack to find which items were selected
- Time complexity: O(n × W), where W is the weight capacity in grams

## How to run

```bash
cd src
python main.py
```

## Example output

```
==================================================
  Airport Packing Assistant
  Cabin baggage limit: 10.0 kg
==================================================

Optimal selection (9.90 kg / 10.0 kg):
  Item                   Weight   Value
  ------------------------------------------
  Laptop                   1.80kg      95
  Phone charger            0.20kg      80
  ...

  Total value score: 605
```
