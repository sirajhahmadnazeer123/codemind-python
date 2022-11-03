n=int(input())
s=[]
for i in range(n):
    i=int(input())
    s.append(i)
d=int(input())
c=0
for i in s:
    if i<=d:
        c+=1
    else:
        c+=2
print(c)