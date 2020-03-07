def twoNumberSum(array, targetSum):
    # Write your code here.
	myset = set()
	for num in array:
		value = targetSum - num
		if value in myset:
			return [value, num]
		myset.add(num)
	return []
    pass
