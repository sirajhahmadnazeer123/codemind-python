a,b=map(int,input().split(':'))
pov=abs(30*a-((11/2)*b))
dov=360-pov
if pov<dov:
    print(pov)
else:
    print(dov)