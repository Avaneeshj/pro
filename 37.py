a=int(input())
b=list(map(int,input().split()))
c=0
d=0
for i in range(1,a-1):
    if(b[i]>b[i-1] and b[i]>b[i+1]):
        c+=1
    elif(b[i]<b[i-1] and b[i]>>b[i+1]):
        c+=1
if(len(b)==1):
    c+=1
elif(len(b)>1):
    if(b[0]==b[1]):
        d+=1
    elif(b[-1]==b[-2]):
        d+=1
    else:
        c+=2
print(c)
