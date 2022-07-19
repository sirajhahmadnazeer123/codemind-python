n=int(input())
x=list(map(int,input().split()))
c=0
s=[]
f=[]
for i in x:
    if i not in s:
        s.append(i)
for i in s:
    if x.count(i)==i:
        f.append(i)
        c=1
if(c==1):
    g=sum(f)/len(f)
    print("%.2f"%g)
else:
    print('-1')