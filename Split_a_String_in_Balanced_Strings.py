def balance_split(s):
    e=0
    a=0
    max=0
    for i in s:
        if i=="L":
            e+=1
        else:
            a+=1
        if e==a:
            max+=1
            e=0
            a=0
    return max
s=str(input())
print(balance_split(s))