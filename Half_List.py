n=int(input())
l=list(map(int,input().split()))
s=l[0:len(l)//2]
p=l[len(l)//2 :len(l)]
o=p[::-1]
r=str(o+s)
print(r.strip("[]").replace(",",""))