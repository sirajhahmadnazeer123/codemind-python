n=input()
d=input()
s=[]
for i in n:
    if i==d:
        s.append(n.index(i))
if len(s)==0:
    print("False")
else:
    print("True")
    print(s[0])