n=int(input())
k=[]
p=list(map(int,input().split()))
for i in p:
    if p.count(i)==i:
        k.append(i)
if len(k)==0:
    print("-1")
else:
    p=set(k)
    o=list(p)
    c=sum(p)/len(p)
    print("%.2f"%c)