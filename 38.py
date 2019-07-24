a,b=map(int,input().split())
c=list(map(int,input().split()))
d=[]
z=0
for i in range(len(c)):
    c[i]=c[i]+b
for j in range(len(c)):
    if c[j]<6:
        d.append(c[j])
e=len(d)
while(e>2):
    z+=1
    e-=3
print(z)
