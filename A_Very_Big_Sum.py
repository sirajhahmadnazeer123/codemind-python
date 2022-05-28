n=int(input())
a=list(map(int,input().split()))
total=0
for i in range(0,len(a)):
    total=total+a[i]
print(total)