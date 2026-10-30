# Floyd's Cycle Detection Algorithm (also known as the Hare and Tortoise Algorithm) is a 
# pointer-based algorithm used to detect loops in linked lists or sequences. 
# It operates using two pointers moving through the sequence at different speeds

# Explanation
# • Tortoise (Slow Pointer): Moves forward by one step at a time.
# • Hare (Fast Pointer): Moves forward by two steps at a time.
# If there is no cycle, the hare will eventually reach the end of the list (None). 
# If a cycle exists, the hare will enter the loop first and eventually "lap" the tortoise,
# causing both pointers to meet at the exact same node.


class Node:
    def __init__(self, value):
        self.val = value
        self.next : Node | None = None

def has_cycle(head : Node) -> bool:
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast: 
            return True
            
    return False


# Example Usage

# List with no cycle
head = Node(0)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)

result = has_cycle(head)

print(f"Cycle Detected : {result}")

# List with cycle

head2 = Node(0)
head2.next = Node(1)
head2.next.next = head2

result2 = has_cycle(head2)

print(f"Cycle Detected : {result2}")