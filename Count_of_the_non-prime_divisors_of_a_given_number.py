n=int(input())
r=[]
p=[]
c=0
for i in range(1,n+1):
    if n%i==0:
        r.append(i)
for a in range(2,n+1):
    k=0
    for i in range(2,a):
        if(a%i==0):
            k=k+1
    if(k<=0):
        p.append(a)
for i in r:
    if i not in p:
        c+=1
print(c)