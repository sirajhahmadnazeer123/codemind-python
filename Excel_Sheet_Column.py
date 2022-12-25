def convertToTitle(n):
    title = ""
    while n:
        n = n - 1
        title = chr(n % 26 + 65) + title
        n = n // 26
    return title
n=int(input())
print(convertToTitle(n))