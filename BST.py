class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif(root.val < key) :
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return key
#inorder travarsal
def S(root,key):
    if root is None or root.val==key:
        return root
    elif root.val<key:
        return root

def inord(root):
    if root:
        inord(root.left)
        print(root.val)
        inord(root.right)

        
r=Node(50)
r1=insert(r,30)
r2=insert(r,20)
r3=insert(r,40)
r4=insert(r,70)
r5=insert(r,80)
r6=insert(r,60)
inord(r)
