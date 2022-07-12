n=int(input())
l=list(map(int,input().split()))
o=int(input())
c=0
for i in l:
    if i==o:
        c+=1
print(c)