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