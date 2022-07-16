n=int(input())
for i in range(n):
    n=int(input())
    p=input()
    c=[]
    f=0
    for o in p:
        if p.count(o)==1:
            c.append(o)
            f=1
    if f==0:
        print("-1")
    else:
        print(c[0])
            