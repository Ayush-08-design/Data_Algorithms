# Ternary search is a divide-and-conquer sorting/searching algorithm that finds the 
# position of a target value within a sorted array, or determines the extremum 
# (maximum or minimum) of a unimodal function by dividing the search space into 
# three equal parts

# For finding the position of a target value within a sorted array

# Unlike binary search which uses one midpoint (mid), ternary search calculates two 
# midpoints (mid1 and mid2), splitting the array into three segments:

# 1. Left segment: From low to mid1 - 1
# 2. Middle segment: From mid1 + 1 to mid2 - 1
# 3. Right segment: From mid2 + 1 to high


def ternary_search(arr: list[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
            
        if target < arr[mid1]:
            high = mid1 - 1
        elif target > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1 


arr = [1, 2, 4, 4, 4, 6, 7, 9]

target = 7

print(ternary_search(arr, target))



# For finding the extremum (maximum or minimum) of a unimodal function

# we can split the range into three equal segments.then evaluate the function (f(x)) at both points:

# • If (f(m1) < f(m2)): The maximum cannot be in the leftmost segment [low, m1]. 
# The peak must be to the right of m1. we can update low = m1

# • If (f(m1) > f(m2)): The maximum cannot be in the rightmost segment [m2, high]. 
# The peak must be to the left of m2. we can update high = m2

# • If (f(m1) == f(m2)): The peak lies between m1 and m2. we can update both low = m1 
# and high = m2

def f(x: float) -> float: # Our function
    return -(x - 3) ** 2 + 5

def ternary_search_max(low, high, func, iterations = 100):
    for i in range(iterations):
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        
        if func(mid1) < func(mid2):
            low = mid1
        else:
            high = mid2
    return (low + high) / 2


l = 0
r = 40

estimate = ternary_search_max(l , r, f)

print(f'Max value at {estimate} in range {l} - {r}')
