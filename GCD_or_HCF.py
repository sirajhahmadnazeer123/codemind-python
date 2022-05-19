def hcf(a,b):
    for i in range(a,0,-1):
        if a%i==0 and b%i==0:
            return i
            
        
           
a,b=map(int,input().split())
print(hcf(a,b))