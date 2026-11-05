# The Euler Tour Technique (ETT) is a tree traversal method used to flatten a tree into 
# an array such that each node's subtree corresponds to a contiguous segment. 
# It's mainly used in problems involving subtree queries or lowest  common ancestor (LCA) 
# computations efficiently .

# Explanation

# Imagine performing a Depth First Search (DFS) on a tree. When you enter a node , 
# you record it when you exit that node after visiting all children you record it again. 
# This creates a sequence that represents the entry and exit times (or positions) of each 
# node - known an the euler tour of the tree.

# So for a tree like this

#          1
#        / | \
#       2  3  4
#         / \
#        5   6

# The euler tour traversal order might look like this:
# 1, 2, 2, 3, 5, 5, 6, 6, 3, 4, 4, 1

# Every node appers twice (on entry and exit)

# This helps represent a node's subtree as a range in this array,
# enabling range queries (like sum, min, etc) via segment Tree or Fenwick Tree

graph = {
    1 : [2, 3, 4],
    2 : [],
    3 : [5, 6],
    4 : [],
    5 : [],
    6 : [],
}

euler_tour = []

entry_time = {}

exit_time = {}
time = 0

def dfs(node, parent):
    global time

    time += 1
    
    entry_time[node] = time
    euler_tour.append(node)
    
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
            euler_tour.append(node)
    time += 1
    exit_time[node] = time


# Example Usage

dfs(1, -1)

print(f"Euler Tour Sequence : {euler_tour}")

print(f"Entry time : {entry_time}")

print(f"Exit time : {exit_time}")