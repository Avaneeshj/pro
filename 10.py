a=int(input())
b=list(map(int,input().split()))
c=0
d=[]
for i in range(a-1):
    if b[i]<b[i+1]:
        d=b[0:i+1]
        c+=sum(d)
print(c)
