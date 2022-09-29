b=str(input())
k=[]
l=[]
h="1234567890"
c=0
j=""
for i in b:
    if i in h:
        k.append(int(i))
for i in k:
    if i%2==0:
        c+=1
        l.append(i)
if(c==0):
    print(-1)
else:
    g=min(l)
    h=set(k)
    z=list(h)
    z.sort()
    f=[]
    for i in z[::-1]:
        f.append(i)
    for i in f:
        if i==g:
            f.remove(i)
            f.append(g)
    for i in f:
        j+=str(i)
    print(j)
        
    