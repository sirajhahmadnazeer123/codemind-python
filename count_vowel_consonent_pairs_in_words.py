n=input()
k=n.lower()
s=[]
m=0
a='aeiou'
for i in n.split():
    s.append(i)
for i in s:
    l=len(i)
    k=1
    n=0
    for j in range(0,l):
        if i[j] in a and i[0-k] not in a or i[j] not in a and i[0-k] in a:
            n+=1
        k+=1
    m+=n
print(m//2)