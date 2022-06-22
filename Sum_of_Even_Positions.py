n=int(input())
l=list(map(int,input().split()))
s=0
g=0
for i in range(0,len(l)):
    if i%2==0:
        g+=l[i]
print(g)
        