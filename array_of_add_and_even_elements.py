n=input()
l=list(map(int,input().split()))
g=[]
f=[]
for i in l :
    if i%2!=0:
        g.append(i)
for i in l:
    if i%2==0:
        f.append(i)
d=g+f
p=str(d)
print(p.strip("[]").replace(",",""))