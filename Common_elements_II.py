a,b=map(int,input().split())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
s3=l+p
for i in s3:
    if s3.count(i)==1:
        print(i,end=" ")