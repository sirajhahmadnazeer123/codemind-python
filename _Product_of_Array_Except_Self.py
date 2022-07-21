def multiplylist(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result
n=int(input())
l=list(map(int,input().split()))
c=multiplylist(l)
s=[]
for i in l:
    s.append(c//i)
print(*s)