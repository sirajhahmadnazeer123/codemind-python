n=input()
s=n.lower()
e=[]
d="abcdefghijklmnopqrstuvwxyz"
for i in s:
    if i in d:
        e.append(i)
f=set(e)
print(len(f))