# kadane's algorithm is a dynamic programming approach to find the maximum sum of a 
# contiguous subarray in the array. it efficiently solves the problem in O(n) time 
# in a single pass

# Explanation
# the idea is to scan through the array and keep track of the maximum subarray sum 
# ending at each position 

# At every index we have two choices : 

# 1. Extend the previous subarray with the current element 

# 2. Start a new subarray from the current element . we take the maximum of these choices and update the global maximum

def kadane(arr : list[int]):
    max_so_far = arr[0]
    curr_max = arr[0]
    
    for i in range(1 , len(arr)):
        curr_max = max(arr[i] , curr_max + arr[i])
        max_so_far = max(max_so_far , curr_max)
    return max_so_far


## Example Usage
arr = [2 ,4 ,-1 ,7, -10 , 6, 3, -5 , -3 , 2]

print('Maximum subarray sum :' , kadane(arr))