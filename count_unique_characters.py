n=str(input())
d=list(n.lower())
a="abcdefghijklmnopqrstuvwxyz"
s=[]
for i in d:
    if i in a:
        if d.count(i)==1:
            s.append(i)
print(len(s))