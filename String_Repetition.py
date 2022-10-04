s=input()
n=int(input())
le=len(s)
c1,c3=0,0
for i in s:
    if i=='a':
        c1+=1
l=n//le
k=n%le
c3=l*c1
for i in range(k):
    if s[i]=='a':
        c3+=1
print(c3)