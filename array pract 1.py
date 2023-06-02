n=int(input())
l=[]
e=[]
a=input().split( )

for i in a:
    if int(i)%2==0:
        
        e.append(int(i))
    else:
        l.append(int(i))
l=l.sort()
e=e.sort()
'''
def s(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]<l[j]:
                l[j],l[i]=l[i],l[j]
            else:
                continue
    return l

e=s(e)
l=s(l)
'''
print
e=e.append(l)
for i in e :
    print(i,end=' ')
