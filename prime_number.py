n=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
if len(l)<=2:
    print("prime")
else:
    print("not a prime")