# Counting sort is a non-comparison-based integer sorting algorithm. It works by 
# counting the number of objects having distinct key values, and then using arithmetic 
# to calculate the positions of each key value in the output sequence.

# 
# Explanation

# Imagine we have an input array: [4, 2, 2, 8, 3, 3, 1]

# 1. Count Frequencies: Create a "Count Array" of size (k) 
# (the maximum value in your input + 1). Iterate through the input array and count how 
# many times each number appears.

# • Count Array: [0, 1, 2, 2, 1, 0, 0, 0, 1] (e.g., there is one 1, two 2s, two 3s, etc.)
# 2. Accumulate Sums (Prefix Sum): Modify the Count Array so that each element at index 
# i stores the sum of previous counts. This determines the actual target position/index 
# of each element in the output array.

# • Accumulated Count Array: [0, 1, 3, 5, 6, 6, 6, 6, 7]
# 3. Build Output Array: Iterate through the original input array 
# (ideally from right to left to maintain stability). Look up the value in the Count 
# Array to find its correct position in the output array, place it there,
# and decrement that count by 1


def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    sorted_arr = []
    for i in range(len(count)):
        for _ in range(count[i]):
            sorted_arr.append(i)
            
    return sorted_arr


# Example Usage:

nums = [4, 2, 2, 8, 3, 3, 1]

result = counting_sort(nums)

print(f'Original Array : {nums}, Sorted Array : {result}')