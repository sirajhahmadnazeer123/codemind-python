n=list(map(int,input().split()))
n.sort()
c=n[-1]
b=n[-2]
print((c-1)*(b-1))