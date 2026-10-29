# Quick Sort is a highly efficient, comparison-based sorting algorithm that uses a 
# divide-and-conquer strategy to order elements. It works by selecting a "pivot" element 
# from the array and partitioning the other elements into two sub-arrays according to 
# whether they are less than or greater than the pivot

# Explanation

# 1. Choose a Pivot: Pick an element from the array (common choices include the first 
# element, the last element, the median, or a random element)

# 2. Partitioning: Rearrange the array so that all elements smaller than the pivot go 
# to its left, and all elements greater go to its right. The pivot is now in its final, 
# correct position

# 3. Recursion: Recursively apply the same steps to the sub-array of smaller elements 
# and the sub-array of larger elements.


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
    
def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)
        
        
# Example Usage

arr = [3, 67, 23, 1, 7, 9, 45]

print(f'Original Array : {arr}')
quicksort(arr , 0, len(arr) - 1)
print(f'Sorted Array : {arr}')