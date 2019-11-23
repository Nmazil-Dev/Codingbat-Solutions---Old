def front_back(str):
	new = []
	length =  len(str) -1
	first = (str[0])
	last = str[length]
	new.append(last)
	for i in range(1, length):
		new.append(str[i])
	new.append(first)
	word = ''.join(new)
	if len(str) == 1:
		print(str)
	else:
		print(word)





front_back('sacwe')