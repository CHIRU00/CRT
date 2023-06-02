class btn:
    def __init__ (self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

n1=btn(50)
n2=btn(20)
n3=btn(45)
n4=btn(11)
n5=btn(15)
n6=btn(30)
n7=btn(78)
n1.leftChild=n2
n1.rightChild=n3
n2.leftChild=n4
n2.rightChild=n5
n3.leftChild=n6
n3.rightChild=n7
print("root note is",n1.data)
print('left child of node is:',n1.leftChild.data)
print('right Chid of node is:',n1.rightChild.data)
print('node is:',n2.data)
print('left child of node is',n2.leftChild.data)
print('right child of node is:',n2.rightChild.data)

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data
def pin(r):
    if r:
        pin(r.left)
        print(r.val,end=' ')
        pin(r.right)
def pir(r):
    if(r):
        pir(r.left)
        pir(r.right)
        print(r.val,end=' ')
def ppr(r):
    if(r):
        print(r.val,end=' ')
        ppr(r.left)
        ppr(r.right)
r=Node(100)
r.left=Node(150)
r.right=Node(1)
r.left.left=Node(250)
r.left.left.right=Node(300)
r.right.right=Node(2)
r.right.right.right=Node(3)
r.right.right.right.left=Node(4)
print()
print('inorder')
pin(r)
print('\n post order')
pir(r)
print('\n pre order')
ppr(r)
