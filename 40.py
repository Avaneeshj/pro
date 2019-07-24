a=['d','h','o','n','i']
b=list(input())
c=0
if(len(a)==len(b)):
    for i in range(len(b)):
        if b[i] in a:
            if(b.count(b[i])==a.count(b[i])):
                c+=1
if(c==5):
    print("yes")
else:
    print("no")
