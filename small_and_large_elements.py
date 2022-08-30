n=input()
s=[]
for i in n.split():
    s.append(i)
a=[]
d=[]
for i in s[0]:
    a.append(i)
for i in s[-1]:
    d.append(i)
print(min(a),max(d))