n=int(input())
l=int(input())
o=[]
g=[]
for i in range(1,n):
    if n%i==0:
        o.append(i)
for i in range(1,l):
    if l%i==0:
        g.append(i)
t=sum(o)
p=sum(g)
if p==n and t==l:
    print("Amicable")
else:
    print("Not Amicable")