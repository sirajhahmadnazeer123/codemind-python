n=int(input())
positions=list(map(int,input().split()))
d=[]
for i in positions:
    if i%2==0:
        d.append(i)
print(sum(d))