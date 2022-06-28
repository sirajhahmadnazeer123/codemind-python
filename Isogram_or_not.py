def check_isogram(str1):
    if len(str1) == len(set(str1.lower())):
        return True
    return False
c=input()
print(check_isogram(c))