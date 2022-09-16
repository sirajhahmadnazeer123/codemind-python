s=str(input())
f=[]
d=list(s)
f.append(d.count("b"))
f.append(d.count("a"))
f.append(d.count("l"))
f.append(d.count("o"))
f.append(d.count("n"))
if f[1]==0 or f[4]==0 or f[0]==0 or f[3]<=1 or f[2]<=1:
    print("0")
elif f[2]%2!=0 :
    print((f[2]-1)//2)
elif f[3]%2!=0:
    print((f[3]-1)//2)
else:
   print(min(f))
