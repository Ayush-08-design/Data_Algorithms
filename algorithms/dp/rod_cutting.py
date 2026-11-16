# The Rod Cutting Algorithm is a classic dynamic programming problem.
# that aims to determine the maximum profit obtainable by cutting a rod into smaller
# pieces and selling them based on given prices for each length.

# It's similar to the unbounded knapsack problem,
# where we can take multiple instances of the same piece length.

# Explanation

# We are given:
# A rod of length n.
# A price list price[i] which gives the price of a rod of length i + 1

# we can cut the rod into smaller parts or leave it uncut
# The goal is to maximize total value.


def rod_cutting(prices: list[int], length: int):
    dp = [0] * (length + 1)
    for i in range(1, length + 1):
        max_value = float("-inf")
        for j in range(i):
            max_value = max(max_value, prices[j] + dp[i - j - 1])
        dp[i] = max_value

    return dp[length]


# Example Usage

prices = [2, 5, 7, 8]
length = 4

print(f"Maximum obtainable profit: {rod_cutting(prices, length)}")
