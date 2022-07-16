from itertools import permutations
n=input()
lisa = [''.join(p) for p in permutations(n)]
for i in lisa:
    print(i)