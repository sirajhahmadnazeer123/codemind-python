m=int(input())
o=list(map(int,input().split()))
p=[]
l=[]
for i in o:
    for j in range (1,i+1):
        if i%j==0:
            p.append(j)
for i in p:
    if p.count(i)==m:
        l.append(i)
if len(l)>m:
    print(max(l))
else:
    print(min(l))