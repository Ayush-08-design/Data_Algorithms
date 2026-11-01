# Binary search is an efficient algorithm for finding a target value within a sorted array
# It works by repeatedly dividing the search interval in half
# achieving a time complexity of (O(log n))

# Explanation :

# 1. Start with two pointers: low at the beginning and high at the end of the array.
# 2. Calculate the middle index: mid = low + (high - low) // 2.
# 3. Compare the target value to the element at mid:
# 	• If they are equal, the target is found.
# 	• If the target is smaller, narrow the search to the left half (high = mid - 1).
# 	• If the target is larger, narrow the search to the right half (low = mid + 1).
# 4. Repeat until the target is found or low exceeds high

# Binary search can be tweaked to find out not only whether an element exists, but also 
# to find the position where it could be inserted while maintaining order


def lower_bound(arr : list[int], target : int):
    low, high = 0, len(arr)
    
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

def upper_bound(arr : list[int], target : int):
    low, high = 0, len(arr)
    
    while low < high:
        mid = low + (high - low) // 2
        
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low



# Example Usage

arr = [1, 2, 4, 4, 4, 6, 7, 9]

target = 4

print(f"Array : {arr} , Lower bound : {lower_bound(arr, target)}, Upper bound : {upper_bound(arr, target)}")