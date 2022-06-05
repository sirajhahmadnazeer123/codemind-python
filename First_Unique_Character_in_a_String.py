n=input()
v='abcdefghijklmnopqrstuvwxyz'
c=0
for i in n:
    if n.count(i)==1:
        print(n.index(i))
        break
else:
    print("-1")
    
    