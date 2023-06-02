'''
n=input("Hi whats your name: ")
print("Hello",n,"Welcom to the qiuze")
q1="How many alphabets in english language? \n a.23 \n b.25 \n c.26 \n d.24"
q2="who is the hero in bahubali? \n a.rana \n b.rajamouli \n c.anushka \n d.prabhas"
q3="How many hours in a day? \n a.24 \n b.25 \n c.26 \n d.23"
q={q1:"c",q2:"d",q3:"a"}
j=list(q.keys())
k=list(q.values())

i=0
def ques(i):
    c=0
    print(j[i])
    print("if you want to skip this question (y/n)")
    a=input()
    if a=="n" or a=="no":
        a=input("enter your ans:")
        if a==(k[i]):
           c+=1
           print('your score is:',c)
           i+=1
        else:
            c-=1
            print('your score is:',c)
            i+=1
        return ques(i)
    else:
        print('your score is:',c)
        i+=1
        return ques(i)
    a=input("Do you want to quite this Quize(y/n)")
    if a=='no' or a=='n':
        pass
    else:
        print('your score is:',c)
    
ques(i)


'''
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
