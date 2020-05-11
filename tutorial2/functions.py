def addition(list):
	i = 0
	for numbers in list:
		i += numbers
	print (i)


def multiply(list):
	i = 1
	for numbers in list:
		i = i*numbers
	print(i)

def conc(list):
	sentance = ""
	for words in list:
		sentance = sentance + " " + words
	print(sentance)
