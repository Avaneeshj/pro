a=int(input())
l=list(map(int,input().split()))
b=int(a/2)
c=l[:b]
d=l[b:]
if(sum(c)/len(c) == sum(d)/len(d)):
  print("yes")
else:
  print("no")
