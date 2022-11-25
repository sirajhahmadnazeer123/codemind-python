n=input()
f="aeiouAEIOU"
g=[]
s=[]
for i in range(0,len(n)):
    if n[i] in f:
        g.append(n[i])
        s.append(i)
k=g[::-1]
ind=0
m=[]
for i in range(len(n)):
    if i in s:
        m.append(k[ind])
        ind+=1
    else:
        m.append(n[i])
st=""
for i in m:
    st+=i
print(st)
        
    