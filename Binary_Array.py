l=int(input())
n=list(map(int,input().split()))
if n.count(1)+n.count(0)==l:
    print("True")
else:
    print("False")