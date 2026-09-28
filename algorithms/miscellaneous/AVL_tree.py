# An AVL tree is a self-balancing binary search tree
# Balance Factor: The height difference between the left and right subtrees for 
# any node is at most one.
# Performance: Operations like search, insertion, and deletion run in \(O(\log n)\) time.
# Rotations: The tree uses rotations (left, right, left-right, right-left) to fix 
# imbalances after insertions or deletions. 



class Node:
    def __init__(self , key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        
class AVLTree:
    def getHeight(self , root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self , root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def rightrotate(self , y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.getHeight(y.left) , self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left) , self.getHeight(x.right))
        return x
    
    def leftrotate(self , x):
        y = x.right
        T2  = y.left
        y.left = x
        x.right = T2
        y.height = 1 + max(self.getHeight(x.left) , self.getHeight(x.right))
        x.height = 1 + max(self.getHeight(y.left) , self.getHeight(y.right))
        return x
    
    def insert(self , root , key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left , key)
        else:
            root.right = self.insert(root.right , key)
            
        root.height = 1 + max(self.getHeight(root.left) , self.getHeight(root.right))
        balance = self.getBalance(root)
        
        if balance > 1 and key < root.left.key:
            return self.rightrotate(root)
        if balance < -1 and key > root.right.key:
            return self.leftrotate(root)
        
        if balance > 1 and key > root.left.key:
            root.left = self.leftrotate(root.left)
            return self.rightrotate(root)
        
        if balance < -1 and key < root.right.key:
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)
        
        return root
    
    def inorder(self , root):
        if not root:
            return
        self.inorder(root.left)
        print(root.key , end = '')
        self.inorder(root.right)
        
        
        
        
# Example Usage

tree = AVLTree()
root = None
nums = [10 , 20 , 30 , 40 , 50 , 25]

for num in nums:
    root = tree.insert(root , num)
    
print('Inorder Traversal of the constructed AVL tree is')
tree.inorder(root)