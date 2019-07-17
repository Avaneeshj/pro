a,b=map(int,input().split())
c=list(map(int,input().split()))
d=[]
for i in range(b):
  u,v=map(int,input().split())
  d=c[u-1:v]
  print(min(d))
