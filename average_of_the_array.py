c=int(input())
t=0
f=list(map(int,input().split()))
for i in range(0,len(f)):
    t+=f[i]
    s=t/c
print("%.2f"%s)