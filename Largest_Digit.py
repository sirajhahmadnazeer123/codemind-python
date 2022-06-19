num=int(input())
L=0;
while (num > 0):
    
    r=num%10
    if L<r:
        L = r
    num =int(num / 10)
print(L)
