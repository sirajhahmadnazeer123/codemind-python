c=input()
d=c.lower()
p=0
v="abcdefghijklmnopqrstuvwxyz1234567890 "
for i in d:
    if i not in v:
        p+=1
print(p)