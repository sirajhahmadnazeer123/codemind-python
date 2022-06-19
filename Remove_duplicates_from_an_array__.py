n=int(input())
j=list(map(int,input().split()))
k=[]
for i in j:
    if i not in k:
        k.append(i)
o=str(k)
print(o.strip("[]").replace(",",""))