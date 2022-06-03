def multi(n):
    p=1
    for i in n:
        p=p*i
    return p
n=list(map(int,input().split()))
print(multi(n))