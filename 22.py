a=int(input())
b=list(map(int,input().split()))
c=b[1:a:2]
d=b[0:a:2]
if(sum(c)>=sum(d)):
  print(sum(c))
else:
  print(sum(d))
