a="abcdefghijklmnopqrstuvwxyz"
b=input()
b=b.lower()
b=b.replace(" ","")
d=list(b)
c=[]
for i in range(len(a)):
    c.append(a[i])
z=0
if(len(d)>=len(c)):
    for j in range(len(c)):
        if c[j] in d:
            z+=1
if(z==26):
    print("yes")
else:
    print("no")
