# Insertion

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if key<root.val:
            root.left = insert(root.left,key)
        else:
            root.right = insert(root.right,key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

root = None
root = insert(root,50)
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)
root = insert(root,70)
root = insert(root,60)
root = insert(root,80)
root = insert(root,100)
print("Inorder Traversal")
inorder_traversal(root)

# Traversal

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        preorder_traversal(root.left)
        preorder_traversal(root.right)
        print(root.val)

def postorder_traversal(root):
    if root:
        print(root.val)
        postorder_traversal(root.left)
        postorder_traversal(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal")
inorder_traversal(root)

print("Preorder Traversal")
preorder_traversal(root)

print("PostOrder Traversal")
postorder_traversal(root)

# Deletion

class Node:
    def __init__(self,key):
        self.left = None
        self.right=None
        self.val = key

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if key<root.val:
            root.left = insert(root.left,key)
        else:
            root.right = insert(root.right,key)
    return root

def delete(root,k):
    if root is None:
        return root
    if root.val>k:
        root.left = delete(root.left,k)
        return root
    elif root.val<k:
        root.right = delete(root.right,k)
        return root
    
    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp
    else:
        succParent = root
        succ = root.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right
        root.val = succ.val
        del succ
        return root
    
root = None
root = insert(root,50)
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)
root = insert(root,70)
root = insert(root,60)

print("Original BST: ",end=" ")
inorder(root)

print("\nDelete a leaf Node: 20")
root = delete(root,20)
print("Modified BST tree after deleting a leaf Node:")
inorder(root)

print("\nDelete a Node with single child: 70")
root = delete(root,70)
print("Modified BST tree after deleting a Node with single child:")
inorder(root)

print("\nDelete a Node with both child: 50")
root = delete(root,50)
print("Modified BST tree after deleting a Node with both child:")
inorder(root)