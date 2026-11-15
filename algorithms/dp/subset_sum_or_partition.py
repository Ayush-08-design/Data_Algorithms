# The subset sum problem is a classic Dynamic Programming problem

# The Partition Equal Subset Sum problem asks whether an array of integers can be split
# into two subsets whose elements add up to the exact same value.

# And subset sum asks whether there exists a subset of a given set of integers that 
# adds up to a specific target sum.

# Explanation

# We are given an array arr[] of size n and a sum target.

# Our goal is to determine if any subset of the array, sums to target
# It can be solved using DP where:

# We will use a 2D boolean table dp[n+1][target+1].
# dp[i][j] = True, means we can form sum j using the first i elements.

# Translation logic:

# If current element arr[i - 1] > j: we can't include it -> dp[i][j] = dp[i-1][j]

# Otherwise -> dp[i][j] = dp[i-1][j] or dp[i-1][j -arr[i-1]]

# Base Conditions:
# dp[0][0] = True -> empty subset can make sum 0
# dp[i][0] = True for all i -> sum 0 is always possible.
# dp[0][j] = False for j > 0 -> can't form positive sum using 0 elements.


def is_subset_sum(arr: list[int], target: int):
    n = len(arr)

    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][target]


# Example Usage

arr = [3, 34, 4, 12, 5, 2]
target = 9

result = is_subset_sum(arr, target)
print("Is subset with given sum possible:", result)
