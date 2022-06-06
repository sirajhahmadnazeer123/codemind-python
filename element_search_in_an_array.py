c=int(input())
f=list(map(int,input().split()))
c=int(input())
for i in f:
    if i==c:
        print("True")
        break
else:
    print("False")