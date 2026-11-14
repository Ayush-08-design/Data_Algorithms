# The Unbounded Knapsack algorithm finds the maximum total value we can pack into a
# knapsack of capacity W when we have an unlimited supply of each item.

# Unlike the 0/1 Knapsack problem where each item can be picked at most once,
# here we can pick the same item multiple times.

# Explanation

# define a 1D array dp of size W + 1.

# Where dp[w] be the maximum value achievable with capacity exactly w.
# Base Case: dp[0] = 0

# For each capacity w form 1 to w, try every item i with weight wt[i]. 

# if wt[i] <= w:
# candidate value = dp[w - wt[i]] + val[i]. 
# Set dp[w] = max(dp[w], candidate)

# This 1D bottom-up DP naturally allows resusing items because when computing dp[w] we may use dp[w - wt] which itself may include item i already

# Optionally store a keep[w] array to reconstruct which item was chosen last for capacity w.


def unbounded_knapsack(W, wt, val):
    dp = [0] * (W + 1)
    keep = [-1] * (W + 1)
    n = len(wt)
    for w in range(1, W + 1):
        for i in range(n):
            if wt[i] <= w:
                dp[w] = max(dp[w], val[i] + dp[w - wt[i]])
                keep[w] = i

    return dp[W], keep


# Example usage:
capacity = 10
weights = [2, 3, 5]
values = [15, 20, 50]

max_value, keep = unbounded_knapsack(capacity, weights, values)
print(f"Max Value : {max_value}")


result_items = []
cap = capacity
while cap > 0 and keep[cap] != 1:
    idx = keep[cap]
    result_items.append(idx)
    cap -= weights[idx]
    
result_pairs = [(weights[i], values[i]) for i in result_items]

print(f"Chosen items (weight , value) in selection order : {result_pairs}")