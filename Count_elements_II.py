n,m=map(int,input().split())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
f=[]
for i in l:
    if i not in p:
        f.append(i)
for i in p:
    if i not in l:
        f.append(i)
d=set(f)
print(len(d))