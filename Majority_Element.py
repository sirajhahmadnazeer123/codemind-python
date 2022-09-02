n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    s.append(l.count(i))
d=max(s)
for i in l:
    if l.count(i)==d:
        print(i)
        break