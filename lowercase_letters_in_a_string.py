n=input()
M="abcdefighjklmnopqrstuvwxyz"
c=0
for i in n:
    if i in M:
        c+=1
print(c)