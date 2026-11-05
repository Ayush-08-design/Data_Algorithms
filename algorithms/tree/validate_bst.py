# A Binary search tree is binary tree in which every node ,
# all nodes in its left subtree have smaller values and all nodes in its right subtree
# have larger values

# Validate bst algorithm checks whether a given binary tree satisfies the bst properties

# Explanation

# To validate a BST, we can use recursion. the idea is to ensure that each node's value
# lies within a range:

# For a root node , the range is (-inf , +inf)

# For the left child, the range becomes (min_value, parent_value).
# For the right child, the range becomes (parent_value, max_value).

# If every node satisfies its range condition, the tree is a valid BST


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def isValidateBST(node: Node, min_value=float("-inf"), max_value=float("inf")):
    if node is None:
        return True

    if not (min_value < node.val < max_value):
        return False

    return isValidateBST(node.left, min_value, node.val) and isValidateBST(
        node.right, node.val, max_value
    )


# Example Usage

# Valid BST

root = Node(5)
root.left = Node(3)
root.right = Node(7)

root.left.left = Node(2)
root.left.right = Node(4)

result = isValidateBST(root)

print(f"Is the tree a BST : {result}")
