# The 0/1 Knapsack algorithm is a dynamic programming method used to find the maximum
# total value of items you can fit into a bag of a fixed weight capacity,
# where each item must either be taken completely (1) or left behind (0)

# Explanation

# We have n items, each with a value[i] and weight[i].

# The knapsack can carry a maximum weight W.

# The key idea is to decide for each item: include it or exclude it.

# We use dynamic programming to avoid recalculating the same sub problems.

# We define a 2D DP table dp[i][w] where:
# i represents the first i items
# w represents the current weight capacity

# dp[i][w] stores the maximum value achievable with i items and weight w.

# The recurrence relation:

# If weight of current item weight[i-1] <= w:
# dp[i][w] = max(dp[i-1][w], value[i-1] + dp[i-1][w - weight[i-1]])

# Else:
# dp[i][w] = dp[i-1][w]


def knapsack_01(weights: list[int], values: list[int], capacity: int):
    n = len(values)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Example usage

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print("Maximum value:", knapsack_01(weights, values, capacity)) 