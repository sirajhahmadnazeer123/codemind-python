n=input().lower()
j="1234567890abcdefghijklmnopqrstuvwxyz "
h="1234567890"
c=0
f=[]
t=[]
for i in n:
    if i not in j:
        c+=1
for i in n:
    if i in h:
        if int(i)%2==0:
            f.append(i)
        else:
            t.append(i)
if c%2==0:
    s=""
    i=0
    j=0
    while i<len(f) or j<len(t):
        if i<len(f):
            s+=f[i]
            i+=1
        if j<len(t):
            s+=t[j]
            j+=1
    print(s)
else:
    s=""
    i=0
    j=0
    while i<len(f) or j<len(t):
        if j<len(t):
            s+=t[j]
            j+=1
        if i<len(f):
            s+=f[i]
            i+=1
    print(s)
    

        