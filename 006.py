a=int(input())
b=list(map(int,input().split()))
d=[]
for i in range(a):
    for j in range(a):
        for k in range(a):
            if(k>j>i):
                if(b[i]<b[j]<b[k]):
                    e=str(b[i])+str(b[j])+str(b[k])
                    if e not in d:
                        d.append(e)
print(len(d))
