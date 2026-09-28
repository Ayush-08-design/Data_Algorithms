# Mo's Algorithm is an offline query optimization technique used to answer 
# multiple range queries on a static array in \(O((N + Q) \sqrt{N})\) time complexity. 

# Divide the array of size N into blocks of size \(B = \lfloor\sqrt{N}\rfloor\).
# Group and sort queries based on the block index of their left endpoint (L / B). 
# If two queries have their left endpoint in the same block, 
# sort them by their right endpoint (R) in ascending order. 

# Problem
# Given an array , answer q queries where each query asks for the 
# sum of elements beetween indices L and R

import math

def MO_algorithm(arr , queries):
    n = len(arr)
    q = len(queries)
    
    block_size = int(math.sqrt(n))
    
    queries.sort(key = lambda x : (x[0] // block_size , x[1]))
    
    currL , currR , currSum = 0 , 0 , 0
    res = [0] * q
    for i in range(q):
        L , R = queries[i]
        while currL < L:
            currSum -= arr[currL]
            currL += 1
        
        while currL > L:
            currL -= 1
            currSum += arr[currL]
            
        while currR <= R:
            currSum += arr[currR]
            currR += 1
        
        while currR > R + 1:
            currR -= 1
            currSum -= arr[currR]
        res[i] = currSum
        
    return res



# Example Usage
print('ff')
arr = [1 , 2, 3, 4, 5, 6]

queries = [(0 , 2) , (1 , 3) , (2 , 5), (0 , 5)]
answers = MO_algorithm(arr , queries)

for i , ans in enumerate(answers):
    print(f'query {i + 1} : Sum = {ans}')