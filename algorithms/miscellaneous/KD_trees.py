# A KD-Tree (K-Dimensional Tree) is a space-partitioning data structure used to 
# organize points in a k-dimensional space. It functions as a specialized binary search 
# tree where every node represents a k-dimensional point. KD-Trees are heavily used to 
# optimize multidimensional spatial operations like Nearest Neighbor Search (NNS) and 
# range queries, replacing slow O(N) brute-force comparisons with efficient logarithmic 
# searches.



class Node:
    def __init__(self , point , left = None , right = None):
        self.point = point
        self.left = left
        self.right = right

def build_kd_tree(points , depth = 0):
    if not points:
        return None
    
    k = len(points[0])
    axis = depth % k

    points.sort(key = lambda x : x[axis])
    
    median = len(points) // 2
    return Node(
        point = points[median],
        left = build_kd_tree(points[:median] , depth + 1),
        right = build_kd_tree(points[median + 1:] , depth + 1)
    )
    
    
def print_kd_tree(node , depth = 0):
    if not node:
       return
    print(' ' * depth + f'Level {depth} : {node.point}') 
    print_kd_tree(node.left , depth + 1)
    print_kd_tree(node.right , depth + 1)
    
    

# Example Usage

points = [(2 , 3) , (5 , 4), (9 , 6) , (4 , 7), (8 , 1), (7 , 2)]

root = build_kd_tree(points)

print('KD tree structure')
print_kd_tree(root)