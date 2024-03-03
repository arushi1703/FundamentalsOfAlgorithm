class Node:
    def __init__(self, data):
        self.val=data
        self.left=None
        self.right=None

class BST:
    def __init__(self,value):
        self.root=Node(value)
        
    def insert(self,root, newnode):
        if root is None:
            root=newnode
        else:
            if root.val<newnode.val:
                if root.right is None:
                    root.right=newnode
                else:
                    self.insert(root.right,newnode)
            else:
                if root.left is None:
                    root.left=newnode
                else:
                    self.insert(root.left,newnode)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

    def preorder(self,root):
        if root:
            print(root.val, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=' ')

b=BST(100)
b.insert(b.root,Node(20))
b.insert(b.root,Node(10))
b.insert(b.root,Node(5))
b.insert(b.root,Node(120))
b.insert(b.root,Node(102))

print("Inorder: ")
b.inorder(b.root)
print("\nPreorder: ")
b.preorder(b.root)
print("\nPostorder: ")
b.postorder(b.root)

        
