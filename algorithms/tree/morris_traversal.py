# Morris Inorder Traversal is a tree traversal algorithm that visits all nodes of a 
# binary tree in-order (Left, Root, Right) using O(1) auxiliary space and O(n) time 
# complexity.

# Explanaion

# The core challenge of traversing without a stack is knowing how to step "up" to a root
# node once you hit the bottom-right of its left subtree. 
# Morris traversal solves this by finding the in-order predecessor (the rightmost node 
# in the left subtree) and temporarily pointing its right pointer to the current root.

# For any current node:

# 1. If current has no left child:
# 	• Process/visit the current node.
# 	• Move to its right child: current = current.right

# 2. If current has a left child:
# Find its in-order predecessor (go left once, then go right as far as possible).

# Case A (Thread creation): If the predecessor's right pointer is null, point it to current. 
    # Then, move current to its left child (current = current.left).
# Case B (Thread removal): If the predecessor's right pointer already points to 
    # current, it means the left subtree has already been fully traversed. Revert the thread 
    # by setting right back to null, visit the current node, and move to its 
    # right child (current = current.right).


class Node:
    def __init__(self, val : int):
        self.val = val
        self.left = None
        self.right = None

def morrisTraversal(root: Node):
    result = []
    curr = root

    while curr:
        if curr.left is None:
            result.append(curr.val)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right
                
            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                result.append(curr.val)
                curr = curr.right
    return result




# Example Usage

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

output = morrisTraversal(root)

print(f"Inorder Traversal : {output}")