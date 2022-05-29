l=int(input())
u=int(input())
for x in range(l,u+1):
    temp=x
    t=0
    while temp:
        r=temp%10
        temp//=10
        if r==0:
            t=1
            break
        elif x%r>0:
            t=1
            break
    if t==0:
        print(l,end=" ")
    l+=1