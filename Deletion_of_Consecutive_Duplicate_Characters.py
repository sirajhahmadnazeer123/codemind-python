f=int(input())
for i in range(f):
    b=str(input())
    l=list(b)
    c=0
    for i in range(0,len(l)-1):
       if l[i]==l[i+1]:
           c+=1
    print(c)