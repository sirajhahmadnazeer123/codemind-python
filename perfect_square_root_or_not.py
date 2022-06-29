from math import*
a=int(input())
for i in range(1,int(sqrt(a)+1)):
    c=0
    if i*i==a:
        c=1
if c==1:
    print(True)
else:
    print(False)