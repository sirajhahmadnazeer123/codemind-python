num=int(input())
sqr=num*num
#Sum of digit
sum=0
while sqr!=0:
    rem = sqr % 10
    sum += rem
    sqr //= 10

if sum==num:
    print("Neon Number")
else:
   print("Not Neon Number")