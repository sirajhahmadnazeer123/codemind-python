n=input()
s=[]
for i in n:
    if n.count(i)==1:
        s.append(i)
d=len(s)
if d==0:
    print("-1")
else:
    print(s[0])
