n=int(input())
s=str(n)
c=0
p=0
for i in s:
    if int(i)%2==0:
        c+=1
    else:
        p+=1
if c+p==len(s) and c!=0 and p!=0:
    print("Mixed")
elif p==len(s):
    print("Odd")
else:
    print("Even")