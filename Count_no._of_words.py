def countWords(s):
    if s.strip() == "":
        return 0
 
    words = s.split()
 
    return len(words)
s = input()
print( countWords(s))