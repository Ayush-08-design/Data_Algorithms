# A subset enumeration algorithm generates all possible subsets (the power set) of a 
# given set or array

# Recursively decide whether to include or exclude each element at index i.
# Bit Manipulation: Iterate integers from 0 to \(2^n - 1\); 
# the set bits of each integer indicate which elements to include.
# Lexicographic / Incremental: Generate subsets in a dictionary or monotonically 
# increasing size order. 

## BitMasking

def generate_subsets(arr : list[int]):
    n = len(arr)
    total_subsets = 1 << n

    result = []
    
    for mask in range(total_subsets):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
                
        result.append(subset)
    return result


## Example usage
arr = [3 ,6 ,1 ,8]
print(generate_subsets(arr))