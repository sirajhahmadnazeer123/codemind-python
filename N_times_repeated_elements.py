n=int(input())
x=list(map(int,input().split()))
c=[]
q=int(input())
for i in x:
    if x.count(i)==q:
        c.append(i)
if len(c)==0:
    print("-1")
else:
    s=set(c)
    print(*s)