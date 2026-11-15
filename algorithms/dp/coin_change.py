# Coin change refers to problems where we must form a target amount using given coin denominations.

# Two common variants are:
# Count the number of combinations (order dosen't matter) to make the amount.

# Find the minimum number of coins required to make the amount (or report impossible).

# Explanation

# Both variants are classic dynamic programming problems (unbounded knapsack style)
# because each coin can be used repeatedly.

# For counting combinations, use a 1D DP array: [ways], where: ways[0] = 1
# and for each coin, iterate sums from coin to amount doing ways[s] += ways[s-coin].

# Iterating coins , use dp[s] initialized to infinity except dp[0] = 0,
# and update dp[s] = min(dp[s], dp[s-coin]+1),

# Again iterate coins outer,
# sums inner to maintain correct unbounded behavior


def coin_change_count(coins, amount):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for c in coins:
        for s in range(c, amount + 1):
            ways[s] += ways[s - c]
    return ways[amount], ways


def coin_change_min(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for c in coins:
        for s in range(c, amount + 1):
            dp[s] = min(dp[s], dp[s - c] + 1)
    return (-1 if dp[amount] == float("inf") else dp[amount]), dp


# Example Usage

coins = [1, 2, 5]
amount = 11

count_result, count_table = coin_change_count(coins, amount)

print(f"Coins: {coins}, Amount: {amount}")

print(f"1) Number of ways to make amount: {count_result}")
print("DP table for count (index = sum -> ways):")
for i in range(amount + 1):
    print(f"{i:2} -> {count_table[i]}")


min_result, min_table = coin_change_min(coins, amount)

print(f"\n2) Minimum coins required to make amount: {min_result}")
print("DP table for min coins (index = sum -> min coins or INF):")
for i in range(amount + 1):
    print(f"{i:2} -> {min_table[i]}")
