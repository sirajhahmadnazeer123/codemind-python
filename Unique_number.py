n=int(input())
temp=n
m=n
t=0
while temp:
    r1=temp%10
    c=0
    while n:
        r2=n%10
        n//=10
        if r1==r2:
            c+=1
    if c>1:
        print("Not Unique Number")
        t=1
        break
    temp//=10
    if t==1:
        break
    n=m
if t==0:
    print("Unique Number")