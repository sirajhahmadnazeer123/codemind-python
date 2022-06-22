n=input()
k=input()
c=0
for i in n.split():
    if i in k.split():
        if k.count(i)==1:
            if n.count(i)==1:
                c+=1
print(c)