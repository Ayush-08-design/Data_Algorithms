# The Longest Common Subsequence (LCS) algorithm that finds the longest sequence of elements
# that appears in the same relative order across multiple strings or arrays.
# Unlike a substring, the characters of a subsequence do not need to be consecutive in the
# original text; they just need to maintain their relative order.

# The most efficient way to solve this problem is via Dynamic Programming (Tabulation).
# By building a 2D table dp of size (m+1) x (n+1),
# where m and n are the lengths of the two strings.

# Explanation

# We build a 2D dp table [dp], where dp[i][j] is the length of the LCS of the prefixes A[:i] and B[:j].

# Recurrence:

# If A[i-1] == B[j-1]:
# dp[i][j] = dp[i-1][j-1] + 1 (take that matched character)

# Else:
# dp[i][j] = max(dp[i-1][j], dp[i][j-1]) (skip one char from A and B)

# After filling the table, we can reconstruct one LCS by tracing back from dp[n][m] to dp[0][0].


def lcs(a, b):
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    lcs_chars = []
    i, j = n, m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs_chars.append(a[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    lcs_string = "".join(reversed(lcs_chars))
    return dp[n][m], lcs_string


# Example Usage
a = "AGGTAB"
b = "GXTXAYB"

length, seq = lcs(a, b)

print(f"String a: {a}, String b: {b}, LCS length: {length}, Seq: {seq}")
