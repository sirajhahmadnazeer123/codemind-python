c,a=map(int,input().split())
j=list(map(int,input().split()))
p=max(j)
b=0
k=0
s=[]
for i in j:
    if i<=a:
        b+=1
    else:
        k+=1
    if(k<=1):
        continue
    else:
        break
print(b)
    
