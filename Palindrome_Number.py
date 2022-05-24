def pal(n):
    temp=n
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if rev==n:
        return True
    else:
        return False
a=int(input())
for i in range(0,a):
    n=int(input())
    print(pal(n))