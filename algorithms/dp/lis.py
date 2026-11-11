# The Longest Increasing Subsequence (LIS) is the longest subsequence in a given sequence
# where all elements are in strictly increasing order. The elements of the subsequence 
# don't need to be contiguous, but their order must be preserved.

# Explanation

# Imagine you have an array of numbers, and you want to find the longest possible sequence
# that increases as you move forward.

# Example:

# Input = [10, 22, 9, 33, 21, 50, 41, 60]

# Possible increasing subsequences
# [10, 22, 33, 50, 60]
# [10, 22, 33, 41, 60]

# Both have length 5 , so the LIS length is 5
# We can solve this problem in O(n**2) using dynamic programming

# For each element, check all previous elements.
# If the current element is greater than a previous one, we can extend the subsequence.

# Store the length of the LIS ending at each element and take the maximum.



def longest_increasing_subsequence(arr: list[int]):
    n = len(arr)
    
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)



# Example Usage

arr = [10, 22, 9, 33, 21, 50, 41, 60]

result = longest_increasing_subsequence(arr)

print(f"Length of longest increasing subsequence is : {result}")