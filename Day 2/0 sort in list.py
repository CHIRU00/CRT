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