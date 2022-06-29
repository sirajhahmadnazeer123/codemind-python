n=input()
p=input()
o=p.lower()
j=n.lower()

s=0
for i in j.split():
    if i in o.split():
        s+=1
print(s)
    