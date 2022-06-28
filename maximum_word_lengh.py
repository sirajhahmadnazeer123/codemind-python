n=input()
s=[]
for i in n.split():
    s.append(len(i))
s.sort()
print(s[-1])
    