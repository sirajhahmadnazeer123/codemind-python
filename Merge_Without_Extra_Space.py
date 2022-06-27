n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    i=list(map(int,input().split()))
    s=str(sorted(l+i))
    print(s.strip("[]").replace(",",""))