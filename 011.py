a=int(input())
b=[]
c=0
for i in range(a):
    b.append(i)
for i in range(a):
    for j in range(a-1):
        if(i>j):
            c+=1
print(c)
