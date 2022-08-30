def prime(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
            
    return 1
n=int(input())
x=list(map(int,input().split()))
s=0
c=0
for i in x:
    if prime(i):
        s+=i
        c+=1
avg=s/c
print('%.2f'%avg)