def countPrimeNumbers(numbers):
    count=0
    for num in numbers:
        if(num<2):
            continue
        else:
            for i in range(2,num):
                if(num%i==0):
                    break
            else:
                count+=1
    return count
l=int(input())
p=list(map(int,input().split()))
print( countPrimeNumbers(p))