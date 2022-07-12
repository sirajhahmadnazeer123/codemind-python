n=int(input())
f=list(map(int,input().split()))
d=(sum(f))//n
c=0
for i in f:
    if i == d:
        c+=1
if c==0:
    print("False")
else:
    print("True")