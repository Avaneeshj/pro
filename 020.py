j,a=map(int,input().split())
b=list(map(int,input().split()))[:j]
b.sort(reverse=True)
c=0
d=int(b[-1])
while(a>0):
    for i in range(len(b)):
       if(a>=b[i]):
           a=a-b[i]
           c+=1
           if(a<d and a!=0):
               c=-1
           else:
               break
if(c<=0):
    print("it's not possible")
else: 
    print(c)
