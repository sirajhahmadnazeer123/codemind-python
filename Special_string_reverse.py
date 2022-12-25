s=input()
d="abcdefghijklmnopqrstuvwxyz"
o=""
f=[]
p=[]
l=[]
t=[]
for i in range(0,len(s)):
    if s[i] not in d:
        p.append(s[i])
        l.append(i)
    else:
        t.append(s[i])
for i in t:
    o+=i
for i in o[::-1]:
    f.append(i)
for i in range(0,len(l)):
    f.insert(l[i],p[i])
v=""
for i in f:
    v+=i
print(v)
    
            