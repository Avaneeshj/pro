a=list(input())
b=[]
d=[]
for i in range(len(a)):
    if a[i] not in b :
        b.append(a[i])
    elif a[i] in b:
        break
    d.append(len(b))
print(max(d))
