"""l=[[1,2,3],
   [4,5,6],
   [7,8,9]]

print('the diagonal')
for i in range (len(l)):
    for j in range (len(l[i])):
        if i==j:
            print(l[i][j],end=' ')
        else:
            print("  ",end=" ")
    print()
print('the non diagonal')
for i in range (len(l)):
    for j in range (len(l[i])):
        if i!=j:
            print(l[i][j],end=' ')
        else:
            print("  ",end=" ")
    print()
print('the upper triangle')
for i in range (len(l)):
    for j in range (len(l[i])):
        if i<j:
            print(l[i][j],end='   ')
        else:
            print("   ",end=" ")
    print()
print('the Lower Triangle')
for i in range (len(l)):
    for j in range (len(l[i])):
        if i>j:
            print(l[i][j],end=' ')
        else:
            print("   ",end=" ")
    print()

l=[0,10,0,15,0,9,0,20,0]
k=0l=[0,10,0,15,0,9,0,20,0]
k=0
n=len(l)
for i in range (0,len(l)):
    if(l[i]==0):
        if l[k]!=0:
            l[k],l[i]=l[i],l[k]
            k+=1
        else:
            k+=1
print(l)

n=input()
if "." in n:
    print("float")
else:
    print("int")


"""
"""
l=[1,2,3,4,5,6]
d=[]
for i in range(0,len(l),2):
    d.append(l[i]+l[i+1])
print(d)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
        self.last=None
    def append(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
            
    def display(self):
        c=self.head
        while c is not None:
            print(c.data,end=' ')
            c=c.next
a=LL()
n=int(input('How many elements would you like to enter:'))
for i in range(n):
    data=int(input('enter data item: '))
    a.append(data)
print('the linked list : ',end='->')
a.display()

"""
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SL:
    def __init__(self):
        self.head =None

        
    def display(self):
        if self.head is None:
            print('linked list is empty')
        else:
            t=self.head
            while t:
                print(t.data,end=' ->')
                t=t.next

o=SL()
n=Node(200)
o.head=n
n1=Node(35)
o.head.next=n1
n2=Node(105)
n1.next=n2
n3=Node(109)
n2.next=n3
n4=Node(50)
n3.next=n4
o.display()"""

"""        
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SL:
    def __init__(self):
        self.head =None
        
    def Ib(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
        
    def display(self):
        if self.head is None:
            print('linked list is empty')
        else:
            t=self.head
            while t:
                print(t.data,end=' ->')
                t=t.next



o=SL()
n=Node(200)
o.head=n
n1=Node(35)
o.head.next=n1
n2=Node(105)
n1.next=n2
n3=Node(109)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before inserting")
o.display()
print('\nafter inserting 100')
o.Ib(100)
o.display()
print('\nafter inserting 550')
o.Ib(550)
o.display()"""
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SL:
    def __init__(self):
        self.head =None
        
    def Ib(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def Il(self,data):
        nb=Node(data)
        t=self.head
        while t.next:
            t=t.next
        t.next=nb   
        nb.next=None
        
    def display(self):
        if self.head is None:
            print('linked list is empty')
        else:
            t=self.head
            while t:
                print(t.data,end=' ->')
                t=t.next



o=SL()
n=Node(200)
o.head=n
n1=Node(35)
o.head.next=n1
n2=Node(105)
n1.next=n2
n3=Node(109)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before inserting")
o.display()
print('\nafter inserting 100')
o.Il(100)
o.display()
print('\nafter inserting 550')
o.Il(550)
o.display()
"""
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SL:
    def __init__(self):
        self.head =None
        
    def Ib(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def Il(self,data):
        nb=Node(data)
        t=self.head
        while t.next:
            t=t.next
        t.next=nb   
        nb.next=None
        
    def Im(self,p,data):
        nd=Node(data)
        t=self.head
        f=1
        for i in range(p-1):
            t=t.next
        nd.next=t.next
        t.next=nd
            
        
    def display(self):
        if self.head is None:
            print('linked list is empty')
        else:
            t=self.head
            while t:
                print(t.data,end=' ->')
                t=t.next



o=SL()
n=Node(200)
o.head=n
n1=Node(35)
o.head.next=n1
n2=Node(105)
n1.next=n2
n3=Node(109)
n2.next=n3
n4=Node(5)
n3.next=n4
print("before inserting")
o.display()
print()
o.Im(3,20)
o.Im(5,50)
o.Im(1,23)
o.Im(0,2)
o.Im(8,3)
o.display()

"""


