# Heap Sort is a highly efficient, comparison-based sorting algorithm that uses a 
# binary heap data structure to sort elements. It conceptually divides the input array 
# into a sorted and an unsorted region, iteratively shrinking the unsorted region by
# extracting its largest element and moving it to the sorted region

# Explanation

# 1. First we build a max heap from input array
# 2. the largest element (root of the heap) is swapped with the last element of the array.
# 3. we reduce the heap size by 1 and heapify the root element again to restore the Max-Heap property.
# Repeat these two steps [2 , 3] util all elements are sorted

# Heap sort runs in O(n log n) time and does not require extra space beyond the input array (in-place sorting)

def heapify(arr , n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
        
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n , i)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        
        
# Example Usage

arr = [4, 7, 2, 9, 12, 0, 45]

print(f'Original Array : {arr}')
heap_sort(arr)
print(f'Sorted Array : {arr}')