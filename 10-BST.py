class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def insert(root, newnode):
    if root is None:
        return newnode
    if newnode.val < root.val:
        root.left = insert(root.left, newnode)
    else:
        root.right = insert(root.right, newnode)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
        

r = Node(100)
r = insert(r, Node(20))
r = insert(r, Node(10))
r = insert(r, Node(50))
r = insert(r, Node(120))
r = insert(r, Node(102))
r = insert(r, Node(180))

inorder(r)
