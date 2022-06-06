c=input()
p=c.lower()
v=p.split()
o="aeiou"
b="bcdfghjklmnpqrstvwxyz"
m=0
for i in v:
    if i[0] in o and i[-1]:
        m+=1
print(m)
        