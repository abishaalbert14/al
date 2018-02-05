string=input("enter any string:")
if string='x':
break
else:
newstr=string
vowels=('a','e','i','o','u')
for x in string.lower():
if x in vowels:
newstr=newstr.replace(x,"")
print(newstr)
