def printsum (a, b):
	sum = a + b
	if(sum > 0):
		print("positive " + str(sum))
	if(sum < 0):
		print("negative " + str (sum))
	if(sum == 0):
		print("positive/negative " + str(sum))
	return

printsum(2, 2)