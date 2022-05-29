n=int(input())
for i in range(n):
    a=int(input())
    for j in range(1,(a//2)+1):
        if pow(j,2)==a:
            print(True)
            break
    else:
        print(False)