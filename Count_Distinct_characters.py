n=input()
s=n.lower()
e=[]
k=''
d="abcdefghijklmnopqrstuvwxyz"
for i in s:
    if i in d:
        e.append(i)
p=set(e)
j=list(p)
j.sort()
print(len(j))