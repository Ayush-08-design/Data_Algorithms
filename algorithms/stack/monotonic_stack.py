# A monotonic stack is a specialized stack data structure that maintains its elements 
# in a fixed sorted order either increasing or decreasing from bottom to top

# Explanation

# Push & Pop Rule: When we push a new element, we compare it with the top of the 
# stack. If pushing it violates the sorted order, we pop elements from the stack until 
# the order is restored, and then push the new element.

# Time Complexity: Each element is pushed and popped at most once, reducing O(n²) 
# brute-force array searches down to linear O(n) time.

# Next Greater Element

def next_greater_element(arr : list[int]):
    n = len(arr)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    return result

# Example Usage

arr = [4, 7, 2, 89, 4, 12, 0]

output = next_greater_element(arr)

print(f"Input array : {arr}")

print(f'Output array : {output}')