a,b=map(list,input().split())
c=0
while(len(a)!=len(b)):
    if(len(a)>len(b)):
        b.append("@")
    else:
        a.append("@")
for i in range(len(a)):
    if a[i]==b[i]:
        continue
    else:
        c+=1
print(c)
