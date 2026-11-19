# Centroid decomposition is a divide and conquer algorithm on trees.

# It recursively breaks a tree into smaller subtrees using centroids-nodes that
# balance the tree such that no resulting subtree has more than half the total nodes.

# It is mainly used in path queries, tree distance problems, and optimization on trees.

# Explanation

# A centroid of a tree is a node that, when removed, splits the tree into subtrees,
# each with at most n/2 nodes.

# The centroid Decomposition recursively:

# Finds the centroid of the current tree.
# Removes the centroid to divide the tree into smaller parts
# Repeats the process on each subtree

# This forms a Centroid tree, which can be used to solve problems efficiently
# that are otherwise expensive on the original tree (e.g - shortest paths, subtree queries, etc).


from collections import defaultdict

g = defaultdict(list)

edges = [(1, 2), (1, 3), (2, 4), (2, 5)]

for u, v in edges:
    g[u].append(v)
    g[v].append(u)

n = 5

subtree_size = [0] * (n + 1)
visited = [False] * (n + 1)


def dfs_size(u, p):
    subtree_size[u] = 1
    for v in g[u]:
        if v != p and not visited[v]:
            subtree_size[u] += dfs_size(v, u)
    return subtree_size[u]


def find_centroid(u, p, total_nodes):
    for v in g[u]:
        if v != p and not visited[v] and subtree_size[v] > total_nodes // 2:
            return find_centroid(v, u, total_nodes)
        return u


def decompose(u, parent):
    total_nodes = dfs_size(u, -1)
    centroid = find_centroid(u, -1, total_nodes)

    visited[centroid] = True
    print(f"Centroid Found: {centroid}, Parent: {parent}")

    for v in g[centroid]:
        if not visited[v]:
            decompose(v, centroid)


decompose(1, -1)
