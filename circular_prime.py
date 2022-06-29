def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
def pal(n):
    rev=0
    while n:
        rev=rev*10+n%10
        n=n//10
    return rev
n=int(input())
if prime(n) and prime(pal(n)):
    print('circular prime')
elif prime(n):
    print('prime but not a circular prime')
else:
    print('not prime')