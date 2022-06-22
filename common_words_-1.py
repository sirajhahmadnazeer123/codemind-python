def passori(s,n):
    s=s.lower()
    n=n.lower()
    sp=s.split(" ")
    np=n.split(" ")
    return len(list(set(sp)&set(np)))
n=input()
k=input()
print(passori(n,k))