class multiply:
	def noStar(a, b):
		if a < 100 and b < 100:
			c = 0
			d = 0
			while d < a:
				c = c + b
				d += 1
			return c
		else:
			print("two digit numbers only")

num1 = int(input()) 
num2 = int(input())

print(noStar(num1, num2))