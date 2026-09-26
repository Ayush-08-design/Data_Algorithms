# The Meet-in-the-Middle algorithm is an optimization technique that reduces the 
# time complexity of an exponential search problem by splitting the search space 
# into two equal halves, solving them independently, and combining their results.

# Procedure
# 1. Split: Divide the array of N elements into two smaller arrays of size N/2 
# (Left and Right).
# 2. Brute Force Both Halves: Naively generate all possible subset sums 
# for both halves independently. If N = 40, each side generates 2²⁰ possible sums, 
# producing two lists, L1 and L2.
# 3. Sort one half: Sort one of the lists (e.g., L2) 
# so it can be searched efficiently.
# 4. Meet in the middle: Iterate through each sum x in L1. For each x, you need a 
# complementary value y in L2 such that x + y = S (or x + y ≤ S,
# depending on the problem). Use binary search on L2 to find if the complement (S - x) 
# exists.


# Problem statement
# Given an array of integers and a target sum , find if there exists a subset 
# whose sum is equal to the target

from bisect import bisect_left

def subset_sum(arr):
    res = [0]
    for x in arr:
        new_sums = [x + y for y in res]
        res += new_sums
    return res

def meet_in_the_middle(nums , target):
    n = len(nums)
    left = nums[: n//2]
    right = nums[n//2 :]
    
    left_sums = subset_sum(left)
    right_sums = subset_sum(right)
    right_sums.sort()
    
    for s in left_sums:
        needed = target - s
        idx = bisect_left(right_sums , needed)
        if idx < len(right_sums) and right_sums[idx] == needed:
            return True
    return False
    
    
# Example usage
nums = [3 , 34, 4, 12 , 5 , 2]
target = 9
result = meet_in_the_middle(nums , target)

print('Exists : ' , result)