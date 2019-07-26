a=list(input())
b=[]
d=[]
for i in range(len(a)):
    b=a[i:]
    c=[]
    for j in range(len(b)):
        if b[j] not in c :
            c.append(b[j])
        elif b[j] in c:
            break
        d.append(len(c))
print(max(d))
