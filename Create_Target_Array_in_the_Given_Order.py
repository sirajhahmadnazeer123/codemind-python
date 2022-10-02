n=int(input())
l=list(map(int,input().split()))
p=int(input())
g=list(map(int,input().split()))
s=[]
for i in range(n):
    s.insert(g[i],l[i])
for i in range(n):
    print(s[i],end=' ')
    