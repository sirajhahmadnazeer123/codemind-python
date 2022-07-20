a,b=map(int,input().split())
o=list(map(int,input().split()))
q=0
for i in o:
    if i%b==0:
        q+=1
print(q)