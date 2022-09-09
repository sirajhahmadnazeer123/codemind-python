def countList(lst1, lst2):
    return [sub[item] for item in range(len(lst2))
                      for sub in [lst1, lst2]]
p=int(input())
l=list(map(int,input().split()))
a=[]
k=[]
for i in range (0,len(l)//2):
    a.append(l[i])
for i in range (len(l)//2,len(l)):
    k.append(l[i])
c=countList(a,k)
print(*c)