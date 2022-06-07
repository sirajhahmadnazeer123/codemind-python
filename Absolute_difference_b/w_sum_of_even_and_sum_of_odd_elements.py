n=int(input())
positions=list(map(int,input().split()))
d=[]
o=[]
for i in positions:
    if i%2!=0:
        d.append(i)
        s=(sum(d))
for i in positions:
    if i%2==0:
        o.append(i)
        product=(sum(o))
print(abs(s-product))