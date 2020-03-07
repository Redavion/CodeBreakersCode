def caesarCipherEncryptor(string, key):
	myStr = ""
	for c in string:
		print(ord(c))
		numOfLetter = (ord(c) - ord('a') + key) % 26
		myStr += chr(numOfLetter + ord('a')) 
	return myStr
