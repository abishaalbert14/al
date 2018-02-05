while True:
	print("Enter 'x' for exit.")
	string = input("Enter any string: ")
	if string == 'x':
		break
	else:
		newstr = string
		print("\nRemoving vowels ")
		vowels = ('a', 'e', 'i', 'o', 'u')
		for x in string.lower():
			if x in vowels:
				newstr = newstr.replace(x,"")
		print("New string ")
		print(newstr,"\n")
		
		
