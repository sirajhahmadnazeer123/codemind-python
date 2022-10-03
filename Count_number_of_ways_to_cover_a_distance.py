def countWays(n):
    if (n == 0):
        return 1
    if (n <= 2):
        return n
 
    f0 = 1
    f1 = 1
    f2 = 2
    ans = 0
 
    for i in range(3, n + 1):
        ans = f0 + f1 + f2
        f0 = f1
        f1 = f2
        f2 = ans
    return ans
 


n=int(input())
print(countWays(n))
