b=str(input())
d=[]
q="13579"
for i in b:
    if i in q:
        d.append((int(i)*int(i)))
f=[]
for i in d:
    f.append(str(i))
o=""
for i in f:
    o+=i
print(o)