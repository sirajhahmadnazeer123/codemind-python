c=int(input())
k=list(map(int,input().split()))
s=[]
for i in k:
    if i%2==0:
        s.append(i)
print(s[-1])