n=input()
k="aeiou"
j="AEIOU"
f=[]
l=[]
for i in n:
    if i in k:
        f.append(i)
for i in n:
    if i in j:
        l.append(i)
k=[]
s=[]
for i in f:
    if i not in k:
        k.append(i)
for i in l:
    if i not in s:
        s.append(i)
if len(k)==5 or len(s)==5:
    print("True")
else:
    print("False")