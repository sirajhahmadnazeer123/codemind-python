n=input()
z=n.split()
l=[]
for i in z:
    vowel=sum(letter in'aeiou' for letter in i.lower())
    l.append(vowel)
i=max(l)
d=[]
print(l.count(i))
        