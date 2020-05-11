import unittest

class sum:
	def printsum (self, a, b):
		sum = a + b
		if(sum > 0):
			product = "positive " + str(sum)
			return product
		if(sum < 0):
			product = "negative " + str (sum)
			return product
		if(sum == 0):
			product = "positive/negative " + str(sum)
			return product



class printsumTest(unittest.TestCase):

	def setUp(self):
		self.myclass = sum()

	def test_Negativeprintsum(self):

		self.assertEqual(self.myclass.printsum(-4,2) , "negative -2")

	def test_Positiveprintsum(self):

		self.assertEqual(self.myclass.printsum(4,2) , "positive 6")

	def test_Zeroprintsum(self):

		self.assertEqual(self.myclass.printsum(-4,4) , "positive/negative 0")

	def tearDown(self):
		del self.myclass

if __name__ == '__main__':
    unittest.main()