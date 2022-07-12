def prime(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in a:
    if prime(i):
        if(i>=k):
            c+=1
print(c)