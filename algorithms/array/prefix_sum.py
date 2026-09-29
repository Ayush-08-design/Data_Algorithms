# Prefix sum (aka cumulative sum) is an array where each element at index i stores the 
# sum of all elements from the original array up to i. it allows answering range sum 
# queries (sum of arr[1..r]) in o(1) after an O(n) preprocessing

# Compute a prefix array where prefix[i] = arr[0] + arr[1] + ........ + arr[i].
# Then the sum of any subarray arr[1..r] (inclusive) is
# prefix[r] if 1 == 0 , otherwise
# prefix[r] - prefix[i - 1].

# Use cases - fast range sum queries , 1d , 2d cumulative sum

def build_prefix(arr : list[int]):
    pref = [0] * len(arr)
    for idx , val in enumerate(arr):
        if idx == 0:
            pref[idx] = val
        else:
            pref[idx] = pref[idx - 1] + val
    return pref

def range_sum(pref , l , r):
    if l == 0:
        return pref[r]
    return pref[r] - pref[l - 1]


# Example Usage

arr = [2 ,4 ,5 , 7, 9, 34, 6]

print(f'Original array : {arr}')
pref = build_prefix(arr)
print(f'Prefix sum array : {pref}')

queries = [(0 ,2) , (4 , 5) , (1 , 6)]

for l , r in queries:
    s = range_sum(pref , l , r)
    print(f'Sum arr [{l}..{r}] = {s}')
    
    
## Preprocessing : O(n) , Extra space : O(n)
# Query time : O(1)