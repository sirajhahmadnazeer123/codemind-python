n=int(input())
l=list(map(int,input().split()))
d=int(input())
p=list(map(int,input().split()))
o=int(input())
c=0
for i in p:
    if i>=o:
        c+=1
if len(p)==p.count(10):
    print(o)
else:
    print(c)