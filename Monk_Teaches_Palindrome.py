n=int(input())
for i in range(0,n):
    a=input()
    c=len(a)
    d=a[: :-1]
    if d!=a:
        print("NO")
    elif d==a and c%2==0:
        print("YES EVEN")
    else:
        print("YES ODD")
    
    