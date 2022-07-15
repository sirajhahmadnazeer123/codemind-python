a,b=map(int,input().split())
x=list(map(int,input().split()))
c=0
for i in x:
    if i%b==0:
        c+=1
print(c)