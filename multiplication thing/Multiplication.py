def noStar(a, b):
	c = 0
	d = 0
	while d < a:
		c = c + b
		d += 1
	return c

num1 = int(input()) 
num2 = int(input())

noStar(num1, num2)