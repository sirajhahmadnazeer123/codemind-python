n=int(input())
s=list(map(int,input().split()))
c=0
p=0
for i in s:
    if i%2!=0:
        c+=1
for i in s:
    if i%2==0:
        p+=1
print(p,end=" ")
print(c)