def reverse(n):
    sum=0
    sign=1
    if n<0:
        sign=-1
        n=n*-1
    while n>0:
        rem=n%10
        sum=sum*10+rem
        n//=10
    if not -1234569<sum<12344555:
        return 0
    return sign*sum
n=int(input())
print(reverse(n))