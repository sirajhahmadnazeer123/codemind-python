s=list(map(str,input().split()))
m=[]
l=[]
for i in s:
    mi=min(i)
    m.append(mi)
    ma=max(i)
    m.append(ma)
    for j in i:
        l.append(j)
a=min(m)
b=max(m)
print(a,end=' ')
print(l.count(a),end=' ')
print(b,end=' ')
print(l.count(b),end=' ')
    