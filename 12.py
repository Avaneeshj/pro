a,b=map(int,input().split())
c=list(map(int,input().split()))
for i in range(b):
  u,v=map(int,input().split())
  print(sum(c[u-1:v]))
