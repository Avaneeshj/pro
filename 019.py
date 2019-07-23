a=int(input())
b=[]
for i in range(a):
    c=list(map(int,input().split()))
    for j in range(len(c)):
        b.append(c[j])
b.sort()
print(*b,end="")
