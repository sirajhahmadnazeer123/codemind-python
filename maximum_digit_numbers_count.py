n=int(input())
c=input()
s=[]
d=str(c)
for i in c.split():
    s.append(len(i))
x=list(c.split())
for i in x:
    if len(i)==max(s):
        print(i,end=" ")
