n=int(input())
ts=list(map(int,input().split()))
sum=0
c=0
for i in range(0,len(ts)):
    sum+=ts[i]
si=round(sum//n)
for i in ts:
    if i>=si:
        c+=1
print(c)