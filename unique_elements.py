n=input()
k=list(map(int,input().split()))
l=[]
for i in k:
    if i not in l:
        l.append(i)
p=str(l)
print(p.strip("[]").replace(",",""))