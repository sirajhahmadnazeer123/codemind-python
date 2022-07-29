n=input()
d="aeiou"
p=[]
for i in d:
    if i not in n:
        p.append(i)
if len(p)==0:
    print("0")
else:
    print(*p)
    