a=input()
c=0
for j in a:
    if j.isdigit():
        c+=1
if c>=1:
    print("Contains",c,"digit")
else:
    print("Doesn't contain digit")
     