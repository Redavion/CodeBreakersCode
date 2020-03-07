def isPalindrome(string):
    # Write your code here.
	if len(string) < 0:
		return True
	front = 0
	back= len(string)-1
	while front < back:
		if string[front] != string[back]:
			return False
		front+=1
		back-=1
		
	return True
	
