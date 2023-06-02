#using %1 remainder logic

n=input()
n=float(n)
if(n%1==0):
    print('int')
else:
    print('float')
    
#using string fun
n=input()
if '.'in n:
    print('float')
else:
    print('int')