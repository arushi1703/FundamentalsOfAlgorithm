class Node:
    def __init__(self, data):
        self.val=data
        self.left=None
        self.right=None
        self.prev=None

def insert(root, newnode):
    if root is None:
        root=newnode
    else:
        newnode.prev=root
        if root.val<newnode.val:
            if root.right is None:
                root.right=newnode
            else:
                insert(root.right,newnode)
        else:
            if root.left is None:
                root.left=newnode
            else:
                insert(root.left,newnode)

def delete(root,value):
    current=root
    while(current.val!=value): #traversing through the tree 
        if(value>current.val):
            current=current.right
        else:
            current=current.left
    #we have the node to be deleted
             
    parent=current.prev
    
    if current.left is None and current.right is None: #for leaf node
        if parent.val>current.val:
            parent.left=None
        else:
            parent.right=None

    else:   #for intermediate node
        if current.right=None: #if there is no right subtree
            repNode=maximumNode(root)
        else:
            repNode=minimumNode(root)
            
def maximumNode
        

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

r=Node(8)
insert(r,Node(3))
insert(r,Node(1))
insert(r,Node(6))
insert(r,Node(4))
insert(r,Node(10))

print("Inorder: ",end=" ")
inorder(r)
delete(r,4)
print("\nInorder: ",end=" ")
inorder(r)



        
