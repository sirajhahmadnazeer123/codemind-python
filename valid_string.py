p=input()
s=list(p)
f=[]
for i in s:
    f.append(s.count(i))
if f.count(2)==len(f) or f.count(2)+1==len(f):
    print("Valid String")
else:
    print("Not Valid")
    