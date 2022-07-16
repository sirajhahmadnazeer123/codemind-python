n=int(input())
l=list(map(int,input().split()))
if n<3:
    print(max(l))
else:
    k=set(l)
    p=list(k)
    i=0
    while i<2:
        p.remove(max(p))
        i+=1
print(max(p))