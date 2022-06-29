n=int(input())
k=list(map(int,input().split()))
l=k[0:len(k)//2]
j=k[(len(k)//2):len(k)]
print(sum(l))
print(sum(j))