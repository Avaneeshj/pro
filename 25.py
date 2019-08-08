a=int(input())
b=list(map(int,input().split()))
c=1
d=1
for i in range(a):
    if(b[i]>b[i-1]):
        c+=1
    else:
        if(d<c):
            d=c
        c=1
print(c)
