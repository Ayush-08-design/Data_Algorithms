# Merge Sort is a highly efficient, sorting algorithm that uses a divide-and-conquer 
# strategy to sort an array or list. It breaks down a large collection into 
# single-element sub-problems, sorts them, and then merges them back together in order


# Explanation

# Merge Sort operates via two primary phases:
# 1. Divide (Recursive): Find the midpoint of the array and recursively split it into 
# left and right halves until each sub-array contains only one element.

# 2. Conquer (Merge): Compare the elements of the smallest sub-arrays and merge them back
# together in sorted order into a new temporary array.


def merge(left, right):
    merged = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged

def merge_sort(arr : list[int]):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    
    left = arr[:mid]
    right = arr[mid:]
    
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)


# Example Usage

arr = [5, 23, 89, 1, 6, 34, 8]

result = merge_sort(arr)

print(f'Original Array : {arr}, Sorted Array : {result}')