def sel(n):
    s=0
    a=n
    d=len(str(n))
    while a!=0:
        r=a%10
        a=a//10
        if r==0:
            continue
        elif n%r==0:
            s+=1
    if(s==d):
        return n
a=int(input())
b=int(input())
for i in range(a,b+1):
    if (i==sel(i)):
        print(i,end=" ")