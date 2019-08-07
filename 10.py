a=int(input())
b=list(map(int,input().split()))
c=0
e=[]
d=[]
for i in range(a-1):
    d=b[:i+2]
    k=0
    f=len(d)
    while(k<f):
        if(d[-1]>d[k]):
            e.append(d[k])
            k+=1
        else:
            k+=1
c+=sum(e)
print(c)
