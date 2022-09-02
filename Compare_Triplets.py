l=list(map(int,input().split()))
p=list(map(int,input().split()))
c=0
s=0
for i in range(0,len(p)):
    if l[i]>p[i]:
        c+=1
print(c,end=" ")
for i in range(0,len(p)):
    if p[i]>l[i]:
        s+=1
print(s,end=" ")
    