n=input()
l=n.lower()
s=l.split()
c=0
for i in s:
    if i==i[::-1]:
        c+=1
print(c)
    