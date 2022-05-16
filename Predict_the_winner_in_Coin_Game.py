def findwinner(m,n):
    if(m%2==0 or n%2==0):
        return("Player 1")
    else:
        return("Player 2")
m,n=map(int,input().split())
c=(findwinner(m,n))
print(c)