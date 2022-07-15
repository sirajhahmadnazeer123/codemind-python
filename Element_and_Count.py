n=int(input())
x=list(map(int,input().split()))
s=[]
f=0
for i in x:
    if i not in s:
        s.append(i)
for i in s:
    print(i,x.count(i),end=" ")