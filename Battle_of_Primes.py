def prime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
            
        return True
        
m=int(input())
n=int(input())
a=m+n
for i in range(1,100):
    if prime(a+i):
        print(i)
        break