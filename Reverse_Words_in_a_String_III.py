def p(Str):
    q= Str.split(" ")
    o = [q[::-1] for q in q]
    l= " ".join(o)
  
    return l
  
tom=input()
print(p(tom))
