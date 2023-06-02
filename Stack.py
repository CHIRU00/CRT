
#stack using list in python
'''
stack=[]
def push():
    e=int(input('enter an element'))
    stack.append(e)
    print(stack)
def pop():
    if not stack:
        print("stack is emptty")
    else:
        e=stack.pop()
        print('removed element is',e)
        print(stack)
while True:
    c=int(input('select operations 1.push 2.pop 3.quit 4.display'))
    if c==1:
        push()
    elif(c==2):
        pop()
    elif(c==4):
        print(stack)
    else:
        break
'''
#works -5 to 256.9 
'''
n=256
d=n//1
if(id(n)==id(d)):
    print('int')
else:
    print('float')
'''
# works for all
'''
n=input()
try:
    int(n)
    print('int')
except:
    print('float')
    
'''
#stack using linked list


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head ==None:
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            nd=node(data)
            nd.next=self.head
            self.head=nd
    def pop(self):
        if self.isempty ():
            return None
        else:
            pn=self.head
            self.head=self.head.next
            pn.next=None
            return pn
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        t=self.head
        if self.isempty():
            print('the stack is empty')
        else:
            while(t!= None):
                print(t.data,end='<-')
                t=t.next
            return
if __name__=='__main__':
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.display()
    print()
    s.peek()
    print(s.peek())
    s.pop()
    s.pop()
    print()
    s.display()
    print()
    print(s.peek())

    
        
        
    


