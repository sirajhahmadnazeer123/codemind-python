n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
for i in l:
    if i not in range(a,b+1):
        s.append(i)
if len(s)==0:
    print("-1")
else:
    print(max(s))