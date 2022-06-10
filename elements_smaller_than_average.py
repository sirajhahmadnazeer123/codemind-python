n=int(input())
h=list(map(int,input().split()))
sum=0
c=0
for i in range(0,len(h)):
    sum=sum+h[i]
l=round(sum/n)
for i in h:
    if i<=l:
        c+=1
print(c)