n=int(input())
x=list(map(int,input().split()))
s=0
c=1
p=[]
for i in range(0,n):
    s=s*10+x[i]
c+=s
while c!=0:
    y=c%10
    c=c//10
    p.append(y)
print(*p[::-1])