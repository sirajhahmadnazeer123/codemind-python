n=int(input())
h=list(map(int,input().split()))
c=[]
j=[]
u=0
y=0
for i in range (0,len(h)):
    if i%2:
        c.append(h[i])
    else:
        j.append(h[i])
for p in range(0,len(j)):
    y=y+j[p]
for o in range(0,len(c)):
    u=u+c[o]
g=y-u
if g==0:
    print("YES")
else:
    print("NO")
    
 