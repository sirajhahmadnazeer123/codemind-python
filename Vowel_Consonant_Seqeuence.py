s=str(input())
s.lower()
d="aeiou"
p=""
l=""
for i in s:
    if i in d:
        p+="V"
    else:
        p+="C"
for i in range(0,len(p)-1):
    if p[i]!=p[i+1]:
        l+=p[i]
l+=p[-1]
print(l)