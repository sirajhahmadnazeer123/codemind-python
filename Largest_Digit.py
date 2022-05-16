num=(int)(input())
z=len(str(num))
y=0
for x in range(z):
    if(num%10>y):
        y=num%10
        num=num//10     
    else:
       num=num//10   
print(y)