n=input()
l=list(map(int,input().split()))
s=l[0:len(l)//2]
h=l[len(l)//2:len(l)]
p=sum(s)
o=sum(h)
print(abs(p-o))