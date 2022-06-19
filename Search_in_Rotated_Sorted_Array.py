n=int(input())
j=list(map(int,input().split()))
k=int(input())
if k in j:
    print(j.index(k))
else:
    print("-1")