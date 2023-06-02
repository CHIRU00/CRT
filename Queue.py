'''
from queue import LifoQueue
s=LifoQueue(maxsize=3)
print(s.qsize())
s.put('a')
s.put('b')
s.put('c')
print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())

print(s.empty())

'''
#take a string as input which should be combination of paranthase ()
#using srtack find out you input is balanced or not
s=input()
st=[]
balance=True

for i in s:
    if i=='('or i=='{'or i=='[':
        st.append(i)
    elif i==']' or i=='}' or i==')':
        if(len(st)==0):
            balance=False
    elif(i==')' ):
        if(len(st) and st.pop()!='('):
            balance=False
            break

    elif(i==']' ):
        if(len(st) and st.pop()!='['):
            balance=False
            break
    elif(i=='}' ):
        if(len(st) and st.pop()!='{'):
            balance=False
            break

if(balance==False or len(st)):
   print('imbalance')
else:
    print('balance')

           

        

    
