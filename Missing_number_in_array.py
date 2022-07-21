n=int(input())
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    for i in range(1,m+1):
        if i not in l:
            print(i)