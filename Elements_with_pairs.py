n=int(input())
l=list(map(int,input().split()))
print(*l,end=" ")
if n%2!=0:
    print(0)