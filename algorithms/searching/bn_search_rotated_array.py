# To search for a target element in a rotated sorted array in (O(log n)) time and O(1) 
# space, we can use a modified binary search that identifies which half of the array is 
# properly sorted

# Explanation

# A rotated sorted array looks like : [4, 5, 6, 7, 0, 1, 2, 3]

# Algorithm

# 1. Initialize two pointers: low = 0 and high = n - 1.
# 2. Loop while low <= high:
# 	• Calculate mid = low + (high - low) / 2.
# 	• If arr[mid] == target, return mid.
# 	• Check left sortedness (arr[low] <= arr[mid]):
# 		• If arr[low] <= target and target < arr[mid], then high = mid - 1.
# 		• Else, low = mid + 1.
# 	• Otherwise (right sortedness is guaranteed):
# 		• If arr[mid] < target and target <= arr[high], then low = mid + 1.
# 		• Else, high = mid - 1.
# 3. If the loop ends without finding the target, return -1



def search_rotated(arr : list[int], target : int):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
               
        else: 
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1



# Example Usage

arr = [4, 5, 6, 7, 0, 1, 2, 3]
target = 7

print(f"Array : {arr}")
print(f"Index of element {target} in {arr} is {search_rotated(arr, target)}")