n=int(input())
c=list(map(int,input().split()))
s=int(input())
l=0
for i in c:
    if i==s:
        l+=1
if(l>=1):
    print(l)
else:
    print("0")