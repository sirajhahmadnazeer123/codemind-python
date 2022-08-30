n=input()
s=[]
for i in n.split():
    s.append(i)
h=0
l=0
for i in s:
    h+=ord(max(i))
    l+=ord(min(i))
print(h-l)
    