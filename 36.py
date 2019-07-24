a=int(input())
c=0
b=list(map(int,input().split()))
while(len(b)!=a):
    b.append(9999999)
for i in range(a):
    for j in range(a):
        for k in range(a):
            if(i<j<k):
                if(b[i]>b[j]>b[k]):
                    c+=1
print(c)
