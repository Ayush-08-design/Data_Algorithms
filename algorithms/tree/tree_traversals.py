# Tree Traversal Algorithms.

# DFS (Depth First Search) explores a tree graph by going as deep as possible along
# one branch before backtracking.

# BFS (Breadth First Search) explores a tree or graph level by level visiting all nodes
# at the current depth before moving deeper.

# Explanation

# DFS can be implemented recursively (stack via function calls) or iteratively (using an explicit stack).
# BFS is implemented using a queue (FIFO order) to explore nodes level by level

# Both traversals are fundamental for understading tree/graph algorithms such as shortest
# paths, connected components, and cycle detection.


# Tree Node


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


# DFS


def dfs(root, nodes):
    if not root:
        return
    nodes.append(root.val)
    dfs(root.left, nodes)
    dfs(root.right, nodes)
    return nodes


from collections import deque

# BFS


def bfs(root: Node):

    nodes = []

    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        nodes.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return nodes


# Example Usage

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


dfs_nodes = dfs(root, [])

bfs_nodes = bfs(root)

print(f"dfs nodes : {dfs_nodes}")

print(f"bfs nodes : {bfs_nodes}")
