def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    c.append(getSum(i))
print(sum(c))
    
