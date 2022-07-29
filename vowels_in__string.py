n=input()
d="aeiouAEIOU"
p=[]
for i in n:
    if i in d:
        p.append(i)
if len(p)==0:
    print("-1")
else:
    f=[]
    for i in p:
        if i not in f:
            f.append(i)
    print(*f)