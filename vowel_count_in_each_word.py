n=input()
z=n.split()
l=[]
for i in z:
    vowel=sum(letter in'aeiou' for letter in i.lower())
    l.append(vowel)
d=str(l)
print(d.strip("[]").replace(",",""))