n=int(input())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
j=[]
for i in range(0,len(l)):
    j.append(l[i]+p[i])
print(*j)