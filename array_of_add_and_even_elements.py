n=int(input())
l=list(map(int,input().split()))
s=[]
d=[]
for i in l:
    if i%2==0:
        s.append(i)
    else:
        d.append(i)
print(*d,end=' ')
print(*s)