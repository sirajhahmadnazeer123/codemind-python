n=input()
v="aeiou"
s=[]
for i in v:
    if i not in n:
        s.append(i)
if len(s)==0:
    print("0")
else:
    for i in s:
        print(i,end=" ")
    