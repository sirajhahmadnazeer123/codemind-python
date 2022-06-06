def isPalindrome(s):
    return s == s[::-1]
s = input()
d=s.lower()
ans = isPalindrome(d)
 
if ans:
    print("True")
else:
    print("False")