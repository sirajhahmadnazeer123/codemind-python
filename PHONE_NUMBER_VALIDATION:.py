n=int(input())
temp=n
i=0
while temp:
    i+=1
    r=temp%10
    temp//=10
if i==10 and r!=0:
    print("Valid")
else:
    print("Invalid")