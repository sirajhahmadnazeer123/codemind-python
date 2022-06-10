n=int(input())
h=list(map(int,input().split()))
s1=[]
s2=[]
for i in range(len(h)):
    if h[i]==0:
        s1.append(h[i])
    else:
        s2.append(h[i])
l=str(s1+s2)
print(l.strip("[]").replace(",",""))