# The Dutch National Flag (DNF) algorithm, designed by Edsger Dijkstra, 
# is a three-way partitioning algorithm that sorts an array containing three distinct 
# values (typically 0s, 1s, and 2s, representing the red, white, and blue bands of 
# the Dutch flag). It achieves this in O(n) time complexity and O(1) space complexity 
# using a single pass.


# Core Logic & Pointers
# The algorithm maintains four distinct sections in the array by utilizing 
# three pointers (low, mid, and high):

# 1. arr[0 ... low-1]: Contains all 0s (Bottom section).
# 2. arr[low ... mid-1]: Contains all 1s (Middle section).
# 3. arr[mid ... high]: Unprocessed elements (Unknown section).
# 4. arr[high+1 ... n-1]: Contains all 2s (Top section).



def dutch_national_flag(arr : list[int]):
    low , mid , high = 0 , 0 , len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low] , arr[mid] = arr[mid] , arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid] , arr[high] = arr[high] , arr[mid]
            high -= 1



## Example Usage

arr = [2 , 0 , 1, 1, 0 , 1]

print(f'Array : {arr}')
dutch_national_flag(arr)
print(f'Sorted Array : {arr}')
    