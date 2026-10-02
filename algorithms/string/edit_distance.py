# Edit distance is the minimum number of operations (insert , delete , replace) 
# required to convert one string to another
# The Wagner-Fischer algorithm solves this using dynamic programming in O(m * n) time

# Explanation

# Suppose we want to transform string word1 into word2

# Allowed opeartions are :
# 1. Insert a character , 2. Delete a character , 3. Replace a character
# we use a dp table , where dp[i][j] = minimum opeartions to convert first i characters
# of word1 into word2

# Fill base cases
# if one string is empty - need insertions/deletions.
# If chars match -> No operation needed
# Otherwise -> 1 + min(insert , delete , replace)


def edit_distance(s1 : str , s2 : str):
    m , n = len(s1) , len(s2)
    
    dp = [[0] * (n+1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1 , m + 1):
        for j in range(1 , n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j] , dp[i][j - 1] , dp[i - 1][j - 1])
    return dp[m][n]


## Example Usage

word1 = 'kitten'
word2 = 'sitting'

result = edit_distance(word1 , word2)

print(f'Edit distance between {word1} and {word2} is : {result}')