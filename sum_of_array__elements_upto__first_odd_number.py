n=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    if i%2==0:
        c+=i
    else:
        break
print(c)