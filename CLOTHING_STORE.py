n=int(input())
k=list(map(int,input().split()))
l=[]
for i in k:
    if k.count(i)>1:
        l.append(k.count(i))
o=set(l)
j=sum(o)
if j%2==0:
    print((len(l)//2))
else:
    print(int((len(l)/2)-0.5))