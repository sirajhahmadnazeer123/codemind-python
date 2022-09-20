c=int(input())
k=int(input())
o=[]
l=[]
for i in range(1,c):
    if c%i==0:
        o.append(i)
for i in range(1,k):
    if k%i==0:
        l.append(i)
if(sum(l)==c and sum(o)==k):
    print("Amicable")
else:
    print("Not Amicable")
