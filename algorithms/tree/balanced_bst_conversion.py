# A Balanced Binary Search Tree (BST) is a BST where the difference between heights
# of left and right subtrees of any node is at most 1.

# Balanced BST conversion algorithms take an unbalanced BST or a sorted array and
# transform it into a height-balanced BST to optimize search, insertion, and deletion operations.

# Explanation

# In many applications, a BST may become skewed (like a linked-list) over time due to
# sequential insertions.
# This causes search operations to degrade from O(log n) to O(n).

# To convert a BST (or sorted array) into a balanced BST.
# Perform an inorder traversal to get elements in sorted order.

# Use the sorted list to build a balanced BST using the middle element as root
# recursively.

# From sorted array.

# Recursively pick the middle element as root.
# Left subarray becomes left subtree, right subarray becomes right subtree.

# Both approaches ensure that the height difference between left and right subtrees of
# every node is minimal.


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left: Node = None
        self.right: Node = None


def inorder(root: Node | None, arr):
    if root:
        inorder(root.left, arr)
        arr.append(root.val)
        inorder(root.right, arr)


def array_to_bst(arr: list[int]):
    if not arr:
        return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = array_to_bst(arr[:mid])
    root.right = array_to_bst(arr[mid + 1 :])
    return root


def show_tree(root: Node):
    if root:
        show_tree(root.left)
        print(root.val, end=" ")
        show_tree(root.right)



# Example Usage

root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.right = Node(15)


sorted_array = []
inorder(root, sorted_array)
print(f"Sorted array from BST: {sorted_array}")

balanced_root = array_to_bst(sorted_array)

print("Inorder of balanced BST: ", end="")
show_tree(balanced_root)
