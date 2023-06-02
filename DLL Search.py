#this is doubly linked list-single linkedlist logic is same
class Node(data):
    def _init_(self,data):
        self.data=data
        self.next=None
        self.prev=None
class SLL:
    def _init_(self):
        self.head=None
    def display_SLL(self):
        if self.head is None:
            return self.head
        else:
            temp=self.head
            while(temp): 
                print(temp.data,"-->",end="")
                temp=temp.next
    def search(self,value):
        if self.head is None:
            return "LL empty"
        else:
            temp=self.head
            while temp:
                if temp.data==value:
                    print("it's present")
                    break
                else:
                    temp=temp.next
                    if temp==None:
                        print("its not present")
obj=SLL()
n1=Node(100)
obj.head=n1
obj.head.prev=None
n2=Node(200)
obj.head.next=n2
n2.prev=obj.head
n3=Node(300)
n2.next=n3
n3.prev=n2
obj.search(200)
