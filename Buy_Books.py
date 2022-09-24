n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
p=sum(l)
x=sum(k)
d=p-x
if d>0:
    print('0')
else:
    print(abs(d))