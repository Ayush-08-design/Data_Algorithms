# The Matrix Chain Multiplication (MCM) algorithm is a classic Dynamic Programming algorithm.
# It finds the most efficient way to parenthesize a sequence of matrices so that the
# total number of scalar multiplications is minimized.

# Although matrix multiplication is associative—meaning the final product is identical
# regardless of the grouping—the order of operations (parenthesization)
# drastically changes the computational cost.

# Explanation

# Steps:
# Let matrices A1, A2, ..., An with dimensions stored in array dims where dim[i-1] * dims[i] is the dimensions of Ai

# Define dp[i][j] as the minimum number of multiplications needed to compute the product of matrices from i to j

# Recurrence relation:
# dp[i][j] = min(dp[i][k] + dp[k+1][j] + dims[i-1] * dims[k] * dims[j]) for all i <= k < j

# Base case: dp[i][i] = 0 (single matrix needs no multiplication).
# Fill the table bottom-up and return dp[1][n]


def matrix_chain_order(dims):
    n = len(dims)
    dp = [[0] * n for _ in range(n)]

    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                dp[i][j] = min(dp[i][j], q)

    return dp[1][n - 1]


# Example Usage

dims = [10, 20, 30, 40, 30]

min_cost = matrix_chain_order(dims)

print(f"Minimum number of multiplications : {min_cost}")
