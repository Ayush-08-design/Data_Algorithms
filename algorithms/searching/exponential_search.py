# Exponential Search algorithm finds a range where the target key resides and then 
# performs a binary search within that range. It achieves a time complexity of (O(log i)),
# where i is the index of the element being searched, making it exceptionally fast for 
# finding elements near the beginning of bounded or unbounded arrays.

# Explanation

# The algorithm runs in two distinct phases

# 1. Range Bounding (Exponential Phase):
# 	• Start at index 1.
# 	• If the element at the current index is less than the target, double the index ((1, 2, 4, 8, 16, ....)).
# 	• Repeat until you find an element greater than or equal to the target, or you exceed the array boundaries.
# 2. Binary Search Phase:
# 	• Once a range is established (between index // 2 and (min(index , array length - 1))

# perform a standard binary search within these boundaries.

# When to use
# Unbounded/Infinite Arrays: Ideal when the size of the array is unknown or infinite, as it doesn't require len(arr) to begin.
# Elements Near the Beginning: Outperforms standard binary search (O(log n)) if the target element is located early in a massive array (i << n).


def binary_search(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    if not arr:
        return -1
    
    if arr[0] == target:
        return 0
    
    bound = 1
    n = len(arr)
    while bound < n and arr[bound] <= target:
        if arr[bound] == target:
            return bound
        bound *= 2
        
    left = bound // 2
    right = min(bound, n - 1)
    
    return binary_search(arr, left, right, target)


# Example Usage

arr = [1, 2, 4, 4, 4, 6, 7, 9]

target = 4

idx = exponential_search(arr, target)

print(f"Position of {target} in array {arr} is {idx}")