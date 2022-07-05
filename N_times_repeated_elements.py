n=input()
l=list(map(int,input().split()))
o=int(input())
j=[]
for i in l:
    if l.count(i)==o:
        j.append(i)
if len(j)==0:
    print("-1")
else:
    d=set(j)
    print(*d)