# A rolling hash is a specialized hash function designed to compute the hash value of a 
# sliding window over a data stream (such as a string or a file) in constant time O(1).

# Explanation

# With rolling hash , we reuse the previous hash value to calculate the next one in 
# constant time O(1)
# it treats the string like a number in a base system (like base p). with modulas M to 
# avoid overflow

# Formula for a string
# s = s[0] s[1] ... s[n-1] is :
# H(s) = (s[0] . p^(n-1) + s[1] . p^(n-2) + ... + s[n-1]) mod M

# when sliding over text , we remove the first character and add the next character to 
# update the hash efficiently


p = 31
M = 10**9 + 9

def compute_hash(s : str):
    h = 0
    p_pow = 1
    for char in s:
        h = (h + (ord(char) - 96) * p_pow) % M
        p_pow = (p_pow * p) % M
    return h


## Example usage

text = 'abacaba'
pattern = 'aba'

pattern_hash = compute_hash(pattern)
n = len(text)
prefix_hash = [0] * (n + 1)
p_pow = [1] * (n + 1)

for i in range(1 , n + 1):
    prefix_hash[i] = (prefix_hash[i - 1] + (ord(text[i - 1]) - 96) * p_pow[i - 1]) % M
    p_pow[i] = (p_pow[i - 1] * p) % M

matches = []
for i in range(n - len(pattern) + 1):
    curr_hash = (prefix_hash[i + len(pattern)] - prefix_hash[i] + M) % M

    if curr_hash == (pattern_hash * p_pow[i]) % M:
        matches.append(i)
        
print(f'Pattern founded at indices : {matches}')