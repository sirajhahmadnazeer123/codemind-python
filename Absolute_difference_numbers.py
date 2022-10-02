n,a=map(int,input().split())
s=str(n)
f=[]
c=0
l=0
sum=""
p=""
for i in s:
    f.append((i))
for i in f:
    sum+=(i)
    c+=1
    if c==a:
        break
    else:
        continue
for i in f[::-1]:
    p+=i
    l+=1
    if l==a:
        break
    else:
        continue
print(abs(int(sum)-int(p[::-1])))