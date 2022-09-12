n=input()
l=[]
o=[]
k=[]
for i in n.split():
    l.append(i)
for i in l:
    o.append(ord(max(i)))
for i in l:
    k.append(ord(min(i)))
for i in range(0,len(o)):
    print(o[i]-k[i],end=" ")