def powerset(array):
    # Write your code here.

	if len(array) == 0:
		return [[]]
	
	listoflists = powerset(array[:-1])
	for i in range(len(listoflists)):
		newlist = listoflists[i] + [array[-1]]
		listoflists.append(newlist)
	return listoflists
