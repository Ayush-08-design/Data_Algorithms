# Radix Sort is a efficient, non-comparative sorting algorithm that sorts data with 
# integer keys by grouping keys by the individual digits that share the same significant
# position and value.

# Explanation

# Radix sort works digit by digit, starting from the least significant digit (LSD) to the 
# most significant digit (MSD) 

# For each digit position, it uses a stable sort (like counting sort) to order elements 
# according to that digit

# After processing all digits the array becomes completely sorted

# Time Complexity: O(d . (n + k)), 
# where (n) is the number of elements, 
# (d) is the number of digits in the maximum number, and (k) is the number of 
# possible values for a digit (the radix or base, e.g., 10 for decimals).


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i-1]
        
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        
    for i in range(n):
        arr[i] = output[i]
        
def radix_sort(arr):
    if not arr:
        return arr
    
    max_num = max(arr)
    
    exp = 1
    
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
        
    return arr



# Example usage:

nums = [34, 222, 76, 90, 8, 24, 2, 686]

print("Original array:", nums)
print("Sorted array:", radix_sort(nums))