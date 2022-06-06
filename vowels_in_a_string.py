n=input()
v="aeiouAEIOU"
l=input()
for i in n:
    if i==l:
        print("True")
        print(n.index(i))
        break
else:
    print("False")