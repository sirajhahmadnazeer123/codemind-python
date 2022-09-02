n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
n=len(l)
for i in range(n):
    summ = 0           
    for j in range(i,n):
        summ += l[j]
        if summ == m:
            c+= 1
 
print(c)