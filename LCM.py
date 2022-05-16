def lcm(a,b):
    c=b
    while True:
        if c%a==0 and c%b==0:
            return c
        c+=1
a,b=map(int,input().split())
print(lcm(a,b))
