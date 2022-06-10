c=int(input())
s=list(map(int,input().split()))
j=[]
for i in s:
    if i%2==0:
        j.append(i)
if j==s:
    print("True")
else:
    print("False")