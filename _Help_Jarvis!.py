n=int(input())
for i in range(n):
    p=str(input())
    d=[]
    for i in p:
        d.append(int(i))
    o=min(d)
    w=max(d)
    s=0
    for i in range(o,w+1):
        if i not in d:
            s+=1
    if(s>=1):
        print("NO")
    else:
        print("YES")
        
        
    