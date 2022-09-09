k=int(input())
h=list(map(int,input().split()))
d=int(input())
k=[]

for i in range(0,len(h)):
    if h[i]==d:
        k.append(i)
p=set(k)
if len(k)==0 :
    print("-1","-1")
elif len(p)==1:
    print(*p,end=" ")
    print(*p)
else:
    print(*p)