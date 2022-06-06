v=input()
d=v.lower()
f=" "
p=0
for i in d:
    if i not in f:
        p+=1
print(p)