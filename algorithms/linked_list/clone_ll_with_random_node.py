# A clone linked list with random pointers is an algorithm used to create a deep copy of
# a linked list where each node has two pointers:
# next -> Points to next Node
# random -> Points to any random node in the list

# the goal is to create a new list with same structure and connections

# Explanation
# Unlike a normal linked list , here each node also has a random pointer that can point 
# anywhere so we need to copy those random pointers also.

# Steps to clone
# Insert copies of each node right after the original node.
# Assign random pointers to these copies nodes
# Detach the original and cloned linked lists into two seperate linked list. This
# Ensures we get an exact deep copy without losing random connections

class Node:
    def __init__(self, value):
        self.val = value
        self.next : Node | None = None
        self.random : Node | None = None
        
def clonelinkedlist(head : Node):
    if not head:
        return None
    curr = head
    while curr:
        new_node = Node(curr.val)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next
        
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    curr = head
    clone_head = head.next
    while curr:
        copy = curr.next
        curr.next = copy.next
        if copy.next:
            copy.next = copy.next.next
        curr = curr.next
    return clone_head

def print_ll(head : Node):
    result = []
    while head:
        rand = head.random.val if head.random else None
        result.append(f"([{head.val}], random = [{rand}])")
        head = head.next
    return result



# Example Usage

head = Node(0)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)

head.random = head.next.next
head.random.random = head

print(f"Original List : {print_ll(head)}")

cloned = clonelinkedlist(head)

print(f"Cloned List : {print_ll(cloned)}")