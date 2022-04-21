inputline = input ("Input line: ")
letters=0
words=1
space=' '
for char in inputline:
    letters=letters+1
    if char==' ':
        words=words+1
print("words=",words)
print("characters=",letters)