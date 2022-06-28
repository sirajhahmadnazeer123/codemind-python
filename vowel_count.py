n=input()
v="aeiouAEIOU"
s=[]
for i in n:
    if i  in v:
        s.append(i)
print(len(s))