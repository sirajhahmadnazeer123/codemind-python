n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    maxi=0
    for j in range(i+1,n):
        if(maxi<a[j]):
            maxi=a[j]
    print(maxi,end=' ')
print(-1)