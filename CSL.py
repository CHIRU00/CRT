class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class Cl:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head
        
    def an(self,data):
        nd=Node(data)
        if self.head.data is None:
            self.head=nd
            self.tail=nd
            nd.next=self.head
        else:
            self.tail.next=nd
            self.tail=nd
            self.tail.next=self.head
    def display(self):
        cr=self.head
        if self.head is None:
            print("list is empty")
            return
        else:
            print('nodes of CLL')
            print(cr.data,'-->')
            while (cr.next != self.head) :
                cr=cr.next
                print(cr.data,'-->')
                
class CLL:
    cl=Cl()
    cl.an('s')
    cl.an('m')
    cl.an('i')
    cl.an('l')
    cl.an('e')
    cl.display()



            
            
            
            
