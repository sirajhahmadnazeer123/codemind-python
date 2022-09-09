l=int(input())
p=list(map(int,input().split()))
i=int(input())
a=max(p)
u=[]
for o in p:
    if o+i>=a:
        u.append("True")
    else:
        u.append("False")
print(*u)
        