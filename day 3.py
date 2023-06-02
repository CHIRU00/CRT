#another logic to find the int and float 
'''
n=input()
c=0
a='1234567890'
for i in n:
    if  i in a:
        pass
    else:
        c+=1
        break
if c!=0:
    print('float')
else:
    print('int')
'''
#deletion linked list elements programs


#deleting first element in single linked list

"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SL:
    def __init__(self):
        self.head =None
        self.tail=None
    def an(self,data):
        nd=Node(data)
        if(self.head==None):
            self.head=nd
            self.tail=nd
        else:
            self.tail.next=nd
            self.tail=nd

    def Ds(self):
        if(self.head==None):
            print("the list is empty")
        elif(self.head!=self.tail):
            self.head=self.head.next
            
        else:
            self.head=self.tail=None

            
            
        
    def display(self):
        c=self.head
        if self.head is None:
            print('linked list is empty')
        while(c!=None):
            print(c.data,end=' ')
            c=c.next
            



o=SL()
o.an(1)
o.an(2)
o.an(3)
o.an(4)
print("before inserting")
o.display()
o.Dl
print()
o.display()

while (o.head!=None):
    o.Ds()
    print('\nupdated list')
    o.display()
"""
#single linked list last element deletion 
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SL:
    def __init__(self):
        self.head =None
        self.tail=None
    def an(self,data):
        nd=Node(data)
        if(self.head==None):
            self.head=nd
            self.tail=nd
        else:
            self.tail.next=nd
            self.tail=nd

    def Ds(self):
        if(self.head==None):
            print("the list is empty")
        elif(self.head!=self.tail):
            self.head=self.head.next
            
        else:
            self.head=self.tail=None
    def Dl(self):
        c=self.head.next
        prev=self.head
        while c.next is not None:
            c=c.next
            prev=prev.next
        prev.next=None

    def Dm(self,p):
        t=self.head.next
        prev=self.head
        for i in range(1,p-1):
            t=t.next
            prev=prev.next
        prev.next=t.next
        t.next=None
        
        

            
            
        
    def display(self):
        c=self.head
        if self.head is None:
            print('linked list is empty')
        while(c!=None):
            print(c.data,end=' ')
            c=c.next
            



o=SL()
o.an(1)
o.an(2)
o.an(3)
o.an(4)
print("before inserting")
o.display()
o.Dl
print()
o.display()

o.Dm(2)
print("\nafter deleting\n")
o.display()
o.Dl()
print()
o.display()
'''

#single linked ist position detetion

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SL:
    def __init__(self):
        self.head =None
        self.tail=None
    def an(self,data):
        nd=Node(data)
        if(self.head==None):
            self.head=nd
            self.tail=nd
        else:
            self.tail.next=nd
            self.tail=nd

    def Ds(self):
        if(self.head==None):
            print("the list is empty")
        elif(self.head!=self.tail):
            self.head=self.head.next
            
        else:
            self.head=self.tail=None
    def Dl(self):
        c=self.head.next
        prev=self.head
        while c.next is not None:
            c=c.next
            prev=prev.next
        prev.next=None

    def Dm(self,p):
        t=self.head.next
        prev=self.head
        for i in range(1,p-1):
            t=t.next
            prev=prev.next
        prev.next=t.next
        t.next=None
        
        

            
            
        
    def display(self):
        c=self.head
        if self.head is None:
            print('linked list is empty')
        while(c!=None):
            print(c.data,end=' ')
            c=c.next
            



o=SL()
o.an(1)
o.an(2)
o.an(3)
o.an(4)
print("before inserting")
o.display()
o.Dl
print()
o.display()

o.Dm(2)
print("\nafter deleting\n")
o.display()
o.Dl()
print()
o.display()

'''

#comparing two single linked lists
'''
class Node:
    def __init__(self,data):
        self.data
        =data
        self.next=None

class SL:
    def __init__(self):
        self.head=None
        self.last=None

    def a(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
def eq(l1,l2):
    c1=l1.head
    c2=l2.head
    while(c1 and c2):
      if c1.data!=c2.data:
            return False
      c1=c1.next
      c2=c2.next
    if c1 is None and c2 is None:
        return True
    else:
        return False
l1=SL()
l2=SL()
d=input("enter elements of first list").split( )
for data in d:
    l1.a(int(data))
d=input("enter elements of second list").split( )
for data in d:
    l2.a(int(data))
if eq(l1,l2):
    print('the linked lists are same')
else:
    print('the linked lists are not same')
'''       
#reversing LL
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SL:
    def __init__(self):
        self.head=None
        

    def Ib(self,nd):
        if self.head is None:
            self.head=nd
        else:
            nd.next=self.head
            self.head=nd
    def display(self):
        c=self.head
        while c is not None:
            print(c.data,end=' ')
            c=c.next
o=SL()
n=int(input('how many elem u want to enter'))
for i in range(n):
    d=input('enter a element')
    o.Ib(Node(d))
print('the linked list:',end=' ')
o.display()
'''
#double linked list
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print('empty')
        else:
            t=self.head
            while t:
                print(t.data,'<-->',end=' ')
                t=t.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.display()
'''
#search in doublelinked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class Dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            return self.head
        else:
            t=self.head
            while(t):
                print(t.data,'-->',end=' ')
                t=t.next
    def Se(self,v):
        if self.head is None:
            return 'linked list is empty '
        else:
            t=self.head
            while t.data==value:
                print('it is present')
                break
            else:
                t=t.next
                if t==None:
                    print('its not found')
o=Dll()
n1=Node(100)
o.head.prev=None
n2=Node(200)
o.head.next=n2
n2.prev=o.head
n3=Node(300)
n2.next=n3
n3.prev=n2
o.search(200)





















        

    
