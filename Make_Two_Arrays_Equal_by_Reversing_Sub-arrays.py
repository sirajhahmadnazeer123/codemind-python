n=int(input())
l=list(map(int,input().split()))
m=int(input())
k=list(map(int,input().split()))
l.sort()
k.sort()
c=0
for i in range(0,len(l)):
    if k[i]==l[i]:
        c+=1
if(c==len(l)):
    print("True")
else:
    print("False")