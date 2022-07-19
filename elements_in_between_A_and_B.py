n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
for i in x:
    if i in range(a,b+1):
        s.append(i)
if len(s)==0:
    print("-1")
else:
    print(*s)