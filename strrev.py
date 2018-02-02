s = input('enter a string:')
i = len(s)-1
rev=" "
while(i>=0):
    rev = rev + s[i]
    i = i-1
    print("reverse:",rev)
