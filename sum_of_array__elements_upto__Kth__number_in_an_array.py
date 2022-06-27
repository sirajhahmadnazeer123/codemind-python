n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=[]
j=l.index(k)
for i in range(0,len(l)):
    if i<=j:
        c.append(l[i])
        
print(sum(c))