# A Treap (the word is a portmanteau of Tree + Heap) is a randomized binary search tree 
# data structure that maintains balance with high probability. 
# Each node in a treap is assigned two attributes: 
# A Key (\[X\]): Follows the Binary Search Tree (BST) property (left children are smaller,
# right children are larger). 
# Priority (\[Y\]): A randomly generated value assigned upon node creation that 
# follows the Heap property (typically a Max-Heap, where parents have a higher priority 
# than their children). 


import random

class Node:
    def __init__(self , key):
        self.key = key
        self.priority = random.randint(1 , 100)
        self.left = None
        self.right = None

def rotate_right(y):
    x = y.left
    T = x.right
    x.right = y
    y.left = T
    return x

def rotate_left(x):
    y = x.right
    T = y.left
    y.left = x
    x.right = T
    return y

def insert(root , key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left , key)
        if root.left.priority > root.priority:
            root = rotate_right(root)
    
    elif key > root.key:
        root.right = insert(root.right , key)
        
        if root.right.priority > root.priority:
            root = rotate_left(root)
    return root
    
def search(root , key):
    if root is None:
        return False
    if root.key == key:
        return True
    elif key < root.key:
        return search(root.left , key)
    else:
        return search(root.right , key)
        
def inorder(root):
    if root:
        inorder(root.left)
        print(f'(key = {root.key})')
        inorder(root.right)
            
            
            
# Example Usage

root = None

# Insert keys into treap
for k in [50 , 30 , 20 , 40 , 70 , 60 , 80]:
    root = insert(root , k)
    
print('Inorder traversal of threap (key , priority)')
inorder(root)
print('\n Search for 40 :' , search(root , 40))
print('\n Search for 90 :' , search(root , 90))