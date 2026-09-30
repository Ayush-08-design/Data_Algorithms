# The Two Pointers Technique is an efficient algorithmic approach that uses 
# two reference indices or positions to traverse a data structure—such as an array, 
# string, or linked list—often reducing time complexity from O(n²) to O(n)

# Core Strategies

# • Opposite Ends (Converging): One pointer starts at the beginning and the other 
# starts at the end, moving toward each other until they meet. 
# This is ideal for sorted arrays (like finding a target sum) or checking for palindromes.

# • Same Direction (Parallel / Fast-Slow): Both pointers start at the beginning, 
# but move at different speeds or conditions. This is frequently used in linked lists 
# for cycle detection (Tortoise and Hare) or removing duplicates.


## Opposite Ends

def two_sum_sorted(arr : list[int] , target : int):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        
        sm = arr[left] + arr[right]
        
        if sm == target:
            return left , right
        elif sm < target:
            left += 1
        else:
            right -= 1
    return -1 , -1

## Same Direction

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


## Example Usage

# two sum sorted
arr = [-1 , 2, 4, 7, 10]
target = 9
idx = two_sum_sorted(arr , target)
print(f'Array : {arr} , Target : {target} , Indices : {idx}')

# find the middle of a linked list
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)

print('Linked List :')
curr = head
while curr:
    print(curr.val , end = ' ')
    curr = curr.next

print()

middle = find_middle(head)
print(f'Middle : {middle.val}')