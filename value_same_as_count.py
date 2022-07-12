n=input()
l=list(map(int,input().split()))
v=[]
for i in l:
    if l.count(i)==i:
        v.append(i)
print(len(set(v)))
        