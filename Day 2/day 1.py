"""i=0.0
while (i<1.1):
    print(i)
    i+=0.1
for i in range(0,11):
    print(i/10)
    """
"""
a=75
a=a/4
print("s=",a*3)
print("a=",a)
l=[0,10,0,15,0,9,0,20,0]
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
"""
"""
n=input("Hi whats your name: ")
print("Hello",n,"Welcom to the qiuze")
q1="How many alphabets in english language? \n a.23 \n b.25 \n c.26 \n d.24"
q2="who is the hero in bahubali? \n a.rana \n b.rajamouli \n c.anushka \n d.prabhas"
q3="How many hours in a day? \n a.24 \n b.25 \n c.26 \n d.23"
q={q1:"c",q2:"d",q3:"a"}
j=list(q.keys())
k=list(q.values())
c=0
i=1
def ques():
    print(j[i])
    print("if you want to skip this question (y/n)")
    a=input()
    if a=="n" or a=="no":
        a=input("enter your ans:")
        if a==(k[i]):
           c+=1
           print(c)
           i+=1
           
        
        else:
            c-=1
    else:
        print(c)
    
    
    print(c+1)
ques()
"""
"""
n=input("Hi whats your name: ")
c=0
print("Hello",n,"Welcom to the qiuze")
q1="How many alphabets in english language? \n a.23 \n b.25 \n c.26 \n d.24"
q2="who is the hero in bahubali? \n a.rana \n b.rajamouli \n c.anushka \n d.prabhas"
q3="How many hours in a day? \n a.24 \n b.25 \n c.26 \n d.23"

q={q1:"c",q2:"d",q3:"a"}
for i in q:
    print(i)
    a=input("if you want to skip this question (y/n)")
    if a=="n":
        a=input("enter your ans:")
        if a==(q[i]):
           c+=1
           print("your score:",c)
        else:
            c-=1
    else:
        continue
    a=input("you want to quit y/n:")
    if a=="y":
        print("your total score:",c)
        break
    else:continue
    
"""
"""
l=[[1,2,3],
   [4,5,6],
   [7,8,9]]
d=[[],[],[]]

for i in range (len(l)):
    for j in range (len(l[i])):
        if(i==j):
            d.insert(l[i][j],l[i][j])
        else:
            d.insert(l[i[j]]," ")
for i in d:
    print(i)

            
print(d)
 elif i<j:
            print(l[i][j],end=",")
        elif i>j:
            print(l[i][j],end=",")
        elif i!=j:
            print(l[i][j],end=",")"""
l=[[1,2,3],
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

            
